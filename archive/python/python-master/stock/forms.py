#coding=utf-8
from django import forms
from stock.models import Stock
import logging

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        exclude=['deal_id']

    #校验新增交易记录时所要输入的全部字段，连内部逻辑关系，也要严格检查
    def clean(self):
	cleaned_data = super(StockForm, self).clean()
	#把前面全部的字段先提取出来
        stock_code = cleaned_data.get("stock_code")
        stock_name = cleaned_data.get("stock_name")
        operation = cleaned_data.get("operation")
        volume = cleaned_data.get("volume")
        balance = cleaned_data.get("balance")
        avg_price = cleaned_data.get("avg_price")
        turnover = cleaned_data.get("turnover")
        amount = cleaned_data.get("amount")
        brokerage = cleaned_data.get("brokerage")
        stamp_tax = cleaned_data.get("stamp_tax")
        transfer_fee = cleaned_data.get("transfer_fee")
        #使用一条大的日志记录全部校验字段的类型，长度，值等主要属性
        logging.info(u"""股票代码字段类型：%s， 值：%s
                        股票名称字段类型：%s， 值：%s
                        操作字段类型：%s， 值：%s
                        成交数量字段类型：%s， 值：%d
                        成交均价字段类型：%s， 值：%f
                        成交金额字段类型：%s， 值：%f
                        发生金额字段类型：%s， 值：%f
                        佣金字段类型：%s， 值：%f
                        印花税字段类型：%s， 值：%f
                        过户费字段类型：%s， 值：%f
                        """ % (type(stock_code),stock_code,
                            type(stock_name),stock_name,
                            type(operation),operation,
                            type(volume),volume,
                            type(avg_price),float(avg_price),
                            type(turnover),float(turnover),
                            type(amount),float(amount),
                            type(brokerage),float(brokerage),
                            type(stamp_tax),float(stamp_tax),
                            type(transfer_fee),float(transfer_fee),
                            ))
	#先对每个字段逐一进行单独分析
	#首先是股票代码，必须满足全数字，且长度为6位，而且本人操作的全部为6或0开头的主板股票
        if not (stock_code.isdigit() and stock_code.startswith(('6','0')) and len(stock_code)==6):
            msg = "股票代码必须为6位数字，且以0或6开头"
            self.add_error('stock_code', msg)

        #按下来是股票名称，通常总长不会少于7个字符（至少2个中文）
        if not len(stock_name)>=3:
            msg = "股票名称的长度不少于3"
            self.add_error('stock_name', msg)

        #成交数量通常在正负10000股之内，并且与操作严格匹配
        if operation==u'证券买入':
            #买入必须是整百股，买入时股票增加，因此必须是正数
            if not (10000>volume>0 and volume % 100 ==0):
                msg = "买入时数量要为正，且必须整手（百股）的买"
                self.add_error('volume', msg)
        elif operation==u'证券卖出':
            #卖出时股票减少，因此必须是负数
            if not (-10000<volume<0 and volume % 100 ==0):
                msg = "卖出时数量必须为负"
                self.add_error('volume', msg)
        elif operation==u'申购中签':
            #申购规则较复杂，且对于一个签位，沪市是1000股，深市则为500股
            if stock_code.startswith('6'):
                if not (10000>volume>0 and volume % 1000 ==0):
                    msg = "沪市申购1000股一个签位"
                    self.add_error('volume', msg)
            elif stock_code.startswith('0'):
                if not (10000>volume>0 and volume % 500 ==0):
                    msg = "深市申购500股一个签位"
                    self.add_error('volume', msg)
        elif operation==u'红股入账':
            #必须是正数
            if not 10000>volume>0:
                msg = "送股必须是正数"
                self.add_error('volume', msg)
        elif operation in (u'股息入账',u'股息红利税补'):
            #股息相关则无成交数量
            if volume!=0:
                msg = "股息没有成交"
                self.add_error('volume', msg)

        #最新持股数量=之前的最新持股数量+当前成交数量
        """
        新买入股票由于之前无持仓量，会导致检索异常，因此暂停该校验
        if balance!=Stock.objects.filter(stock_code=stock_code)[0].balance+volume:
            msg = "变动后的持股数量输入有误"
            self.add_error('balance', msg)

        #成交均价通常0~300之间，实际上基本不可能超过100
        if not 300>avg_price>0:
            msg = "买卖价格必须为正,且不得超过300"
            self.add_error('avg_price', msg)
        """

        #成交金额部分：如果为买卖，则成交金额为成交均价乘以成交数量的积的绝对值
        if operation in (u'证券买入',u'证券卖出',u'申购中签'):
            if not float(turnover)==abs(float(avg_price)*volume):
                msg = "成交金额计算错误，请自查"
                self.add_error('turnover', msg)
        elif operation in (u'股息入账',u'股息红利税补'):
            if not turnover>0:
                msg = "成交金额必须大于0"
                self.add_error('turnover', msg)
        elif operation==u'红股入账':
            if not turnover==0:
                msg = "必须没有成交金额"
                self.add_error('turnover', msg)

        #佣金计算
        if operation in (u'证券买入',u'证券卖出'):
            if not float(brokerage)==max(round(float(turnover)*2.5/10000,2),5):
                msg = "佣金计算错误，请自查"
                self.add_error('brokerage', msg)
        else:
            if not brokerage==0:
                msg = "佣金必须为0"
                self.add_error('brokerage', msg)

        #印花税计算
        if operation==u'证券卖出':
            if not float(stamp_tax)==round(turnover/1000,2):
                msg = "印花税计算错误，请自查"
                self.add_error('stamp_tax', msg)
        else:
            if not stamp_tax==0:
                msg = "非卖出股票不收印花税"
                self.add_error('stamp_tax', msg)

        #过户费计算，由于官方的过户费计算方式中，分的取舍有问题，导致无法得知其是执行四舍五入，还是直接截掉，因此该校验暂停
        """
        if operation in (u'证券买入',u'证券卖出'):
            if not float(transfer_fee)==round(float(turnover)*0.02/1000.0,2):
                msg = "过户费计算错误，请自查"
                self.add_error('transfer_fee', msg)
        else:
            if not transfer_fee==0:
                msg = "其它情况不收过户费"
                self.add_error('transfer_fee', msg)
        """

        #发生金额计算
        if operation==u'证券买入':
            if stock_code.startswith('6'):
                if not (float(amount)==float(-turnover-brokerage-transfer_fee)):
                    msg = "沪市买入时，发生金额为成交+佣金+过户费的结果的负值"
                    self.add_error('amount', msg)
            elif stock_code.startswith('0'):
                if not (float(amount)==float(-turnover-brokerage)):
                    msg = "深市买入时，发生金额为成交+佣金的结果的负值（过户费虽计算，但并不扣减）"
                    self.add_error('amount', msg)
        elif operation==u'证券卖出':
            if stock_code.startswith('6'):
                if not (float(amount)==float(turnover-brokerage-stamp_tax-transfer_fee)):
                    msg = "沪市卖出时，发生金额为成交-佣金-印花税-过户费"
                    self.add_error('amount', msg)
            elif stock_code.startswith('0'):
                if not (float(amount)==float(turnover-brokerage-stamp_tax)):
                    msg = "深市卖出时，发生金额为成交-佣金-印花税（过户费虽计算，但并不扣减）"
                    self.add_error('amount', msg)
        elif operation in (u'申购中签',u'股息红利税补'):
            if not amount==-turnover:
                msg = "申购及税补时发生金额为成交金额取负"
                self.add_error('amount', msg)
        elif operation in (u'红股入账',u'股息入账'):
            if amount!=turnover:
                msg = "送红股及发股息时，发生金额与成交金额必定相同"
                self.add_error('amount', msg)
