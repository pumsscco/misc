#coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q

from .models import *
from .forms import *
import logging, re

#物品的购买获取途径的详细信息
def item_buy_source(item_id):
    #购买信息数组
    shop_list=[]
    #先从Good表中获取物品作为商品的出售信息
    buy_info_list=Good.objects.filter(goods_id=item_id).values('shop_id','goods_type','open_condition','open_num')
    #针对每一条店铺信息，深入挖掘
    for buy_info in buy_info_list:
        shop={}
        #以下是深入查询店铺信息的部分
        #先查ShopProperty表获得其店铺名称，位置，及类型
        shop_info=Shopproperty.objects.get(pk=buy_info['shop_id'])
        #根据店铺位置查Scene表，获得场景外部区块的列表，同样去除夜景
        scene_outers=Scene.objects.filter(Q(scene=shop_info.position),~Q(section__endswith='Y'),Q(type=0)).values('section','name')
        #如果只有一个外部区块，就直接取这个区块的名字
        if len(scene_outers)==1:
            shop['container']=scene_outers[0]['name']
        #否则，就要比较外部区块名称与店铺区块名称的命名规则了
        else:
            #根据店铺名称查Scene表，获得店铺区块编码，去除掉夜景重复的店铺
            try:
                shop_section=Scene.objects.get(Q(name=shop_info.name),Q(scene=shop_info.position),~Q(section__endswith='Y'))
            except:
                shop_section=None
            #有的话，就是正规店铺，没有就是小摊贩及NPC
            if shop_section:
                #对比外部区块代码的最后字母与店铺区块的首字母，相同，就是容器区块了
                for scene_outer in scene_outers:
                    if shop_section.section[0]==scene_outer['section'][-1]:
                        shop['container']=scene_outer['name']
                        break
                #包含进播仙镇的特殊情况
                if 'container' not in shop:
                    shop['container']=scene_outers[0]['name']
            #小摊贩及NPC则取外部区块的第一个做为容器区域
            else:
                shop['container']=scene_outers[0]['name']
        #店铺类型的名称
        shop['type_name']=Shoptype.objects.get(pk=shop_info.type).content
        #然后是查询开放条件对应的任务名称
        if buy_info['open_condition'] and buy_info['open_num']:
            shop['quest_name']=Mission.objects.get(trunk=buy_info['open_condition'],quest_id=buy_info['open_num']).name
        #接下来是店铺名称
        shop['shop_name']=shop_info.name
        #再接下来是开放条件对应的委托任务名
        shop['quest_name']='无' if 'quest_name' not in shop else shop['quest_name']
        shop_list.append(shop)
    return shop_list

#物品的掉落获取途径的详细信息
def item_drop_source(item_id):
    drop_info=Monster.objects.filter(Q(mdt_1_id=item_id)|Q(mdt_2_id=item_id)|Q(mdt_3_id=item_id)|Q(mdt_4_id=item_id)).values('monster_id','ma_name','is_boss')
    return drop_info

#物品的偷窃获取途径的详细信息
def item_steal_source(item_id):
    steal_info=Monster.objects.filter(ca_losable_property=item_id).values('monster_id','ma_name','is_boss')
    return steal_info

#场景内物品或宝箱拾取途径的详细信息
def item_pick_source(item_id):
    pick_info_list=Sceneitem.objects.filter(Q(si_ea_id=item_id)|Q(si_pa_id=item_id)|Q(si_item_1_id=item_id)|Q(si_item_2_id=item_id)|Q(si_item_3_id=item_id)|Q(si_item_4_id=item_id)|Q(si_item_5_id=item_id)|Q(si_item_6_id=item_id)).values('scene','section','si_id','si_model_path','si_model','si_texture','si_coor_x','si_coor_y','si_coor_z')
    #logging.info('item_pick_source, pick_info_list after query db:  %s', pick_info_list)
    pick_info_array=[]
    for pick_info in pick_info_list:
        #先直接查Scene表获得区域名称
        try:
            section_name=Scene.objects.get(scene=pick_info['scene'],section=pick_info['section'])
        except:
            continue
        if pick_info['scene'].startswith('Q'):
            #处理城镇室外场景的情况
            if section_name.type==0:
                pick_info['section_name']=section_name.name
                #判断夜景情况，追加后缀
                if pick_info['section'].endswith('Y'):
                    pick_info['section_name']+=u'（夜）'
            #处理城镇室内场景的情况
            elif section_name.type==1:
                #找其室外区域的名称，先判定室外区域数量
                container_num=Scene.objects.filter(scene=pick_info['scene'],type__exact=0).exclude(section__endswith='Y').count()
                if container_num==1:
                    container=Scene.objects.get(scene=pick_info['scene'],section=pick_info['scene'])
                else:
                    try:
                        container=Scene.objects.get(scene=pick_info['scene'],section__endswith=pick_info['section'][0])
                    except:
                        container=Scene.objects.get(scene=pick_info['scene'],section=pick_info['scene'])
                pick_info['section_name']=container.name+u'__'+section_name.name
                if pick_info['section'].endswith('Y') or (len(pick_info['section'])>2 and pick_info['section'][-2]=='Y'):
                    pick_info['section_name']+=u'（夜）'
        elif pick_info['scene'].startswith('M'):
            #处理迷宫场景的情况
            pick_info['section_name']=section_name.name
            if pick_info['section'].endswith('Y') or (len(pick_info['section'])>2 and pick_info['section'][-2]=='Y'):
            #if pick_info['section'].endswith('Y'):
                pick_info['section_name']+=u'（夜）'
        pick_info_array.append(pick_info)
    #logging.info('before return, pick_info_array:  %s', pick_info_array)
    return pick_info_array

#列出道具获得途径的全部方法，包括店铺购买，从怪物身上掉落，偷窃，以及场景内拾取
class PropertyGetView(View):
    #以下部分是处理表单的视图的模板，不要忘了修改
    form_class = PropertyNameForm
    template_name = 'db_ana/pa_input.html'

    def get_all_methods(self, pa_name):
        #先从Property表获得道具的部分基本信息，其中最重要的是ID
        prop={}
        try:
            p=Property.objects.get(pa_name=pa_name)
            #logging.info('after get property basic info, the property obj is  %s', p)
            prop['id'],prop['pa_name'],prop['pa_price']=p.id,p.pa_name,p.pa_price
            tmp=Propertyclass.objects.get(id=p.pa_type.id)
            #logging.info('after get propertyclass, the pa_type is  %s', p.pa_type)
            prop['type_name']=tmp.content
            #查店铺
            shops=item_buy_source(p.id)
            #然后是掉落
            drops=item_drop_source(p.id)
            #然后是偷窃
            steals=item_steal_source(p.id)
            #最后是拾取
            picks=item_pick_source(p.id)
            return (prop,shops,drops,steals,picks)
        except:
            return (None,None,None,None,None)

    def get(self, request, *args, **kwargs):
        #form = self.form_class(initial=self.initial)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #手工及选择的先都抓取
            p_obj=form.cleaned_data['manual_input']
            logging.info('In post of view, the property name is  %s', p_obj.pa_name)
            self.template_name='db_ana/property_get_view.html'
            prop,shops,drops,steals,picks=self.get_all_methods(p_obj.pa_name)
            return render(request, self.template_name, {'prop': prop, 'shops': shops, 'drops': drops, 'steals': steals, 'picks': picks})

        return render(request, self.template_name, {'form': form})


#列出装备获得途径的全部方法，包括店铺购买，以及场景内拾取
class EquipGetView(View):
    #以下部分是处理表单的视图的模板，不要忘了修改
    form_class = EquipNameForm
    template_name = 'db_ana/ea_input.html'

    def get_all_methods(self, ea_name):
        #先从Equip表获得装备的部分基本信息，其中最重要的是ID
        eq={}
        try:
            e=Equip.objects.get(ea_name=ea_name)
            #ea为装备本身的基本信息
            eq['id'],eq['ea_name'],eq['ea_price']=e.id,e.ea_name,e.ea_price
            tmp=Equiptype.objects.get(id=e.ea_type.id)
            eq['type_name']=tmp.content
            #查店铺，shops为装备直接购买信息
            shops=item_buy_source(e.id)
            #如果店铺查不到，查配方表
            if not shops:
                #pres为配方信息，pres_shops为配方购买信息
                try:
                    pres=Prescription.objects.get(pra_name=e.ea_name)
                    pres_shops=item_buy_source(pres.id)
                except:
                    pres=pres_shops=None
            else:
                pres=pres_shops=None
            #最后是拾取
            picks=item_pick_source(e.id)
            return (eq,shops,pres,pres_shops,picks)
        except:
            return (None,None,None,None,None)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #把下拉列表的数据抓回作为参数
            e_obj=form.cleaned_data['select_input']
            logging.info('In post of view, the equip name is  %s', e_obj.ea_name)
            self.template_name='db_ana/get_equip.html'
            eq,shops,pres,pres_shops,picks=self.get_all_methods(e_obj.ea_name)
            return render(request, self.template_name, {'eq': eq, 'shops': shops, 'pres': pres, 'pres_shops': pres_shops, 'picks': picks})

        return render(request, self.template_name, {'form': form})

#依场景列出拾取信息，为宝箱党提供查询便利
class SceneItemGetView(View):
    form_class = SceneNameForm
    template_name = 'db_ana/scene_input.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #先找场景的名称与场景的类型
            sn_obj=form.cleaned_data['select_input']
            scene_id,scene_name=sn_obj.scene,sn_obj.cn_name
            if scene_id.startswith('M'):
                scene_type=u'迷宫'
            elif scene_id.startswith('Q'):
                scene_type=u'城镇'
            #然后把该场景的物品信息全部整理出来
            scene_items=Sceneitem.objects.filter(scene=scene_id)
            scene_item_list=[]
            for scene_item in scene_items:
                si={}
                try:
                    so=Scene.objects.get(scene=scene_item.scene,section=scene_item.section)
                except:
                    continue
                #最后分析整理，先整理出室外区块名称
                if scene_type==u'迷宫':
                    si['container']='N/A'
                elif scene_type==u'城镇':
                    section_type=so.type
                    #该区块本身即是室外区块，就无须再填了
                    if section_type==0:
                        si['container']='N/A'
                    elif section_type==1:
                        #找室外区块，先尝试只一个室外区块的情况，再按命名规则找多个室外区块中的正确的那个
                        try:
                            si['container']=Scene.objects.get(scene=scene_id,section=scene_id).name
                        except:
                            si['container']=Scene.objects.get(scene=scene_id,section__endswith=scene_item.section[0]).name
                #然后确认本身区块名称，追加夜景的补充说明到该名称中
                si['section_name']=so.name
                if len(scene_item.section)>=2:
                    if scene_item.section.endswith('Y') or (scene_item.section[-2]=='Y' and scene_item.section[-1].islower()):
                        si['section_name']+=u'（夜）'
                #物品ID
                si['si_id']=scene_item.si_id
                #外观类型
                if scene_item.si_model=='OM06':
                    si['appearance']=u'特殊矿石'
                elif scene_item.si_model=='OM07':
                    si['appearance']=u'小宝箱'
                elif scene_item.si_model=='OM08':
                    si['appearance']=u'大宝箱'
                elif scene_item.si_model=='OM09':
                    si['appearance']=u'隐藏宝箱'
                elif scene_item.si_model=='OM10':
                    si['appearance']=u'上锁宝箱'
                elif scene_item.si_model=='OQ20':
                    si['appearance']=u'钱'
                elif re.search('^CK',scene_item.si_model):
                    si['appearance']=u'矿石'
                elif re.search('^DF',scene_item.si_model):
                    si['appearance']=u'辅助道具'
                elif re.search('^DH',scene_item.si_model):
                    si['appearance']=u'恢复道具'
                elif re.search('^DG',scene_item.si_model):
                    si['appearance']=u'攻击道具'
                elif re.search('^JQ',scene_item.si_model):
                    si['appearance']=u'剧情道具'
                elif re.search('^WT',scene_item.si_model):
                    si['appearance']=u'剑'
                elif re.search('^WL',scene_item.si_model):
                    si['appearance']=u'双剑'
                elif re.search('^WM',scene_item.si_model):
                    si['appearance']=u'琴'
                elif re.search('^P',scene_item.si_model):
                    si['appearance']=u'配饰'
                elif re.search('^X',scene_item.si_model):
                    si['appearance']=u'足部防具'
                elif re.search('^M',scene_item.si_model):
                    si['appearance']=u'头部防具'
                elif re.search('^Y',scene_item.si_model):
                    si['appearance']=u'身体防具'
                else:
                    si['appearance']=u'其它'
                #物品位置坐标
                si['coordinate']=u'东西坐标：%.3f，南北坐标：%.3f，上下坐标：%.3f' % (scene_item.si_coor_x,scene_item.si_coor_z,scene_item.si_coor_y)
                #具体的物品，包括物品名称和数量
                si['details']=''
                #直接纯装备的类型
                if scene_item.si_ea_id:
                    ea_name=Equip.objects.get(id=scene_item.si_ea_id).ea_name
                    if scene_item.si_num!=1:
                        si['details']+=u'%s*%d、' % (ea_name,scene_item.si_num)
                    else:
                        si['details']+=u'%s、' % ea_name
                #直接纯物品的类型
                elif scene_item.si_pa_id:
                    pa_name=Property.objects.get(id=scene_item.si_pa_id).pa_name
                    if scene_item.si_num!=1:
                        si['details']+=u'%s*%d、' % (pa_name,scene_item.si_num)
                    else:
                        si['details']+=u'%s、' % pa_name
                #直接纯金钱
                elif scene_item.si_money:
                    si['details']+=u'%d文、' % scene_item.si_money
                #宝箱中藏有若干物品的情况，第一个物品一定是有的（不为0）
                if scene_item.si_item_1_id:
                    #解出第一个物品
                    if 3300>scene_item.si_item_1_id>=3000:
                        pa_name=Property.objects.get(id=scene_item.si_item_1_id).pa_name
                        if scene_item.si_item_1_num!=1:
                            si['details']+=u'%s*%d、' % (pa_name,scene_item.si_item_1_num)
                        else:
                            si['details']+=u'%s、' % pa_name
                    elif 3700>scene_item.si_item_1_id>=3501:
                        ea_name=Equip.objects.get(id=scene_item.si_item_1_id).ea_name
                        if scene_item.si_item_1_num!=1:
                            si['details']+=u'%s*%d、' % (ea_name,scene_item.si_item_1_num)
                        else:
                            si['details']+=u'%s、' % ea_name
                    #第二个
                    if 3300>scene_item.si_item_2_id>=3000:
                        pa_name=Property.objects.get(id=scene_item.si_item_2_id).pa_name
                        if scene_item.si_item_2_num!=1:
                            si['details']+=u'%s*%d、' % (pa_name,scene_item.si_item_2_num)
                        else:
                            si['details']+=u'%s、' % pa_name
                    elif 3700>scene_item.si_item_2_id>=3501:
                        ea_name=Equip.objects.get(id=scene_item.si_item_2_id).ea_name
                        if scene_item.si_item_2_num!=1:
                            si['details']+=u'%s*%d、' % (ea_name,scene_item.si_item_2_num)
                        else:
                            si['details']+=u'%s、' % ea_name
                    #第三个
                    if 3300>scene_item.si_item_3_id>=3000:
                        pa_name=Property.objects.get(id=scene_item.si_item_3_id).pa_name
                        if scene_item.si_item_3_num!=1:
                            si['details']+=u'%s*%d、' % (pa_name,scene_item.si_item_3_num)
                        else:
                            si['details']+=u'%s、' % pa_name
                    elif 3700>scene_item.si_item_3_id>=3501:
                        ea_name=Equip.objects.get(id=scene_item.si_item_3_id).ea_name
                        if scene_item.si_item_3_num!=1:
                            si['details']+=u'%s*%d、' % (ea_name,scene_item.si_item_3_num)
                        else:
                            si['details']+=u'%s、' % ea_name
                    #第四个
                    if 3300>scene_item.si_item_4_id>=3000:
                        pa_name=Property.objects.get(id=scene_item.si_item_4_id).pa_name
                        if scene_item.si_item_4_num!=1:
                            si['details']+=u'%s*%d、' % (pa_name,scene_item.si_item_4_num)
                        else:
                            si['details']+=u'%s、' % pa_name
                    elif 3700>scene_item.si_item_4_id>=3501:
                        ea_name=Equip.objects.get(id=scene_item.si_item_4_id).ea_name
                        if scene_item.si_item_4_num!=1:
                            si['details']+=u'%s*%d、' % (ea_name,scene_item.si_item_4_num)
                        else:
                            si['details']+=u'%s、' % ea_name
                    #第五个
                    if 3300>scene_item.si_item_5_id>=3000:
                        pa_name=Property.objects.get(id=scene_item.si_item_5_id).pa_name
                        if scene_item.si_item_5_num!=1:
                            si['details']+=u'%s*%d、' % (pa_name,scene_item.si_item_5_num)
                        else:
                            si['details']+=u'%s、' % pa_name
                    elif 3700>scene_item.si_item_5_id>=3501:
                        ea_name=Equip.objects.get(id=scene_item.si_item_5_id).ea_name
                        if scene_item.si_item_5_num!=1:
                            si['details']+=u'%s*%d、' % (ea_name,scene_item.si_item_5_num)
                        else:
                            si['details']+=u'%s、' % ea_name
                    #第六个
                    if 3300>scene_item.si_item_6_id>=3000:
                        pa_name=Property.objects.get(id=scene_item.si_item_6_id).pa_name
                        if scene_item.si_item_6_num!=1:
                            si['details']+=u'%s*%d、' % (pa_name,scene_item.si_item_6_num)
                        else:
                            si['details']+=u'%s、' % pa_name
                    elif 3700>scene_item.si_item_6_id>=3501:
                        ea_name=Equip.objects.get(id=scene_item.si_item_6_id).ea_name
                        if scene_item.si_item_6_num!=1:
                            si['details']+=u'%s*%d、' % (ea_name,scene_item.si_item_6_num)
                        else:
                            si['details']+=u'%s、' % ea_name
                    if scene_item.si_item_money:
                        si['details']+=u'%d文、' % scene_item.si_item_money
                si['details']=si['details'].rstrip(u'、')
                if not si['details']:
                    si['details']=u'空无一物'
                scene_item_list.append(si)

            self.template_name='db_ana/sceneitems.html'
            return render(request, self.template_name, {'scene_name': scene_name, 'scene_type': scene_type, 'scene_item_list': scene_item_list})

        return render(request, self.template_name, {'form': form})

