/*已清仓股票排行*/
---------------------------------------
/*按日均利润*/
select stock_code,stock_name, sum(amount) as '净利润', 
min(deal_date) as '首次交易日期', max(deal_date) as '最后交易日期', 
datediff(max(deal_date),min(deal_date)) as '持股天数', 
sum(amount)/datediff(max(deal_date),min(deal_date)) as '日均利润' 
from stock group by stock_code having sum(volume)=0 order by 日均利润 DESC
/*按总利润*/
select stock_code,stock_name, sum(amount) as '净利润', 
min(deal_date) as '首次交易日期', max(deal_date) as '最后交易日期', 
datediff(max(deal_date),min(deal_date)) as '持股天数', 
sum(amount)/datediff(max(deal_date),min(deal_date)) as '日均利润' 
from stock group by stock_code having sum(volume)=0 order by 净利润 DESC
/*按持股天数*/
select stock_code,stock_name, sum(amount) as '净利润', 
min(deal_date) as '首次交易日期', max(deal_date) as '最后交易日期', 
datediff(max(deal_date),min(deal_date)) as '持股天数', 
sum(amount)/datediff(max(deal_date),min(deal_date)) as '日均利润' 
from stock group by stock_code having sum(volume)=0 order by 持股天数 DESC
----------------------------------------------------------------------------------------------------------------------------------------
/*未清仓股票成本分析*/
select stock_code,stock_name,sum(amount) as '总成本/已获得收益',min(deal_date) as '首次交易日期',max(deal_date) as '最近交易日期',datediff(curdate(),min(deal_date)) as '当前持股天数' from stock group by stock_code having sum(volume)!=0 order by sum(amount) desc

/*增加新交易记录*/
insert into stock(deal_date,stock_code,stock_name,operation,volume,balance,avg_price,turnover,amount,brokerage,stamp_tax,transfer_fee)
VALUES
('2019-03-26','600686','金龙汽车','证券买入',900,10800,10.9,9810,-9815.2,5,0,0.2),
('2019-03-27','600686','金龙汽车','证券买入',1000,11800,9.99,9990,-9995.2,5,0,0.2),
('2019-03-27','601789','宁波建工','证券买入',1900,30700,4.32,8208,-8213.16,5,0,0.16);
