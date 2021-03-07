#coding=utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.views.generic.list import ListView
from django.db.models import Q

from .models import *
from .forms import *
from .views_extra import *
import logging, re

def item_shop_scene(item_id):
    shop_list=[]
    shops=Good.objects.filter(goods_id=item_id).values('shop_id','open_condition','open_num')
    for shop in shops:
        shop['position']=Shopproperty.objects.get(id=shop['shop_id']).position
        shop['scene']=Scenename.objects.get(scene=shop['position']).cn_name
        if int(shop['shop_id'][-2:])>36:
            shop['scene']+=u'（后期）'
        if shop['open_condition'] and shop['open_num']:
            shop['quest']=Mission.objects.get(trunk=shop['open_condition'],quest_id=shop['open_num']).name
            shop['scene']+=u'（%s）' % shop['quest']
        shop_list.append(shop['scene'])
    shops_string=u'、'.join(shop_list)
    shops_string=shops_string.rstrip(u'、')
    return shops_string
#首页
class IndexView(TemplateView):
    template_name = 'pal4/index.html'
#装备购买主页
class BuyEquipIndexView(TemplateView):
    template_name = 'pal4/buy_equip_index.html'

#装备购买详细页
class BuyEquipView(ListView):
    model = Equip
    eq_type_dic={
            'sword':'剑','dsword':'双剑','instrument':'琴',
            'helmet':'头部防具','corselet':'身体防具','legharness':'足部防具',
            'ornament':'佩戴'
    }
    template_name = 'pal4/buy_equip.html'

    def get_queryset(self):
        rl=['ept_tianhe_lv_lmt','ept_linsha_lv_lmt','ept_mengli_lv_lmt','ept_ziying_lv_lmt']
        attr_l=[{'ca_max_hp':'精上限'},{'ca_additional_rage':'气'},{'ca_max_mp':'神上限'},
                {'ca_physical':'武'},{'ca_toughness':'防'},{'ca_speed':'速'},{'ca_lucky':'运'},{'ca_will':'灵'},
                {'efe_water':'水'},{'efe_fire':'火'},{'efe_thunder':'雷'},{'efe_air':'风'},{'efe_earth':'土'},
                {'ca_attack_physical_additional':'物理伤害'},{'ca_attack_water_additional':'水伤害'},{'ca_attack_fire_additional':'火伤害'},{'ca_attack_thunder_additional':'雷伤害'},{'ca_attack_air_additional':'风伤害'},{'ca_attack_earth_additional':'土伤害'},
                {'ca_attack_physical_extract':'物理吸收'},{'ca_attack_water_extract':'水吸收'},{'ca_attack_fire_extract':'火吸收'},{'ca_attack_thunder_extract':'雷吸收'},{'ca_attack_air_extract':'风吸收'},{'ca_attack_earth_extract':'土吸收'},
                {'ca_attack_physical_react':'物理反弹'},{'ca_attack_water_react':'水反弹'},{'ca_attack_fire_react':'火反弹'},{'ca_attack_thunder_react':'雷反弹'},{'ca_attack_air_react':'风反弹'},{'ca_attack_earth_react':'土反弹'},
                {'ca_additional_critical':'暴击'},{'ca_fend_off':'格挡'},{'ca_additional_hitting':'命中'}
        ]
        equip_list=[]
        equips=Equip.objects.filter(ea_type__content=self.eq_type_dic[self.kwargs['equip_type']])
        for equip in equips:
            equip.name=equip.ea_name
            equip.price=equip.ea_price
            #获取适用角色
            if getattr(equip,rl[0]) and getattr(equip,rl[1]) and getattr(equip,rl[2]) and getattr(equip,rl[3]):
                equip.role_can_use=u'全体'
            elif getattr(equip,rl[0]) and getattr(equip,rl[3]):
                equip.role_can_use=u'男用'
            elif getattr(equip,rl[1]) and getattr(equip,rl[2]):
                equip.role_can_use=u'女用'
            elif getattr(equip,rl[0]):
                equip.role_can_use=u'天河'
            elif getattr(equip,rl[1]):
                equip.role_can_use=u'菱纱'
            elif getattr(equip,rl[2]):
                equip.role_can_use=u'梦璃'
            elif getattr(equip,rl[3]):
                equip.role_can_use=u'紫英'
            #获取要求等级
            equip.require_lv_lmt=max(getattr(equip,rl[i]) for i in range(4))
            #获取属性
            equip.attribute=''
            for attr in attr_l:
                for key in attr:
                    tmp=getattr(equip,key)
                    if tmp:
                        if tmp==int(tmp):
                            equip.attribute+='%s+%d ' % (attr[key],tmp)
                        else:
                            equip.attribute+='{0}+{1:.0%} '.format(attr[key],tmp)
            equip.attribute+='灵蕴:%d ' % equip.ea_ling_capacity + '潜力:%d' % equip.ea_forge_potential
            #获得购买场景字串
            equip.shopscene=item_shop_scene(equip.id)
            if not equip.shopscene:
                if self.eq_type_dic[self.kwargs['equip_type']]=='佩戴':
                    equip.shopscene=u'请注意支线任务'
                else:
                    equip.shopscene=u'参阅熔铸图谱自己铸造'
            equip_list.append(equip)
        return equip_list

    def get_context_data(self, **kwargs):
        context = super(BuyEquipView, self).get_context_data(**kwargs)
        context['equip_type']=self.eq_type_dic[self.kwargs['equip_type']]
        return context

#道具购买主页
class BuyPropertyIndexView(TemplateView):
    template_name = 'pal4/buy_property_index.html'

#道具购买详细页
class BuyPropertyView(ListView):
    model = Property
    prop_type_l=[
            {'cont':'恢复','mo_p':'DH','sub_tp':'一般恢复类'},
            {'cont':'恢复','mo_p':'SW','sub_tp':'食物'},
            {'cont':'攻击','mo_p':'DG','sub_tp':'攻击类'},
            {'cont':'辅助','mo_p':'DF','sub_tp':'一般辅助类'},
            {'cont':'辅助','mo_p':'CX','sub_tp':'香料'},
            {'cont':'材料','mo_p':'CK','sub_tp':'矿石'},
            {'cont':'材料','mo_p':'CQ','sub_tp':'其它'}
    ]
    template_name = 'pal4/buy_property.html'

    def get_queryset(self):
        prop_list=[]
        for prop_type in self.prop_type_l:
            if prop_type['mo_p'].lower()==self.kwargs['pr_type']:
                break
        #恢复类的获取
        if prop_type['cont']=='恢复':
            propertys=Property.objects.filter(pa_type__content=prop_type['cont'],pa_model__startswith=prop_type['mo_p'])
        #攻击类
        if prop_type['cont']=='攻击':
            propertys=Property.objects.filter(pa_type__content=prop_type['cont'])
        #辅助类的获取
        if prop_type['cont']=='辅助':
            if prop_type['mo_p']=='CX':
                propertys=Property.objects.filter(pa_type__content=prop_type['cont'],pa_model__startswith=prop_type['mo_p'])
            elif prop_type['mo_p']=='DF':
                propertys=Property.objects.filter(pa_type__content=prop_type['cont']).exclude(pa_model__startswith='CX')
        #材料类的获取
        if prop_type['cont']=='材料':
            if prop_type['mo_p']=='CK':
                propertys=Property.objects.filter(pa_type__content=prop_type['cont'],pa_model__startswith=prop_type['mo_p'],pa_property='熔铸、锻冶的材料')
            elif prop_type['mo_p']=='CQ':
                propertys=Property.objects.filter(pa_type__content=prop_type['cont'],pa_model__startswith=prop_type['mo_p'])
        for prop in propertys:
            #获得购买场景字串
            prop.shopscene=item_shop_scene(prop.id)
            #logging.DEBUG('type of prop: ',type(prop))
            if not prop.shopscene:
                #logging.DEBUG('type of prop.pa_type: ', type(prop.pa_type))
                """if prop.pa_type.content==u'攻击':
                    prop.shopscene='无法买到'
                elif prop.pa_type.content==u'辅助' and prop.pa_model.startswith('JQ'):
                    prop.shopscene='剧情获得'"""
                #使用prop.pa_type来区分买不到的情况总是出错，暂时改用
                if prop.pa_model.startswith('JQ'):
                    prop.shopscene='剧情获得'
                else:
                    prop.shopscene='无法买到'
            prop_list.append(prop)
        return prop_list

    def get_context_data(self, **kwargs):
        for prop_type in self.prop_type_l:
            if prop_type['mo_p'].lower()==self.kwargs['pr_type']:
                break
        context = super(BuyPropertyView, self).get_context_data(**kwargs)
        context['p_type']=prop_type['cont']
        context['sub_type']=prop_type['sub_tp']
        return context

#配方购买主页
class BuyPrescriptionIndexView(TemplateView):
    template_name = 'pal4/buy_prescription_index.html'

#配方购买详细页
class BuyPrescriptionView(ListView):
    model = Prescription
    pre_type_l=[
            {'pre_cont':'熔铸图谱','pre_flag':'_wt','sub_tp':'剑','eq_url_key':'sword'},
            {'pre_cont':'熔铸图谱','pre_flag':'_wl','sub_tp':'双剑','eq_url_key':'dsword'},
            {'pre_cont':'熔铸图谱','pre_flag':'_wm','sub_tp':'琴','eq_url_key':'instrument'},
            {'pre_cont':'熔铸图谱','pre_flag':'_m','sub_tp':'头部防具','eq_url_key':'helmet'},
            {'pre_cont':'熔铸图谱','pre_flag':'_y','sub_tp':'身体防具','eq_url_key':'corselet'},
            {'pre_cont':'熔铸图谱','pre_flag':'_x','sub_tp':'足部防具','eq_url_key':'legharness'},
            {'pre_cont':'锻造图谱','pre_flag':'02','sub_tp':'锻冶'},
            {'pre_cont':'注灵图谱','pre_flag':'03','sub_tp':'注灵'}
    ]
    template_name = 'pal4/buy_prescription.html'

    def get_queryset(self):
        prescription_list=[]
        #先分析URL链接中的配方标志，确认配方类型的细节
        for pre_type in self.pre_type_l:
            if self.kwargs['pre_type'].endswith(pre_type['pre_flag']):
                break
        #如果存在子类型，说明是熔铸图谱
        if 'eq_url_key' in pre_type:
            #先把装备的ID找出来，然后依据ID找相应配方
            eq_ids=Equip.objects.filter(ea_type__content=pre_type['sub_tp']).values('id')
            prescriptions=Prescription.objects.filter(type__content=pre_type['pre_cont'],pra_product_id__in=eq_ids)
        else:
            prescriptions=Prescription.objects.filter(type__content=pre_type['pre_cont'])
        for prescription in prescriptions:
            #获得购买场景字串
            prescription.shopscene=item_shop_scene(prescription.id)
            #logging.DEBUG('type of prescription: ',type(prescription))
            if not prescription.shopscene:
                prescription.shopscene='请注意支线剧情'
            prescription_list.append(prescription)
        return prescription_list

    def get_context_data(self, **kwargs):
        for pre_type in self.pre_type_l:
            if self.kwargs['pre_type'].endswith(pre_type['pre_flag']):
                break
        context = super(BuyPrescriptionView, self).get_context_data(**kwargs)
        context['pre_type']=pre_type['pre_cont']
        context['sub_type']=pre_type['sub_tp']
        if 'eq_url_key' in pre_type:
            context['eq_url_key']=pre_type['eq_url_key']
        return context

#怪物信息首页
class MonsterIndexView(TemplateView):
    template_name = 'pal4/monster_index.html'

#怪物信息汇总表
class MonsterSumView(ListView):
    model = Monster
    template_name='pal4/monster_sum.html'

    def get_queryset(self):
        #获得怪物的全部信息，结构比较大，但没办法，好在记录数不多
        monster_list=[]
        monsters=Monster.objects.all().order_by('ca_level')
        for monster in monsters:
            #ID和名称直接用库中现成的，所以略过，种族名称通过race外键获得
            monster.racename=monster.race.content
            #等级、经验、精也直接用现成的，五灵属性比较复杂，由以下分析获得
            monster.wuling=''
            wls=[{'efe_water':'水'},{'efe_fire':'火'},{'efe_thunder':'雷'},{'efe_air':'风'},{'efe_earth':'土'}]
            for wl in wls:
                for attr in wl:
                    if getattr(monster,attr):
                        monster.wuling+='%s、' % wl[attr]
            if not monster.wuling:
                monster.wuling='无'
            monster.wuling=monster.wuling.rstrip('、')+'属性'
            #然后是特殊属性，分为两部分，一部分是抗性分析，另一部分是反弹分析
            monster.spe_p=''
            #先看抗性
            if monster.ca_attack_physical_extract==1:
                monster.spe_p+='物理免疫； '
            ma_ex=''
            wl_exs=[{'ca_attack_water_extract':'水'},{'ca_attack_fire_extract':'火'},{'ca_attack_thunder_extract':'雷'},{'ca_attack_air_extract':'风'},{'ca_attack_earth_extract':'土'}]
            for wl_ex in wl_exs:
                for attr in wl_ex:
                    if getattr(monster,attr)==1:
                        ma_ex+='%s免疫、' % wl_ex[attr]
                    elif getattr(monster,attr)>1:
                        ma_ex+='%s吸收、' % wl_ex[attr]
            ma_ex=ma_ex.rstrip('、')
            if ma_ex.count('免疫')==5:
                ma_ex='仙术免疫'
            elif ma_ex.count('吸收')==5:
                ma_ex='仙术吸收'
            if ma_ex: monster.spe_p+=ma_ex+'； '
            #再看反弹
            if monster.ca_attack_physical_react>0:
                monster.spe_p+='物理反弹； '
            ma_ra=''
            wl_ras=[{'ca_attack_water_react':'水'},{'ca_attack_fire_react':'火'},{'ca_attack_thunder_react':'雷'},{'ca_attack_air_react':'风'},{'ca_attack_earth_react':'土'}]
            for wl_ra in wl_ras:
                for attr in wl_ra:
                    if getattr(monster,attr)>0:
                        ma_ra+='%s反弹、' % wl_ra[attr]
            ma_ra=ma_ra.rstrip('、')
            if ma_ra.count('反弹')==5:
                ma_ra='仙术反弹'
            monster.spe_p+=ma_ra
            monster.spe_p=monster.spe_p.rstrip('； ')
            #接下来是技能部分
            monster.skills=''
            for i in range(1,7):
                skill_id=getattr(monster,'monster_magic_'+str(i))
                if skill_id:
                    try:
                        skill_name=Magic.objects.get(id=skill_id).name
                    except:
                        skill_name=Stunt.objects.get(id=skill_id).name
                    finally:
                        monster.skills+=u'%s、' % skill_name
            monster.skills=monster.skills.rstrip(u'、')
            #可偷物品名称
            monster.losable_prop_name=''
            if monster.ca_losable_property:
                monster.losable_prop_name=Property.objects.get(id=monster.ca_losable_property).pa_name
            #可能掉落的物品名称，由于有可能重复，因此先用一个集合表示不重复的物品
            monster.drop_prop=''
            prop_set=set()
            for i in range(1,5):
                prop_id=getattr(monster,'mdt_%d_id' % i)
                if prop_id:
                    prop_set.add(prop_id)
            for prop_id in prop_set:
                prop_name=Property.objects.get(id=prop_id).pa_name
                monster.drop_prop+=prop_name+u'、'
            monster.drop_prop=monster.drop_prop.rstrip(u'、')
            #组合出掉落金钱的情况
            monster.drop_money='%d~%d' % (monster.ma_min_drop_money,monster.ma_max_drop_money)
            monster_list.append(monster)
        return monster_list

#以下几个敌人信息视图为明细表
#一、偷窃敌人及击败敌人的掉落详情
class MonsterStolenDropView(ListView):
    model = Monster
    template_name='pal4/monster_stolen_drop.html'

    def get_queryset(self):
        monster_list=[]
        monsters=Monster.objects.all().order_by('ca_level')
        for monster in monsters:
            #可偷窃物品名称
            monster.losable_prop_name='---'
            if monster.ca_losable_property:
                monster.losable_prop_name=Property.objects.get(id=monster.ca_losable_property).pa_name
            #可能掉落的物品信息
            for i in range(1,5):
                prop_id=getattr(monster,'mdt_%d_id' % i)
                if prop_id:
                    tmp_prop=Property.objects.get(id=prop_id).pa_name
                    setattr(monster,'mdt_%d' % i,tmp_prop)
                    tmp_prob='{0:.2%}'.format(getattr(monster,'mdt_%d_rate' % i))
                    setattr(monster,'mdt_%d_rate_p' % i,tmp_prob)
                else:
                    setattr(monster,'mdt_%d' % i,'---')
                    setattr(monster,'mdt_%d_rate_p' % i,'---')
            monster_list.append(monster)
        return monster_list

#敌人技能及额外属性追加
class MonsterSkillExtraPView(ListView):
    model = Monster
    template_name='pal4/monster_skill_extra_p.html'

    def get_queryset(self):
        monster_list=[]
        monsters=Monster.objects.all().order_by('ca_level')
        for monster in monsters:
            #技能部分
            for i in range(1,7):
                skill_id=getattr(monster,'monster_magic_%d' % i)
                if skill_id:
                    try:
                        magic_name=Magic.objects.get(id=skill_id).name
                        magic_info=u'仙术ID：%d、仙术名称：%s' % (skill_id,magic_name)
                        setattr(monster,'ma_skill_%d' % i,magic_info)
                    except:
                        stunt_name=Stunt.objects.get(id=skill_id).name
                        stunt_info=u'特技ID：%d、特技名称：%s' % (skill_id,stunt_name)
                        setattr(monster,'ma_skill_%d' % i,stunt_info)
                else:
                    setattr(monster,'ma_skill_%d' % i,'-----')
            #属性追加部分
            for p in ['additional_critical','fend_off','additional_hitting','counterpunch_rate']:
                pd_p='{0:.0%}'.format(getattr(monster,'ca_%s' % p))
                if pd_p:
                    setattr(monster,'ca_%s_p' % p,pd_p)
                else:
                    setattr(monster,'ca_%s_p' % p,0)
            monster_list.append(monster)
        return monster_list

#抗性及反弹百分比
class MonsterResistReboundView(ListView):
    model = Monster
    template_name='pal4/monster_resist_rebound.html'

    def get_queryset(self):
        monster_list=[]
        monsters=Monster.objects.all().order_by('ca_level')
        for monster in monsters:
            #一个双重循环全面解决
            for tp1 in ['physical','water','fire','thunder','air','earth']:
                for tp2 in ['extract','react']:
                    tmp_r=getattr(monster,'ca_attack_%s_%s' % (tp1,tp2))
                    if tmp_r:
                        tmp_rp='{0:.0%}'.format(tmp_r)
                        setattr(monster,'ca_attack_%s_%s_p' %(tp1,tp2),tmp_rp)
                    else:
                        setattr(monster,'ca_attack_%s_%s_p' %(tp1,tp2),0)

            monster_list.append(monster)
        return monster_list

#五基本属性及五灵属性
class MonsterFPWulingView(ListView):
    model = Monster
    template_name='pal4/monster_fp_wuling.html'

    def get_queryset(self):
        monsters=Monster.objects.all().order_by('ca_level')
        return monsters

#怪物基本信息
class MonsterBasicView(ListView):
    model = Monster
    template_name='pal4/monster_basic.html'

    def get_queryset(self):
        #获得怪物的全部信息，结构比较大，但没办法，好在记录数不多
        monster_list=[]
        monsters=Monster.objects.all().order_by('ca_level')
        for monster in monsters:
            #前四项直接使用，种族名称通过race外键获得
            monster.racename=monster.race.content
            monster.is_boss_cn='是' if monster.is_boss.content=='TRUE' else '否'
            monster.phy_atk_tgt= monster.physical_atk_targett.content
            monster.phy_atk_range= monster.physical_atk_range.content
            monster.is_count='是' if monster.count==1 else '否'
            monster_list.append(monster)
        return monster_list

#全任务列表
class MissionView(ListView):
    model = Mission
    template_name='pal4/mission.html'

    def get_queryset(self):
        mission_list=[]
        missions=Mission.objects.all()
        for mission in missions:
            if mission.depended_id<200:
                mission.type='主线'
                mission.color='red'
            elif 300>mission.depended_id>=200:
                mission.type='委托'
                mission.color='green'
            else:
                mission.type='支线'
                mission.color='blue'
            mission.story_percent='{0:.2%}'.format(mission.story_per/100)
            mission.is_gray='是' if mission.story_show==1 else '否'
            mission_list.append(mission)
        return mission_list

#五灵仙术一览
class MagicView(ListView):
    model = Magic
    template_name='pal4/magic.html'

    def get_queryset(self):
        magic_list=[]
        magics=Magic.objects.all()
        for magic in magics:
            #指令类型的名称
            magic.ai_cmd_name=magic.ai_cmd_type.content
            #目标名称
            magic.target_name=magic.target.content
            magic.wl_name=magic.felements.content
            if magic.wl_name==u'水':
                magic.color='blue'
            elif magic.wl_name==u'火':
                magic.color='red'
            elif magic.wl_name==u'雷':
                magic.color='purple'
            elif magic.wl_name==u'风':
                magic.color='green'
            elif magic.wl_name==u'土':
                magic.color='chocolate'
            if magic.prop:
                magic.bgcolor='chartreuse'
            else:
                magic.bgcolor='turquoise'
            magic.act_name=magic.acttype.content
            magic_list.append(magic)
        return magic_list













