#coding=utf-8
import datetime

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.db.models import Q, Max, Min, Sum, Avg, F, Count
from django.db import connection

from .models import Stock
from .forms import StockForm
import logging

logger=logging.getLogger('django.request')

#获得当前持仓股票的最近交易记录
class HoldLastDealView(ListView):
    model = Stock
    template_name = 'stock/list.html'

    def get_queryset(self):
        object_list=[]
        hold_stock_code_list=Stock.objects.values('stock_code').annotate(per_stock_hold=Sum('volume')).exclude(per_stock_hold=0).values_list('stock_code',flat=True).order_by('stock_code')
        #logger.info('hold stock code list: %s', hold_stock_code_list)
        for hold_stock_code in hold_stock_code_list:
            #只要股份增加，或是钱减少，就算是买入
            stock_stat_in=Stock.objects.filter(stock_code=hold_stock_code,operation__in=[u'申购中签',u'证券买入',u'红股入账',u'股息红利税补']).order_by().aggregate(last_deal_day=Max('deal_date'))
            #logger.info('stock buy deal date: %s', stock_stat_in)
            object_list.append(Stock.objects.filter(stock_code=hold_stock_code,operation__in=[u'申购中签',u'证券买入',u'红股入账',u'股息红利税补'],deal_date=stock_stat_in['last_deal_day'].strftime('%Y-%m-%d'))[0])
            #股票减少，或是钱增加，就算是卖出
            stock_stat_out=Stock.objects.filter(stock_code=hold_stock_code,operation__in=[u'证券卖出',u'股息入账']).order_by().aggregate(last_deal_day=Max('deal_date'))
            #logger.info('stock sell deal date: %s, and its type: %s', stock_stat_out, type(stock_stat_out))
            if stock_stat_out['last_deal_day']:
                object_list.append(Stock.objects.filter(stock_code=hold_stock_code,operation__in=[u'证券卖出',u'股息入账'],deal_date=stock_stat_out['last_deal_day'].strftime('%Y-%m-%d'))[0])
        return object_list

class IndexView(TemplateView):
    template_name = "stock/index.html"

#持仓股票的最新状态
class PositionDetailView(TemplateView):
    template_name = 'stock/clearance_list.html'

    def get_context_data(self,**kwargs):
        context = super(ClearanceView, self).get_context_data(**kwargs)
        #先找出持仓的股票代码
        hold_stock_code_list=Stock.objects.values('stock_code').annotate(per_stock_hold=Sum('volume')).exclude(per_stock_hold=0).values_list('stock_code',flat=True).order_by('stock_code')
        #取出各代码，逐一分析
        object_list=[]
        for clear_stock in hold_stock_code_list:
            obj={'stock_code':clear_stock}
            #先将股票名称，首次及末次交易日期，净利润，总买卖次数统计出来
            stock_name_list=Stock.objects.filter(stock_code=clear_stock).values_list('stock_name',flat=True)
            obj['stock_name']=stock_name_list[0]
            stock_stat_p1=Stock.objects.filter(stock_code=clear_stock).aggregate(first_deal_day=Min('deal_date'),last_deal_day=Max('deal_date'),profit=Sum('amount'))
            obj['first_deal_day'],obj['last_deal_day'],obj['profit']=stock_stat_p1['first_deal_day'],stock_stat_p1['last_deal_day'],stock_stat_p1['profit']
            obj['transaction_count']=Stock.objects.filter(stock_code=clear_stock,operation__in=[u'申购中签',u'证券买入',u'证券卖出']).aggregate(transaction_count=Count('deal_id'))['transaction_count']
            #然后是持股天数，日均利润，买卖频率(以次/周为单位)
            obj['hold_days']=(obj['last_deal_day']-obj['first_deal_day']).days
            obj['avg_daily_profit']=round(float(obj['profit'])/float(obj['hold_days']),3)
            obj['transaction_freq']=round(float(obj['transaction_count'])/float(obj['hold_days'])*7,3)
            clear_stock_deals=Stock.objects.filter(stock_code=clear_stock)
            #然后取出最高持仓量以及其最新日期
            obj['max_balance']=clear_stock_deals.aggregate(max_balance=Max('balance'))['max_balance']
            obj['max_balance_day']=Stock.objects.filter(stock_code=clear_stock,balance=obj['max_balance'])[0].deal_date
            object_list.append(obj)
        profits=sum(obj['profit'] for obj in object_list)
        context['object_list']=sorted(object_list, key=lambda obj: obj['profit'], reverse=True)
        context['profits']=profits
        return context


#单个股票交易记录
class StockListView(ListView):
    model = Stock
    template_name = 'stock/list.html'

    def get_queryset(self):
        return Stock.objects.filter(stock_code=self.kwargs['stock_code'])

#清仓股票
class ClearanceView(TemplateView):
    template_name = 'stock/clearance_list.html'

    def get_context_data(self,**kwargs):
        context = super(ClearanceView, self).get_context_data(**kwargs)
        #先找出已经清仓的股票代码
        clear_stock_code_list=Stock.objects.values('stock_code').annotate(per_stock_hold=Sum('volume')).filter(per_stock_hold=0).values_list('stock_code',flat=True).order_by('stock_code')
        #取出各代码，昨一分析
        object_list=[]
        for clear_stock in clear_stock_code_list:
            obj={'stock_code':clear_stock}
            #先将股票名称，首次及末次交易日期，净利润，总买卖次数统计出来
            stock_name_list=Stock.objects.filter(stock_code=clear_stock).values_list('stock_name',flat=True)
            obj['stock_name']=stock_name_list[0]
            stock_stat_p1=Stock.objects.filter(stock_code=clear_stock).aggregate(first_deal_day=Min('deal_date'),last_deal_day=Max('deal_date'),profit=Sum('amount'))
            obj['first_deal_day'],obj['last_deal_day'],obj['profit']=stock_stat_p1['first_deal_day'],stock_stat_p1['last_deal_day'],stock_stat_p1['profit']
            obj['transaction_count']=Stock.objects.filter(stock_code=clear_stock,operation__in=[u'申购中签',u'证券买入',u'证券卖出']).aggregate(transaction_count=Count('deal_id'))['transaction_count']
            #然后是持股天数，日均利润，买卖频率(以次/周为单位)
            obj['hold_days']=(obj['last_deal_day']-obj['first_deal_day']).days
            obj['avg_daily_profit']=round(float(obj['profit'])/float(obj['hold_days']),3)
            obj['transaction_freq']=round(float(obj['transaction_count'])/float(obj['hold_days'])*7,3)
            clear_stock_deals=Stock.objects.filter(stock_code=clear_stock)
            #然后取出最高持仓量以及其最新日期
            obj['max_balance']=clear_stock_deals.aggregate(max_balance=Max('balance'))['max_balance']
            obj['max_balance_day']=Stock.objects.filter(stock_code=clear_stock,balance=obj['max_balance'])[0].deal_date
            object_list.append(obj)
        profits=sum(obj['profit'] for obj in object_list)
        context['object_list']=sorted(object_list, key=lambda obj: obj['profit'], reverse=True)
        context['profits']=profits
        return context

#持仓股票
class PositionView(ListView):
    model=Stock
    template_name = 'stock/position_list.html'

    def get_queryset(self,**kwargs):
        #先找出目前持仓的股票代码
        hold_stock_code_list=Stock.objects.values('stock_code').annotate(per_stock_hold=Sum('volume')).exclude(per_stock_hold=0).values_list('stock_code',flat=True).order_by('stock_code')
        #取出代码逐一分析
        object_list=[]
        for hold_stock in hold_stock_code_list:
            obj={'stock_code':hold_stock}
            #先将股票名称，首次及最近交易日期，持仓总成本，总买卖次数统计出来
            stock_name_list=Stock.objects.filter(stock_code=hold_stock).values_list('stock_name',flat=True)
            obj['stock_name']=stock_name_list[0]
            stock_stat_p1=Stock.objects.filter(stock_code=hold_stock).aggregate(first_deal_day=Min('deal_date'),recent_deal_day=Max('deal_date'),cost=Sum('amount'))
            #以下的持仓总成本一般为负数，但有可能为正的，原因是之前的操作的已获利金额超过当前成本
            obj['first_deal_day'],obj['recent_deal_day'],obj['cost']=stock_stat_p1['first_deal_day'],stock_stat_p1['recent_deal_day'],stock_stat_p1['cost']
            obj['transaction_count']=Stock.objects.filter(stock_code=hold_stock,operation__in=[u'申购中签',u'证券买入',u'证券卖出']).aggregate(transaction_count=Count('deal_id'))['transaction_count']
            #然后是当前持股天数，买卖频率(以次/周为单位)
            obj['hold_days']=(datetime.date.today()-obj['first_deal_day']).days
            obj['transaction_freq']=round(float(obj['transaction_count'])/float(obj['hold_days'])*7,3)
            #最后针对该股票的每条交易记录，进行最新持仓量的计算
            hold_stock_deals=Stock.objects.filter(stock_code=hold_stock)
            #然后先计算平均持股成本，再取出最高持仓量以及其最新日期
            obj['balance']=hold_stock_deals[0].balance
            obj['avg_cost']=round(float(obj['cost'])/float(obj['balance']),3)
            obj['max_balance']=hold_stock_deals.aggregate(max_balance=Max('balance'))['max_balance']
            obj['max_balance_day']=Stock.objects.filter(stock_code=hold_stock,balance=obj['max_balance'])[0].deal_date
            object_list.append(obj)
        return object_list

#新增记录
class StockCreate(CreateView):
    template_name='stock/stock_form.html'
    form_class = StockForm

    def get_success_url(self):
        return reverse('stock:recent_deal')
