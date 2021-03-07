#coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),
    #最近10条交易
    #url(r'^recent_deal/$',views.RecentDealView.as_view(),name='recent_deal'),
    #持仓股票的最近买卖交易
    url(r'^hold_last_deal/$',views.HoldLastDealView.as_view(),name='hold_last_deal'),
    # 清仓股票分析
    url(r'^clearance/$',views.ClearanceView.as_view(),name='clearance'),
    # 持仓股票分析
    url(r'^position/$',views.PositionView.as_view(),name='position'),
    # 新增记录
    url(r'^add/$',views.StockCreate.as_view(),name='add'),
    # 个股记录列表
    url(r'^stock_code/(?P<stock_code>(0|6)[0-9]{5})/$',views.StockListView.as_view(),name='stock_code'),
]
