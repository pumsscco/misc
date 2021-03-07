#coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    # 首页，包含有常用功能的使用方法
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 购买信息入口页面
    # 装备购买索引页
    url(r'^buy/equip/$',views.BuyEquipIndexView.as_view(),name='buy_equip_index'),
    url(r'^buy/(?P<equip_type>sword|dsword|instrument|helmet|corselet|legharness|ornament)/$',views.BuyEquipView.as_view(),name='buy_equip'),
    # 道具购买
    url(r'^buy/property/$',views.BuyPropertyIndexView.as_view(),name='buy_property_index'),
    url(r'^buy/(?P<pr_type>dh|sw|dg|df|cx|ck|cq)/$',views.BuyPropertyView.as_view(),name='buy_property'),
    # 配方购买
    url(r'^buy/prescription/$',views.BuyPrescriptionIndexView.as_view(),name='buy_prescription_index'),
    url(r'^buy/(?P<pre_type>zz((_(wt|wl|wm|m|y|x))|02|03))/$',views.BuyPrescriptionView.as_view(),name='buy_prescription'),

    # 怪物信息类
    url(r'^monster/$',views.MonsterIndexView.as_view(),name='monster_index'),
    # 怪物汇总表
    url(r'^monster/sum/$',views.MonsterSumView.as_view(),name='monster_sum'),
    # 掉落及偷窃详情
    url(r'^monster/stolen_drop/$',views.MonsterStolenDropView.as_view(),name='monster_stolen_drop'),
    # 技能及额外属性追加
    url(r'^monster/skill_extra_p/$',views.MonsterSkillExtraPView.as_view(),name='monster_skill_extra_p'),
    # 抗性及反弹
    url(r'^monster/resist_rebound/$',views.MonsterResistReboundView.as_view(),name='monster_resist_rebound'),
    # 五基本属性及五灵属性
    url(r'^monster/monster/fp_wuling/$',views.MonsterFPWulingView.as_view(),name='monster_fp_wuling'),
    # 怪物基本表
    url(r'^monster/basic/$',views.MonsterBasicView.as_view(),name='monster_basic'),

    # 任务全记录
    url(r'^mission/$',views.MissionView.as_view(),name='mission'),
    # 仙术列表
    url(r'^magic/$',views.MagicView.as_view(),name='magic'),
    # 获得道具的方式罗列
    url(r'^getproperty/$',views.PropertyGetView.as_view(),name='getproperty'),
    url(r'^getequip/$',views.EquipGetView.as_view(),name='getequip'),
    url(r'^getsceneitem/$',views.SceneItemGetView.as_view(),name='sceneitems'),
]
