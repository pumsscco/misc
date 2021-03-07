#coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

#攻击动作类型
class Acttype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActType'

#AI指令类型
class Aicommandtype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AiCommandType'

#AI配置类型
class Aiconfig(models.Model):
    ai_type = models.ForeignKey('Aitype', db_column='AI_TYPE', primary_key=True)  # Field name made lowercase.
    aca_self_in_danger = models.FloatField(db_column='ACA_SELF_IN_DANGER', blank=True, null=True)  # Field name made lowercase.
    aca_min_self_hp = models.FloatField(db_column='ACA_MIN_SELF_HP', blank=True, null=True)  # Field name made lowercase.
    aca_max_self_hp = models.FloatField(db_column='ACA_MAX_SELF_HP', blank=True, null=True)  # Field name made lowercase.
    aca_mate_in_danger = models.FloatField(db_column='ACA_MATE_IN_DANGER', blank=True, null=True)  # Field name made lowercase.
    aca_mate_dead = models.FloatField(db_column='ACA_MATE_DEAD', blank=True, null=True)  # Field name made lowercase.
    aca_min_mate_hp = models.FloatField(db_column='ACA_MIN_MATE_HP', blank=True, null=True)  # Field name made lowercase.
    aca_max_mate_hp = models.FloatField(db_column='ACA_MAX_MATE_HP', blank=True, null=True)  # Field name made lowercase.
    aca_enemy_dead = models.FloatField(db_column='ACA_ENEMY_DEAD', blank=True, null=True)  # Field name made lowercase.
    aca_enemy_in_danger = models.FloatField(db_column='ACA_ENEMY_IN_DANGER', blank=True, null=True)  # Field name made lowercase.
    aca_min_enemy_hp = models.FloatField(db_column='ACA_MIN_ENEMY_HP', blank=True, null=True)  # Field name made lowercase.
    aca_max_enemy_hp = models.FloatField(db_column='ACA_MAX_ENEMY_HP', blank=True, null=True)  # Field name made lowercase.
    aca_bout_count = models.FloatField(db_column='ACA_BOUT_COUNT', blank=True, null=True)  # Field name made lowercase.
    aca_bout_times = models.FloatField(db_column='ACA_BOUT_TIMES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AiConfig'

#AI属性明细
class Aiproperty(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ai_type = models.ForeignKey('Aitype', db_column='AI_TYPE', blank=True, null=True)  # Field name made lowercase.
    team_state = models.ForeignKey('Teamstate', db_column='TEAM_STATE', blank=True, null=True)  # Field name made lowercase.
    enemy_state = models.ForeignKey('Enemystate', db_column='ENEMY_STATE', blank=True, null=True)  # Field name made lowercase.
    apa_cure_rate = models.FloatField(db_column='APA_CURE_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_special_atk_rate = models.FloatField(db_column='APA_SPECIAL_ATK_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_other_rate = models.FloatField(db_column='APA_OTHER_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_normal_atk_rate = models.FloatField(db_column='APA_NORMAL_ATK_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_flee_rate = models.FloatField(db_column='APA_FLEE_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_assign_skill = models.FloatField(db_column='APA_ASSIGN_SKILL', blank=True, null=True)  # Field name made lowercase.
    apa_skill_rate = models.FloatField(db_column='APA_SKILL_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_summon_rate = models.FloatField(db_column='APA_SUMMON_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_revive_rate = models.FloatField(db_column='APA_REVIVE_RATE', blank=True, null=True)  # Field name made lowercase.
    apa_assign_target = models.FloatField(db_column='APA_ASSIGN_TARGET', blank=True, null=True)  # Field name made lowercase.
    apa_for_assign_target = models.FloatField(db_column='APA_FOR_ASSIGN_TARGET', blank=True, null=True)  # Field name made lowercase.
    apa_for_the_dangerous = models.FloatField(db_column='APA_FOR_THE_DANGEROUS', blank=True, null=True)  # Field name made lowercase.
    apa_for_random = models.FloatField(db_column='APA_FOR_RANDOM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AiProperty'

#AI类型
class Aitype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AiType'

#布尔类型，用于表示是或否
class Bool(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOOL'

#战斗计算参数
class Combatformulaconfig(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CombatFormulaConfig'

#战斗评级计算参数，给出了影响特，一，二，三，四等战斗的因素的给分情况
class Combatprize(models.Model):
    key = models.IntegerField(db_column='KEY', primary_key=True)  # Field name made lowercase.
    est_protect = models.IntegerField(db_column='EST_PROTECT', blank=True, null=True)  # Field name made lowercase.
    est_joint_atk = models.IntegerField(db_column='EST_JOINT_ATK', blank=True, null=True)  # Field name made lowercase.
    est_critical = models.IntegerField(db_column='EST_CRITICAL', blank=True, null=True)  # Field name made lowercase.
    est_missed = models.IntegerField(db_column='EST_MISSED', blank=True, null=True)  # Field name made lowercase.
    est_fend_off = models.IntegerField(db_column='EST_FEND_OFF', blank=True, null=True)  # Field name made lowercase.
    est_react_atk = models.IntegerField(db_column='EST_REACT_ATK', blank=True, null=True)  # Field name made lowercase.
    est_cast_magic = models.IntegerField(db_column='EST_CAST_MAGIC', blank=True, null=True)  # Field name made lowercase.
    est_stunt = models.IntegerField(db_column='EST_STUNT', blank=True, null=True)  # Field name made lowercase.
    est_use_property = models.IntegerField(db_column='EST_USE_PROPERTY', blank=True, null=True)  # Field name made lowercase.
    est_revive = models.IntegerField(db_column='EST_REVIVE', blank=True, null=True)  # Field name made lowercase.
    est_flee_fail = models.IntegerField(db_column='EST_FLEE_FAIL', blank=True, null=True)  # Field name made lowercase.
    est_role_dead = models.IntegerField(db_column='EST_ROLE_DEAD', blank=True, null=True)  # Field name made lowercase.
    est_unattacked = models.IntegerField(db_column='EST_UNATTACKED', blank=True, null=True)  # Field name made lowercase.
    est_hp_in_max = models.IntegerField(db_column='EST_HP_IN_MAX', blank=True, null=True)  # Field name made lowercase.
    est_hp_in_danger = models.IntegerField(db_column='EST_HP_IN_DANGER', blank=True, null=True)  # Field name made lowercase.
    est_take_action = models.IntegerField(db_column='EST_TAKE_ACTION', blank=True, null=True)  # Field name made lowercase.
    est_monster_didnt_act = models.IntegerField(db_column='EST_MONSTER_DIDNT_ACT', blank=True, null=True)  # Field name made lowercase.
    est_monster_flee = models.IntegerField(db_column='EST_MONSTER_FLEE', blank=True, null=True)  # Field name made lowercase.
    est_monster_dead = models.IntegerField(db_column='EST_MONSTER_DEAD', blank=True, null=True)  # Field name made lowercase.
    est_level_upper = models.IntegerField(db_column='EST_LEVEL_UPPER', blank=True, null=True)  # Field name made lowercase.
    est_level_lower = models.IntegerField(db_column='EST_LEVEL_LOWER', blank=True, null=True)  # Field name made lowercase.
    est_physical_atk = models.IntegerField(db_column='EST_PHYSICAL_ATK', blank=True, null=True)  # Field name made lowercase.
    est_knock_out = models.IntegerField(db_column='EST_KNOCK_OUT', blank=True, null=True)  # Field name made lowercase.
    est_win_at_the_first_bout = models.IntegerField(db_column='EST_WIN_AT_THE_FIRST_BOUT', blank=True, null=True)  # Field name made lowercase.
    est_ko_by_one_role = models.IntegerField(db_column='EST_KO_BY_ONE_ROLE', blank=True, null=True)  # Field name made lowercase.
    est_all_survive = models.IntegerField(db_column='EST_ALL_SURVIVE', blank=True, null=True)  # Field name made lowercase.
    base = models.IntegerField(db_column='BASE', blank=True, null=True)  # Field name made lowercase.
    prize_s = models.IntegerField(db_column='PRIZE_S', blank=True, null=True)  # Field name made lowercase.
    prize_1 = models.IntegerField(db_column='PRIZE_1', blank=True, null=True)  # Field name made lowercase.
    prize_2 = models.IntegerField(db_column='PRIZE_2', blank=True, null=True)  # Field name made lowercase.
    prize_3 = models.IntegerField(db_column='PRIZE_3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CombatPrize'

#战斗场景
class Combatscene(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    world = models.TextField(db_column='WORLD', blank=True, null=True)  # Field name made lowercase.
    floor = models.IntegerField(db_column='FLOOR', blank=True, null=True)  # Field name made lowercase.
    combat_scene = models.TextField(db_column='COMBAT_SCENE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CombatScene'

#战斗中用到的字符串的中英文对照翻译
class Combattranslation(models.Model):
    english = models.CharField(db_column='English', primary_key=True, max_length=100)  # Field name made lowercase.
    translation = models.TextField(db_column='Translation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CombatTranslation'

#战斗评分随机奖励道具表
class Dropproperty(models.Model):
    item_id = models.IntegerField(db_column='ITEM_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DropProperty'

#敌人状态
class Enemystate(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EnemyState'

#装备，包括了所有武器，防具，配饰在内
class Equip(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ea_type = models.ForeignKey('Equiptype', db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    ea_name = models.TextField(db_column='EA_NAME', blank=True, null=True)  # Field name made lowercase.
    ea_description = models.TextField(db_column='EA_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    ea_ling_info = models.TextField(db_column='EA_LING_INFO', blank=True, null=True)  # Field name made lowercase.
    ea_ling_name = models.TextField(db_column='EA_LING_NAME', blank=True, null=True)  # Field name made lowercase.
    ea_icon = models.TextField(db_column='EA_ICON', blank=True, null=True)  # Field name made lowercase.
    ea_model = models.TextField(db_column='EA_MODEL', blank=True, null=True)  # Field name made lowercase.
    ea_texture = models.TextField(db_column='EA_TEXTURE', blank=True, null=True)  # Field name made lowercase.
    ea_lhand = models.TextField(db_column='EA_LHAND', blank=True, null=True)  # Field name made lowercase.
    ea_rhand = models.TextField(db_column='EA_RHAND', blank=True, null=True)  # Field name made lowercase.
    ept_tianhe_lv_lmt = models.IntegerField(db_column='ePT_TIANHE_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    ept_linsha_lv_lmt = models.IntegerField(db_column='ePT_LINSHA_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    ept_mengli_lv_lmt = models.IntegerField(db_column='ePT_MENGLI_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    ept_ziying_lv_lmt = models.IntegerField(db_column='ePT_ZIYING_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    ea_attached_effect = models.TextField(db_column='EA_ATTACHED_EFFECT', blank=True, null=True)  # Field name made lowercase.
    ea_price = models.IntegerField(db_column='EA_PRICE', blank=True, null=True)  # Field name made lowercase.
    ea_ling_capacity = models.IntegerField(db_column='EA_LING_CAPACITY', blank=True, null=True)  # Field name made lowercase.
    ea_skill_id = models.IntegerField(db_column='EA_SKILL_ID', blank=True, null=True)  # Field name made lowercase.
    ea_forge_potential = models.IntegerField(db_column='EA_FORGE_POTENTIAL', blank=True, null=True)  # Field name made lowercase.
    ca_max_hp = models.IntegerField(db_column='CA_MAX_HP', blank=True, null=True)  # Field name made lowercase.
    ca_additional_rage = models.IntegerField(db_column='CA_ADDITIONAL_RAGE', blank=True, null=True)  # Field name made lowercase.
    ca_max_mp = models.IntegerField(db_column='CA_MAX_MP', blank=True, null=True)  # Field name made lowercase.
    ca_physical = models.IntegerField(db_column='CA_PHYSICAL', blank=True, null=True)  # Field name made lowercase.
    ca_toughness = models.IntegerField(db_column='CA_TOUGHNESS', blank=True, null=True)  # Field name made lowercase.
    ca_speed = models.IntegerField(db_column='CA_SPEED', blank=True, null=True)  # Field name made lowercase.
    ca_lucky = models.IntegerField(db_column='CA_LUCKY', blank=True, null=True)  # Field name made lowercase.
    ca_will = models.IntegerField(db_column='CA_WILL', blank=True, null=True)  # Field name made lowercase.
    efe_water = models.IntegerField(db_column='EFE_WATER', blank=True, null=True)  # Field name made lowercase.
    efe_fire = models.IntegerField(db_column='EFE_FIRE', blank=True, null=True)  # Field name made lowercase.
    efe_thunder = models.IntegerField(db_column='EFE_THUNDER', blank=True, null=True)  # Field name made lowercase.
    efe_air = models.IntegerField(db_column='EFE_AIR', blank=True, null=True)  # Field name made lowercase.
    efe_earth = models.IntegerField(db_column='EFE_EARTH', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_additional = models.IntegerField(db_column='CA_ATTACK_PHYSICAL_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_additional = models.IntegerField(db_column='CA_ATTACK_WATER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_additional = models.IntegerField(db_column='CA_ATTACK_FIRE_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_additional = models.IntegerField(db_column='CA_ATTACK_THUNDER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_additional = models.IntegerField(db_column='CA_ATTACK_AIR_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_additional = models.IntegerField(db_column='CA_ATTACK_EARTH_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_extract = models.FloatField(db_column='CA_ATTACK_PHYSICAL_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_extract = models.FloatField(db_column='CA_ATTACK_WATER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_extract = models.FloatField(db_column='CA_ATTACK_FIRE_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_extract = models.FloatField(db_column='CA_ATTACK_THUNDER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_extract = models.FloatField(db_column='CA_ATTACK_AIR_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_extract = models.FloatField(db_column='CA_ATTACK_EARTH_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_react = models.FloatField(db_column='CA_ATTACK_PHYSICAL_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_react = models.FloatField(db_column='CA_ATTACK_WATER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_react = models.FloatField(db_column='CA_ATTACK_FIRE_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_react = models.FloatField(db_column='CA_ATTACK_THUNDER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_react = models.FloatField(db_column='CA_ATTACK_AIR_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_react = models.FloatField(db_column='CA_ATTACK_EARTH_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_additional_critical = models.FloatField(db_column='CA_ADDITIONAL_CRITICAL', blank=True, null=True)  # Field name made lowercase.
    ca_fend_off = models.FloatField(db_column='CA_FEND_OFF', blank=True, null=True)  # Field name made lowercase.
    ca_additional_hitting = models.FloatField(db_column='CA_ADDITIONAL_HITTING', blank=True, null=True)  # Field name made lowercase.
    ca_pay_for_spare = models.FloatField(db_column='CA_PAY_FOR_SPARE', blank=True, null=True)  # Field name made lowercase.
    ea_ef1 = models.TextField(db_column='EA_EF1', blank=True, null=True)  # Field name made lowercase.
    ea_ef2 = models.TextField(db_column='EA_EF2', blank=True, null=True)  # Field name made lowercase.
    ea_ef3 = models.TextField(db_column='EA_EF3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Equip'
    def __unicode__(self):
        return "装备ID: %d, 装备名称: %s" % (self.id,self.ea_name)

#装备大类，包括武器，头部，身体，足部，配饰
class Equipclass(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipClass'

#装备关系表
class Equiprelation(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    class_field = models.IntegerField(db_column='CLASS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipRelation'

#装备种类，主要是分出武器中的子项
class Equiptype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipType'

#仙剑问答，全答对有不错的道具奖励
class Gamequestion(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    question = models.TextField(db_column='QUESTION', blank=True, null=True)  # Field name made lowercase.
    answer_1 = models.TextField(db_column='ANSWER_1', blank=True, null=True)  # Field name made lowercase.
    answer_2 = models.TextField(db_column='ANSWER_2', blank=True, null=True)  # Field name made lowercase.
    answer_3 = models.TextField(db_column='ANSWER_3', blank=True, null=True)  # Field name made lowercase.
    right_answer = models.IntegerField(db_column='RIGHT_ANSWER', blank=True, null=True)  # Field name made lowercase.
    window = models.IntegerField(db_column='WINDOW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameQuestion'

#游戏中会出现的字符串
class Gamestring(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    string = models.TextField(db_column='STRING', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GameString'

#全部商店中出现商品的对应表，包括了开放条件在内，与Mission表中的相关内容对应
class Good(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shop_id = models.TextField(db_column='SHOP_ID', blank=True, null=True)  # Field name made lowercase.
    goods_id = models.IntegerField(db_column='GOODS_ID', blank=True, null=True)  # Field name made lowercase.
    goods_type = models.ForeignKey('Goodstype', db_column='GOODS_TYPE', blank=True, null=True)  # Field name made lowercase.
    open_condition = models.IntegerField(db_column='OPEN_CONDITION', blank=True, null=True)  # Field name made lowercase.
    open_num = models.IntegerField(db_column='OPEN_NUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Good'

    def __unicode__(self):
	return "店铺ID: %s, 物品ID: %d" % (self.shop_id,self.goods_id)

#货物种类
class Goodstype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsType'

    def __unicode__(self):
	return "商品类型ID: %d, 商品类型名称: %s" % (self.id,self.content)

#帮助提示
class Helptips(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    window = models.IntegerField(db_column='WINDOW', blank=True, null=True)  # Field name made lowercase.
    class_field = models.TextField(db_column='CLASS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    tips = models.TextField(db_column='TIPS', blank=True, null=True)  # Field name made lowercase.
    quest_id = models.IntegerField(db_column='QUEST_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HelpTips'

#介绍
class Introduction(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    introduction = models.TextField(db_column='INTRODUCTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Introduction'

#五灵仙术
class Magic(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    prop = models.TextField(db_column='PROP', blank=True, null=True)  # Field name made lowercase.
    ai_cmd_type = models.ForeignKey(Aicommandtype, db_column='AI_CMD_TYPE', blank=True, null=True)  # Field name made lowercase.
    target = models.ForeignKey('Skilltarget', db_column='TARGET', blank=True, null=True)  # Field name made lowercase.
    felements = models.ForeignKey('Wuling', db_column='FELEMENTS', blank=True, null=True)  # Field name made lowercase.
    need_total_used_point = models.IntegerField(db_column='NEED_TOTAL_USED_POINT', blank=True, null=True)  # Field name made lowercase.
    need_point = models.IntegerField(db_column='NEED_POINT', blank=True, null=True)  # Field name made lowercase.
    parent_magic = models.IntegerField(db_column='PARENT_MAGIC', blank=True, null=True)  # Field name made lowercase.
    attached_skill = models.IntegerField(db_column='ATTACHED_SKILL', blank=True, null=True)  # Field name made lowercase.
    consumed_mp = models.IntegerField(db_column='CONSUMED_MP', blank=True, null=True)  # Field name made lowercase.
    acttype = models.ForeignKey(Acttype, db_column='ACTTYPE', blank=True, null=True)  # Field name made lowercase.
    hit_extra = models.FloatField(db_column='HIT_EXTRA', blank=True, null=True)  # Field name made lowercase.
    animation = models.TextField(db_column='ANIMATION', blank=True, null=True)  # Field name made lowercase.
    effect = models.TextField(db_column='EFFECT', blank=True, null=True)  # Field name made lowercase.
    target_ef = models.TextField(db_column='TARGET_EF', blank=True, null=True)  # Field name made lowercase.
    target_bind = models.TextField(db_column='TARGET_BIND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Magic'

#地图信息，这张表完全看不出有什么用！
class Mapinfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    string_id = models.IntegerField(db_column='STRING_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MapInfo'

#任务，包括主线和支线
class Mission(models.Model):
    depended_id = models.IntegerField(db_column='DEPENDED_ID', primary_key=True)  # Field name made lowercase.
    trunk = models.IntegerField(db_column='TRUNK', blank=True, null=True)  # Field name made lowercase.
    quest_id = models.IntegerField(db_column='QUEST_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='PICTURE', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    story_per = models.FloatField(db_column='STORY_PER', blank=True, null=True)  # Field name made lowercase.
    story_show = models.IntegerField(db_column='STORY_SHOW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mission'

    def __unicode__(self):
        return "任务变量: %d, 任务编号: %d, 任务名称: %s, 剧情完成度: %f" % (self.trunk,self.quest_id,self.name,self.story_per)

#怪物，准确说是敌人的详细信息
class Monster(models.Model):
    monster_id = models.IntegerField(db_column='MONSTER_ID', primary_key=True)  # Field name made lowercase.
    ma_name = models.TextField(db_column='MA_NAME', blank=True, null=True)  # Field name made lowercase.
    ma_icon = models.TextField(db_column='MA_ICON', blank=True, null=True)  # Field name made lowercase.
    ma_model = models.TextField(db_column='MA_MODEL', blank=True, null=True)  # Field name made lowercase.
    ma_texture = models.TextField(db_column='MA_TEXTURE', blank=True, null=True)  # Field name made lowercase.
    ma_desc = models.TextField(db_column='MA_DESC', blank=True, null=True)  # Field name made lowercase.
    race = models.ForeignKey('Race', db_column='RACE', blank=True, null=True)  # Field name made lowercase.
    is_boss = models.ForeignKey(Bool, db_column='IS_BOSS', blank=True, null=True)  # Field name made lowercase.
    ai_type = models.ForeignKey(Aitype, db_column='AI_TYPE', blank=True, null=True)  # Field name made lowercase.
    ca_max_hp = models.IntegerField(db_column='CA_MAX_HP', blank=True, null=True)  # Field name made lowercase.
    ca_additional_rage = models.IntegerField(db_column='CA_ADDITIONAL_RAGE', blank=True, null=True)  # Field name made lowercase.
    ca_max_mp = models.IntegerField(db_column='CA_MAX_MP', blank=True, null=True)  # Field name made lowercase.
    ca_physical = models.IntegerField(db_column='CA_PHYSICAL', blank=True, null=True)  # Field name made lowercase.
    ca_toughness = models.IntegerField(db_column='CA_TOUGHNESS', blank=True, null=True)  # Field name made lowercase.
    ca_speed = models.IntegerField(db_column='CA_SPEED', blank=True, null=True)  # Field name made lowercase.
    ca_lucky = models.IntegerField(db_column='CA_LUCKY', blank=True, null=True)  # Field name made lowercase.
    ca_will = models.IntegerField(db_column='CA_WILL', blank=True, null=True)  # Field name made lowercase.
    efe_water = models.IntegerField(db_column='EFE_WATER', blank=True, null=True)  # Field name made lowercase.
    efe_fire = models.IntegerField(db_column='EFE_FIRE', blank=True, null=True)  # Field name made lowercase.
    efe_thunder = models.IntegerField(db_column='EFE_THUNDER', blank=True, null=True)  # Field name made lowercase.
    efe_air = models.IntegerField(db_column='EFE_AIR', blank=True, null=True)  # Field name made lowercase.
    efe_earth = models.IntegerField(db_column='EFE_EARTH', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_additional = models.IntegerField(db_column='CA_ATTACK_PHYSICAL_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_additional = models.IntegerField(db_column='CA_ATTACK_WATER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_additional = models.IntegerField(db_column='CA_ATTACK_FIRE_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_additional = models.IntegerField(db_column='CA_ATTACK_THUNDER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_additional = models.IntegerField(db_column='CA_ATTACK_AIR_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_additional = models.IntegerField(db_column='CA_ATTACK_EARTH_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_extract = models.FloatField(db_column='CA_ATTACK_PHYSICAL_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_extract = models.FloatField(db_column='CA_ATTACK_WATER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_extract = models.FloatField(db_column='CA_ATTACK_FIRE_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_extract = models.FloatField(db_column='CA_ATTACK_THUNDER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_extract = models.FloatField(db_column='CA_ATTACK_AIR_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_extract = models.FloatField(db_column='CA_ATTACK_EARTH_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_react = models.FloatField(db_column='CA_ATTACK_PHYSICAL_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_react = models.FloatField(db_column='CA_ATTACK_WATER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_react = models.FloatField(db_column='CA_ATTACK_FIRE_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_react = models.FloatField(db_column='CA_ATTACK_THUNDER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_react = models.FloatField(db_column='CA_ATTACK_AIR_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_react = models.FloatField(db_column='CA_ATTACK_EARTH_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_additional_critical = models.FloatField(db_column='CA_ADDITIONAL_CRITICAL', blank=True, null=True)  # Field name made lowercase.
    ca_fend_off = models.FloatField(db_column='CA_FEND_OFF', blank=True, null=True)  # Field name made lowercase.
    ca_additional_hitting = models.FloatField(db_column='CA_ADDITIONAL_HITTING', blank=True, null=True)  # Field name made lowercase.
    ca_counterpunch_rate = models.FloatField(db_column='CA_COUNTERPUNCH_RATE', blank=True, null=True)  # Field name made lowercase.
    ca_pay_for_spare = models.FloatField(db_column='CA_PAY_FOR_SPARE', blank=True, null=True)  # Field name made lowercase.
    ca_experience = models.IntegerField(db_column='CA_EXPERIENCE', blank=True, null=True)  # Field name made lowercase.
    ca_level = models.IntegerField(db_column='CA_LEVEL', blank=True, null=True)  # Field name made lowercase.
    physical_atk_targett = models.ForeignKey('Physicalattacktarget', db_column='PHYSICAL_ATK_TARGETT', blank=True, null=True)  # Field name made lowercase.
    physical_atk_range = models.ForeignKey('Physicalattacktype', db_column='PHYSICAL_ATK_RANGE', blank=True, null=True)  # Field name made lowercase.
    monster_magic_1 = models.IntegerField(db_column='MONSTER_MAGIC_1', blank=True, null=True)  # Field name made lowercase.
    monster_magic_2 = models.IntegerField(db_column='MONSTER_MAGIC_2', blank=True, null=True)  # Field name made lowercase.
    monster_magic_3 = models.IntegerField(db_column='MONSTER_MAGIC_3', blank=True, null=True)  # Field name made lowercase.
    monster_magic_4 = models.IntegerField(db_column='MONSTER_MAGIC_4', blank=True, null=True)  # Field name made lowercase.
    monster_magic_5 = models.IntegerField(db_column='MONSTER_MAGIC_5', blank=True, null=True)  # Field name made lowercase.
    monster_magic_6 = models.IntegerField(db_column='MONSTER_MAGIC_6', blank=True, null=True)  # Field name made lowercase.
    ca_losable_property = models.IntegerField(db_column='CA_LOSABLE_PROPERTY', blank=True, null=True)  # Field name made lowercase.
    ca_the_losable_number = models.IntegerField(db_column='CA_THE_LOSABLE_NUMBER', blank=True, null=True)  # Field name made lowercase.
    ca_losable_money = models.IntegerField(db_column='CA_LOSABLE_MONEY', blank=True, null=True)  # Field name made lowercase.
    mdt_1_id = models.IntegerField(db_column='MDT_1_ID', blank=True, null=True)  # Field name made lowercase.
    mdt_1_rate = models.FloatField(db_column='MDT_1_RATE', blank=True, null=True)  # Field name made lowercase.
    mdt_2_id = models.IntegerField(db_column='MDT_2_ID', blank=True, null=True)  # Field name made lowercase.
    mdt_2_rate = models.FloatField(db_column='MDT_2_RATE', blank=True, null=True)  # Field name made lowercase.
    mdt_3_id = models.IntegerField(db_column='MDT_3_ID', blank=True, null=True)  # Field name made lowercase.
    mdt_3_rate = models.FloatField(db_column='MDT_3_RATE', blank=True, null=True)  # Field name made lowercase.
    mdt_4_id = models.IntegerField(db_column='MDT_4_ID', blank=True, null=True)  # Field name made lowercase.
    mdt_4_rate = models.FloatField(db_column='MDT_4_RATE', blank=True, null=True)  # Field name made lowercase.
    ma_max_drop_money = models.IntegerField(db_column='MA_MAX_DROP_MONEY', blank=True, null=True)  # Field name made lowercase.
    ma_min_drop_money = models.IntegerField(db_column='MA_MIN_DROP_MONEY', blank=True, null=True)  # Field name made lowercase.
    ma_atk_added_rage = models.IntegerField(db_column='MA_ATK_ADDED_RAGE', blank=True, null=True)  # Field name made lowercase.
    ca_rage = models.IntegerField(db_column='CA_RAGE', blank=True, null=True)  # Field name made lowercase.
    sound_wounded1 = models.TextField(db_column='SOUND_WOUNDED1', blank=True, null=True)  # Field name made lowercase.
    sound_wounded2 = models.TextField(db_column='SOUND_WOUNDED2', blank=True, null=True)  # Field name made lowercase.
    sound_wounded3 = models.TextField(db_column='SOUND_WOUNDED3', blank=True, null=True)  # Field name made lowercase.
    sound_wounded4 = models.TextField(db_column='SOUND_WOUNDED4', blank=True, null=True)  # Field name made lowercase.
    sound_wounded5 = models.TextField(db_column='SOUND_WOUNDED5', blank=True, null=True)  # Field name made lowercase.
    eff_final_hit = models.TextField(db_column='EFF_FINAL_HIT', blank=True, null=True)  # Field name made lowercase.
    acttype = models.ForeignKey(Acttype, db_column='ACTTYPE', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='COUNT', blank=True, null=True)  # Field name made lowercase.
    easb_bondage_immunity = models.FloatField(db_column='EASB_BONDAGE_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easb_seal_immunity = models.FloatField(db_column='EASB_SEAL_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easb_forbiden_immunity = models.FloatField(db_column='EASB_FORBIDEN_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easb_sleep_immunity = models.FloatField(db_column='EASB_SLEEP_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easb_mad_immunity = models.FloatField(db_column='EASB_MAD_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easb_disorder_immunity = models.FloatField(db_column='EASB_DISORDER_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easa_water_immunity = models.FloatField(db_column='EASA_WATER_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easa_fire_immunity = models.FloatField(db_column='EASA_FIRE_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easa_thunder_immunity = models.FloatField(db_column='EASA_THUNDER_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easa_air_immunity = models.FloatField(db_column='EASA_AIR_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    easa_earth_immunity = models.FloatField(db_column='EASA_EARTH_IMMUNITY', blank=True, null=True)  # Field name made lowercase.
    esi_siphon = models.FloatField(db_column='ESI_SIPHON', blank=True, null=True)  # Field name made lowercase.
    esi_mortal = models.FloatField(db_column='ESI_MORTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Monster'

    def __unicode__(self):
        return "怪物ID: %d, 怪物名称: %s, 怪物信息描述: %s" % (self.monster_id,self.ma_name,self.ma_desc)

#物理攻击目标
class Physicalattacktarget(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysicalAttackTarget'

#物理攻击方式
class Physicalattacktype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysicalAttackType'

#配方
class Prescription(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pra_name = models.TextField(db_column='PRA_NAME', blank=True, null=True)  # Field name made lowercase.
    pra_description = models.TextField(db_column='PRA_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    pra_property = models.TextField(db_column='PRA_PROPERTY', blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey('Prescriptiontype', db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    eet_sword = models.ForeignKey(Bool, db_column='EET_SWORD', blank=True, null=True, related_name='Bool_eet_swords')  # Field name made lowercase.
    eet_dsword = models.ForeignKey(Bool, db_column='EET_DSWORD', blank=True, null=True, related_name='Bool_eet_dswords')  # Field name made lowercase.
    eet_instrument = models.ForeignKey(Bool, db_column='EET_INSTRUMENT', blank=True, null=True, related_name='Bool_eet_instruments')  # Field name made lowercase.
    eet_helmet = models.ForeignKey(Bool, db_column='EET_HELMET', blank=True, null=True, related_name='Bool_eet_helmets')  # Field name made lowercase.
    eet_corselet = models.ForeignKey(Bool, db_column='EET_CORSELET', blank=True, null=True, related_name='Bool_eet_corselets')  # Field name made lowercase.
    eet_legharness = models.ForeignKey(Bool, db_column='EET_LEGHARNESS', blank=True, null=True, related_name='Bool_eet_legharnesss')  # Field name made lowercase.
    eet_ornament = models.ForeignKey(Bool, db_column='EET_ORNAMENT', blank=True, null=True, related_name='Bool_eet_ornaments')  # Field name made lowercase.
    pra_product_id = models.IntegerField(db_column='PRA_PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    pra_need_potential = models.IntegerField(db_column='PRA_NEED_POTENTIAL', blank=True, null=True)  # Field name made lowercase.
    pra_need_magic = models.IntegerField(db_column='PRA_NEED_MAGIC', blank=True, null=True)  # Field name made lowercase.
    pra_skill_id = models.IntegerField(db_column='PRA_SKILL_ID', blank=True, null=True)  # Field name made lowercase.
    pra_price = models.IntegerField(db_column='PRA_PRICE', blank=True, null=True)  # Field name made lowercase.
    p_mat_1 = models.IntegerField(db_column='P_MAT_1', blank=True, null=True)  # Field name made lowercase.
    p_mat_1_number = models.IntegerField(db_column='P_MAT_1_NUMBER', blank=True, null=True)  # Field name made lowercase.
    p_mat_2 = models.IntegerField(db_column='P_MAT_2', blank=True, null=True)  # Field name made lowercase.
    p_mat_2_number = models.IntegerField(db_column='P_MAT_2_NUMBER', blank=True, null=True)  # Field name made lowercase.
    p_mat_3 = models.IntegerField(db_column='P_MAT_3', blank=True, null=True)  # Field name made lowercase.
    p_mat_3_number = models.IntegerField(db_column='P_MAT_3_NUMBER', blank=True, null=True)  # Field name made lowercase.
    p_mat_4 = models.IntegerField(db_column='P_MAT_4', blank=True, null=True)  # Field name made lowercase.
    p_mat_4_number = models.IntegerField(db_column='P_MAT_4_NUMBER', blank=True, null=True)  # Field name made lowercase.
    pri_max_hp = models.IntegerField(db_column='PRI_MAX_HP', blank=True, null=True)  # Field name made lowercase.
    pri_added_rage = models.IntegerField(db_column='PRI_ADDED_RAGE', blank=True, null=True)  # Field name made lowercase.
    pri_max_mp = models.IntegerField(db_column='PRI_MAX_MP', blank=True, null=True)  # Field name made lowercase.
    pri_wu = models.IntegerField(db_column='PRI_WU', blank=True, null=True)  # Field name made lowercase.
    pri_defence = models.IntegerField(db_column='PRI_DEFENCE', blank=True, null=True)  # Field name made lowercase.
    pri_speed = models.IntegerField(db_column='PRI_SPEED', blank=True, null=True)  # Field name made lowercase.
    pri_lucky = models.IntegerField(db_column='PRI_LUCKY', blank=True, null=True)  # Field name made lowercase.
    pri_magic_attack = models.IntegerField(db_column='PRI_MAGIC_ATTACK', blank=True, null=True)  # Field name made lowercase.
    efe_water = models.IntegerField(db_column='EFE_WATER', blank=True, null=True)  # Field name made lowercase.
    efe_fire = models.IntegerField(db_column='EFE_FIRE', blank=True, null=True)  # Field name made lowercase.
    efe_thunder = models.IntegerField(db_column='EFE_THUNDER', blank=True, null=True)  # Field name made lowercase.
    efe_air = models.IntegerField(db_column='EFE_AIR', blank=True, null=True)  # Field name made lowercase.
    efe_earth = models.IntegerField(db_column='EFE_EARTH', blank=True, null=True)  # Field name made lowercase.
    paa_physical_add = models.IntegerField(db_column='PAA_PHYSICAL_ADD', blank=True, null=True)  # Field name made lowercase.
    paa_water_add = models.IntegerField(db_column='PAA_WATER_ADD', blank=True, null=True)  # Field name made lowercase.
    paa_fire_add = models.IntegerField(db_column='PAA_FIRE_ADD', blank=True, null=True)  # Field name made lowercase.
    paa_thunder_add = models.IntegerField(db_column='PAA_THUNDER_ADD', blank=True, null=True)  # Field name made lowercase.
    paa_air_add = models.IntegerField(db_column='PAA_AIR_ADD', blank=True, null=True)  # Field name made lowercase.
    paa_earth_add = models.IntegerField(db_column='PAA_EARTH_ADD', blank=True, null=True)  # Field name made lowercase.
    paa_physical_extract = models.FloatField(db_column='PAA_PHYSICAL_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    paa_water_extract = models.FloatField(db_column='PAA_WATER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    paa_fire_extract = models.FloatField(db_column='PAA_FIRE_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    paa_thunder_extract = models.FloatField(db_column='PAA_THUNDER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    paa_air_extract = models.FloatField(db_column='PAA_AIR_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    paa_earth_extract = models.FloatField(db_column='PAA_EARTH_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    paa_physical_react = models.FloatField(db_column='PAA_PHYSICAL_REACT', blank=True, null=True)  # Field name made lowercase.
    paa_water_react = models.FloatField(db_column='PAA_WATER_REACT', blank=True, null=True)  # Field name made lowercase.
    paa_fire_react = models.FloatField(db_column='PAA_FIRE_REACT', blank=True, null=True)  # Field name made lowercase.
    paa_thunder_react = models.FloatField(db_column='PAA_THUNDER_REACT', blank=True, null=True)  # Field name made lowercase.
    paa_air_react = models.FloatField(db_column='PAA_AIR_REACT', blank=True, null=True)  # Field name made lowercase.
    paa_earth_react = models.FloatField(db_column='PAA_EARTH_REACT', blank=True, null=True)  # Field name made lowercase.
    psa_added_critical = models.FloatField(db_column='PSA_ADDED_CRITICAL', blank=True, null=True)  # Field name made lowercase.
    psa_fend_off = models.FloatField(db_column='PSA_FEND_OFF', blank=True, null=True)  # Field name made lowercase.
    psa_added_hitting = models.FloatField(db_column='PSA_ADDED_HITTING', blank=True, null=True)  # Field name made lowercase.
    psa_pay_for_spare = models.FloatField(db_column='PSA_PAY_FOR_SPARE', blank=True, null=True)  # Field name made lowercase.
    calc_type = models.IntegerField(db_column='CALC_TYPE', blank=True, null=True)  # Field name made lowercase.
    pra_ef2 = models.TextField(db_column='PRA_EF2', blank=True, null=True)  # Field name made lowercase.
    pra_ef3 = models.TextField(db_column='PRA_EF3', blank=True, null=True)  # Field name made lowercase.
    pra_ef4 = models.TextField(db_column='PRA_EF4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prescription'

#配方类型
class Prescriptiontype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrescriptionType'

#预览信息，其实是游戏中的过场动画及原画
class Previewinfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    preview = models.TextField(db_column='PREVIEW', blank=True, null=True)  # Field name made lowercase.
    desc = models.TextField(db_column='DESC', blank=True, null=True)  # Field name made lowercase.
    file = models.TextField(db_column='FILE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreviewInfo'

#道具表
class Property(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pa_name = models.TextField(db_column='PA_NAME', blank=True, null=True)  # Field name made lowercase.
    pa_description = models.TextField(db_column='PA_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    pa_property = models.TextField(db_column='PA_PROPERTY', blank=True, null=True)  # Field name made lowercase.
    pa_icon = models.TextField(db_column='PA_ICON', blank=True, null=True)  # Field name made lowercase.
    pa_model = models.TextField(db_column='PA_MODEL', blank=True, null=True)  # Field name made lowercase.
    pa_texture = models.TextField(db_column='PA_TEXTURE', blank=True, null=True)  # Field name made lowercase.
    pa_attached_effect = models.TextField(db_column='PA_ATTACHED_EFFECT', blank=True, null=True)  # Field name made lowercase.
    pa_type = models.ForeignKey('Propertyclass', db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    prize_level = models.ForeignKey('Propertylevel', db_column='PRIZE_LEVEL', blank=True, null=True)  # Field name made lowercase.
    target = models.ForeignKey('Skilltarget', db_column='TARGET', blank=True, null=True)  # Field name made lowercase.
    ept_tianhe_can_use = models.ForeignKey(Bool, db_column='ePT_TIANHE_CAN_USE', blank=True, null=True, related_name='Bool_ept_tianhe_can_use')  # Field name made lowercase.
    ept_linsha_can_use = models.ForeignKey(Bool, db_column='ePT_LINSHA_CAN_USE', blank=True, null=True,                 related_name='Bool_ept_linsha_can_use')  # Field name made lowercase.
    ept_mengli_can_use = models.ForeignKey(Bool, db_column='ePT_MENGLI_CAN_USE', blank=True, null=True,                 related_name='Bool_ept_mengli_can_use')  # Field name made lowercase.
    ept_ziying_can_use = models.ForeignKey(Bool, db_column='ePT_ZIYING_CAN_USE', blank=True, null=True,                 related_name='Bool_ept_ziying_can_use')  # Field name made lowercase.
    ai_cmd_type = models.ForeignKey(Aicommandtype, db_column='AI_CMD_TYPE', blank=True, null=True)  # Field name made lowercase.
    pa_price = models.IntegerField(db_column='PA_PRICE', blank=True, null=True)  # Field name made lowercase.
    pa_attached_skill = models.IntegerField(db_column='PA_ATTACHED_SKILL', blank=True, null=True)  # Field name made lowercase.
    candrop = models.IntegerField(db_column='CANDROP', blank=True, null=True)  # Field name made lowziying.
    canuse_in_sysui = models.IntegerField(db_column='CANUSE_IN_SYSUI', blank=True, null=True)  # Field name made lowercase.
    pa_atk_type = models.IntegerField(db_column='PA_ATK_TYPE', blank=True, null=True)  # Field name made lowercase.
    pa_atk_delay = models.FloatField(db_column='PA_ATK_DELAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Property'
    def __unicode__(self):
        return "道具ID: %d, 道具名称: %s" % (self.id,self.pa_name)
#道具大类
class Propertyclass(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PropertyClass'

    def __unicode__(self):
        return " 道具大类ID: %d, 道具大类名称: %s" % (self.id,self.content)

#道具级别，实际上没什么用处的样子
class Propertylevel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PropertyLevel'

#种族类别
class Race(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Race'

#游戏角色（四大主角）
class Role(models.Model):
    role_id = models.IntegerField(db_column='ROLE_ID', primary_key=True)  # Field name made lowercase.
    ra_name = models.TextField(db_column='RA_NAME', blank=True, null=True)  # Field name made lowercase.
    ra_icon = models.TextField(db_column='RA_ICON', blank=True, null=True)  # Field name made lowercase.
    ra_model = models.TextField(db_column='RA_MODEL', blank=True, null=True)  # Field name made lowercase.
    ra_texture = models.TextField(db_column='RA_TEXTURE', blank=True, null=True)  # Field name made lowercase.
    race = models.ForeignKey(Race, db_column='RACE', blank=True, null=True)  # Field name made lowercase.
    ept_tianhe_favor = models.IntegerField(db_column='ePT_TIANHE_FAVOR', blank=True, null=True)  # Field name made lowercase.
    ept_linsha_favor = models.IntegerField(db_column='ePT_LINSHA_FAVOR', blank=True, null=True)  # Field name made lowercase.
    ept_mengli_favor = models.IntegerField(db_column='ePT_MENGLI_FAVOR', blank=True, null=True)  # Field name made lowercase.
    ept_ziying_favor = models.IntegerField(db_column='ePT_ZIYING_FAVOR', blank=True, null=True)  # Field name made lowercase.
    ca_max_hp = models.IntegerField(db_column='CA_MAX_HP', blank=True, null=True)  # Field name made lowercase.
    ca_additional_rage = models.IntegerField(db_column='CA_ADDITIONAL_RAGE', blank=True, null=True)  # Field name made lowercase.
    ca_max_mp = models.IntegerField(db_column='CA_MAX_MP', blank=True, null=True)  # Field name made lowercase.
    ca_physical = models.IntegerField(db_column='CA_PHYSICAL', blank=True, null=True)  # Field name made lowercase.
    ca_toughness = models.IntegerField(db_column='CA_TOUGHNESS', blank=True, null=True)  # Field name made lowercase.
    ca_speed = models.IntegerField(db_column='CA_SPEED', blank=True, null=True)  # Field name made lowercase.
    ca_lucky = models.IntegerField(db_column='CA_LUCKY', blank=True, null=True)  # Field name made lowercase.
    ca_will = models.IntegerField(db_column='CA_WILL', blank=True, null=True)  # Field name made lowercase.
    efe_water = models.IntegerField(db_column='EFE_WATER', blank=True, null=True)  # Field name made lowercase.
    efe_fire = models.IntegerField(db_column='EFE_FIRE', blank=True, null=True)  # Field name made lowercase.
    efe_thunder = models.IntegerField(db_column='EFE_THUNDER', blank=True, null=True)  # Field name made lowercase.
    efe_air = models.IntegerField(db_column='EFE_AIR', blank=True, null=True)  # Field name made lowercase.
    efe_earth = models.IntegerField(db_column='EFE_EARTH', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_additional = models.IntegerField(db_column='CA_ATTACK_PHYSICAL_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_additional = models.IntegerField(db_column='CA_ATTACK_WATER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_additional = models.IntegerField(db_column='CA_ATTACK_FIRE_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_additional = models.IntegerField(db_column='CA_ATTACK_THUNDER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_additional = models.IntegerField(db_column='CA_ATTACK_AIR_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_additional = models.IntegerField(db_column='CA_ATTACK_EARTH_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_extract = models.FloatField(db_column='CA_ATTACK_PHYSICAL_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_extract = models.FloatField(db_column='CA_ATTACK_WATER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_extract = models.FloatField(db_column='CA_ATTACK_FIRE_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_extract = models.FloatField(db_column='CA_ATTACK_THUNDER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_extract = models.FloatField(db_column='CA_ATTACK_AIR_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_extract = models.FloatField(db_column='CA_ATTACK_EARTH_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_react = models.FloatField(db_column='CA_ATTACK_PHYSICAL_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_react = models.FloatField(db_column='CA_ATTACK_WATER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_react = models.FloatField(db_column='CA_ATTACK_FIRE_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_react = models.FloatField(db_column='CA_ATTACK_THUNDER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_react = models.FloatField(db_column='CA_ATTACK_AIR_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_react = models.FloatField(db_column='CA_ATTACK_EARTH_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_additional_critical = models.FloatField(db_column='CA_ADDITIONAL_CRITICAL', blank=True, null=True)  # Field name made lowercase.
    ca_fend_off = models.FloatField(db_column='CA_FEND_OFF', blank=True, null=True)  # Field name made lowercase.
    ca_additional_hitting = models.FloatField(db_column='CA_ADDITIONAL_HITTING', blank=True, null=True)  # Field name made lowercase.
    ca_pay_for_spare = models.FloatField(db_column='CA_PAY_FOR_SPARE', blank=True, null=True)  # Field name made lowercase.
    physical_atk_target = models.ForeignKey(Physicalattacktarget, db_column='PHYSICAL_ATK_TARGET', blank=True, null=True)  # Field name made lowercase.
    physical_atk_range = models.ForeignKey(Physicalattacktype, db_column='PHYSICAL_ATK_RANGE', blank=True, null=True)  # Field name made lowercase.
    sound_wounded1 = models.TextField(db_column='SOUND_WOUNDED1', blank=True, null=True)  # Field name made lowercase.
    sound_wounded2 = models.TextField(db_column='SOUND_WOUNDED2', blank=True, null=True)  # Field name made lowercase.
    sound_wounded3 = models.TextField(db_column='SOUND_WOUNDED3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role'

#场景表，包括全部的室内室外区域
class Scene(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    scene = models.TextField(db_column='SCENE', blank=True, null=True)  # Field name made lowercase.
    section = models.TextField(db_column='SECTION', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    earthball = models.IntegerField(db_column='EARTHBALL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scene'

    def __unicode__(self):
        return "场景: %s, 区块: %s, 名称: %s" % (self.scene,self.section,self.name)

#场景物品表，包含所有在场景内能收集到的装备，道具，钱，以及各种宝箱的情况（含只有紫英能采的矿石）
class Sceneitem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    scene = models.CharField(db_column='SCENE', max_length=512)  # Field name made lowercase.
    section = models.CharField(db_column='SECTION', max_length=512)  # Field name made lowercase.
    si_id = models.CharField(db_column='SI_ID', max_length=512)  # Field name made lowercase.
    si_model_path = models.CharField(db_column='SI_MODEL_PATH', max_length=512)  # Field name made lowercase.
    si_model = models.CharField(db_column='SI_MODEL', max_length=512)  # Field name made lowercase.
    si_texture = models.CharField(db_column='SI_TEXTURE', max_length=512)  # Field name made lowercase.
    si_coor_x = models.DecimalField(db_column='SI_COOR_X', max_digits=8, decimal_places=3)  # Field name made lowercase.
    si_coor_y = models.DecimalField(db_column='SI_COOR_Y', max_digits=8, decimal_places=3)  # Field name made lowercase.
    si_coor_z = models.DecimalField(db_column='SI_COOR_Z', max_digits=8, decimal_places=3)  # Field name made lowercase.
    si_ea_id = models.IntegerField(db_column='SI_EA_ID', blank=True, null=True)  # Field name made lowercase.
    si_pa_id = models.IntegerField(db_column='SI_PA_ID', blank=True, null=True)  # Field name made lowercase.
    si_num = models.IntegerField(db_column='SI_NUM', blank=True, null=True)  # Field name made lowercase.
    si_money = models.IntegerField(db_column='SI_MONEY', blank=True, null=True)  # Field name made lowercase.
    si_item_1_id = models.IntegerField(db_column='SI_ITEM_1_ID', blank=True, null=True)  # Field name made lowercase.
    si_item_1_num = models.IntegerField(db_column='SI_ITEM_1_NUM', blank=True, null=True)  # Field name made lowercase.
    si_item_2_id = models.IntegerField(db_column='SI_ITEM_2_ID', blank=True, null=True)  # Field name made lowercase.
    si_item_2_num = models.IntegerField(db_column='SI_ITEM_2_NUM', blank=True, null=True)  # Field name made lowercase.
    si_item_3_id = models.IntegerField(db_column='SI_ITEM_3_ID', blank=True, null=True)  # Field name made lowercase.
    si_item_3_num = models.IntegerField(db_column='SI_ITEM_3_NUM', blank=True, null=True)  # Field name made lowercase.
    si_item_4_id = models.IntegerField(db_column='SI_ITEM_4_ID', blank=True, null=True)  # Field name made lowercase.
    si_item_4_num = models.IntegerField(db_column='SI_ITEM_4_NUM', blank=True, null=True)  # Field name made lowercase.
    si_item_5_id = models.IntegerField(db_column='SI_ITEM_5_ID', blank=True, null=True)  # Field name made lowercase.
    si_item_5_num = models.IntegerField(db_column='SI_ITEM_5_NUM', blank=True, null=True)  # Field name made lowercase.
    si_item_6_id = models.IntegerField(db_column='SI_ITEM_6_ID', blank=True, null=True)  # Field name made lowercase.
    si_item_6_num = models.IntegerField(db_column='SI_ITEM_6_NUM', blank=True, null=True)  # Field name made lowercase.
    si_item_money = models.IntegerField(db_column='SI_ITEM_MONEY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SceneItem'

    def __unicode__(self):
        return "场景: %s, 区块: %s, 物品编号: %s, 模型路径: %s, 模型: %s, 贴图: %s" % (self.scene,self.section,self.si_id,self.si_model_path,si_model,si_texture)

#场景名称表，场景名称与场景编号的对应关系
class Scenename(models.Model):
    scene = models.CharField(db_column='SCENE', primary_key=True, max_length=5)  # Field name made lowercase.
    cn_name = models.CharField(db_column='CN_NAME', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SceneName'

#店铺属性表，包括了种类，名称信息，小摊贩及NPC均囊括其中
class Shopproperty(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    position = models.TextField(db_column='POSITION', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShopProperty'

    def __unicode__(self):
	return """
		店铺ID: %s
		店铺名称: %s
		店铺位置: %s
	       """ % (self.id,
		      self.name,
		      self.position,
		      )

#店铺类型
class Shoptype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShopType'

    def __unicode__(self):
        return """
                店铺类型ID: %d
                店铺类型名称: %s
               """ % (self.id,
                      self.content,
                      )

#技能表，仙术和特技均会映射到这里来
class Skill(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.ForeignKey('Skilltype', db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    triger = models.ForeignKey('Skilltrigertype', db_column='TRIGER', blank=True, null=True)  # Field name made lowercase.
    exist_time = models.IntegerField(db_column='EXIST_TIME', blank=True, null=True)  # Field name made lowercase.
    function = models.IntegerField(db_column='FUNCTION', blank=True, null=True)  # Field name made lowercase.
    skill_param_1 = models.FloatField(db_column='SKILL_PARAM_1', blank=True, null=True)  # Field name made lowercase.
    skill_param_2 = models.FloatField(db_column='SKILL_PARAM_2', blank=True, null=True)  # Field name made lowercase.
    skill_param_3 = models.FloatField(db_column='SKILL_PARAM_3', blank=True, null=True)  # Field name made lowercase.
    skill_param_4 = models.FloatField(db_column='SKILL_PARAM_4', blank=True, null=True)  # Field name made lowercase.
    skill_param_5 = models.FloatField(db_column='SKILL_PARAM_5', blank=True, null=True)  # Field name made lowercase.
    skill_param_6 = models.FloatField(db_column='SKILL_PARAM_6', blank=True, null=True)  # Field name made lowercase.
    skill_param_7 = models.FloatField(db_column='SKILL_PARAM_7', blank=True, null=True)  # Field name made lowercase.
    skill_param_8 = models.FloatField(db_column='SKILL_PARAM_8', blank=True, null=True)  # Field name made lowercase.
    skill_param_9 = models.FloatField(db_column='SKILL_PARAM_9', blank=True, null=True)  # Field name made lowercase.
    attached_skill = models.IntegerField(db_column='ATTACHED_SKILL', blank=True, null=True)  # Field name made lowercase.
    mutex_id = models.IntegerField(db_column='MUTEX_ID', blank=True, null=True)  # Field name made lowercase.
    status_id = models.IntegerField(db_column='STATUS_ID', blank=True, null=True)  # Field name made lowercase.
    ef = models.TextField(db_column='EF', blank=True, null=True)  # Field name made lowercase.
    bind = models.TextField(db_column='BIND', blank=True, null=True)  # Field name made lowercase.
    ef1 = models.TextField(db_column='EF1', blank=True, null=True)  # Field name made lowercase.
    bind1 = models.TextField(db_column='BIND1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Skill'

#技能目标
class Skilltarget(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SkillTarget'

#技能触发条件
class Skilltrigertype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SkillTrigerType'

#技能类别
class Skilltype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SkillType'

#剧情明细表
class Story(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    memo = models.TextField(db_column='MEMO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Story'

#剧情简要描述
class Storydesc(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    chapter = models.TextField(db_column='CHAPTER', blank=True, null=True)  # Field name made lowercase.
    memo = models.TextField(db_column='MEMO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoryDesc'

#特技
class Stunt(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    prop = models.TextField(db_column='PROP', blank=True, null=True)  # Field name made lowercase.
    ai_cmd_type = models.ForeignKey(Aicommandtype, db_column='AI_CMD_TYPE', blank=True, null=True)  # Field name made lowercase.
    target = models.ForeignKey(Skilltarget, db_column='TARGET', blank=True, null=True)  # Field name made lowercase.
    ept_tianhe_lv_lmt = models.IntegerField(db_column='ePT_TIANHE_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    ept_linsha_lv_lmt = models.IntegerField(db_column='ePT_LINSHA_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    ept_mengli_lv_lmt = models.IntegerField(db_column='ePT_MENGLI_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    ept_ziying_lv_lmt = models.IntegerField(db_column='ePT_ZIYING_LV_LMT', blank=True, null=True)  # Field name made lowercase.
    attached_skill = models.IntegerField(db_column='ATTACHED_SKILL', blank=True, null=True)  # Field name made lowercase.
    consumed_rage = models.IntegerField(db_column='CONSUMED_RAGE', blank=True, null=True)  # Field name made lowercase.
    scp_id_1 = models.IntegerField(db_column='SCP_ID_1', blank=True, null=True)  # Field name made lowercase.
    scp_id_1_number = models.IntegerField(db_column='SCP_ID_1_NUMBER', blank=True, null=True)  # Field name made lowercase.
    scp_id_2 = models.IntegerField(db_column='SCP_ID_2', blank=True, null=True)  # Field name made lowercase.
    scp_id_2_number = models.IntegerField(db_column='SCP_ID_2_NUMBER', blank=True, null=True)  # Field name made lowercase.
    scp_id_3 = models.IntegerField(db_column='SCP_ID_3', blank=True, null=True)  # Field name made lowercase.
    scp_id_3_number = models.IntegerField(db_column='SCP_ID_3_NUMBER', blank=True, null=True)  # Field name made lowercase.
    scp_id_4 = models.IntegerField(db_column='SCP_ID_4', blank=True, null=True)  # Field name made lowercase.
    scp_id_4_number = models.IntegerField(db_column='SCP_ID_4_NUMBER', blank=True, null=True)  # Field name made lowercase.
    scp_id_5 = models.IntegerField(db_column='SCP_ID_5', blank=True, null=True)  # Field name made lowercase.
    scp_id_5_number = models.IntegerField(db_column='SCP_ID_5_NUMBER', blank=True, null=True)  # Field name made lowercase.
    consumed_money = models.IntegerField(db_column='CONSUMED_MONEY', blank=True, null=True)  # Field name made lowercase.
    need_prop_id = models.IntegerField(db_column='NEED_PROP_ID', blank=True, null=True)  # Field name made lowercase.
    skill_depended = models.IntegerField(db_column='SKILL_DEPENDED', blank=True, null=True)  # Field name made lowercase.
    acttype = models.ForeignKey(Acttype, db_column='ACTTYPE', blank=True, null=True)  # Field name made lowercase.
    hit_extra = models.FloatField(db_column='HIT_EXTRA', blank=True, null=True)  # Field name made lowercase.
    animation = models.TextField(db_column='ANIMATION', blank=True, null=True)  # Field name made lowercase.
    effect = models.TextField(db_column='EFFECT', blank=True, null=True)  # Field name made lowercase.
    target_ef = models.TextField(db_column='TARGET_EF', blank=True, null=True)  # Field name made lowercase.
    target_bind = models.TextField(db_column='TARGET_BIND', blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(db_column='MODEL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stunt'

#队伍状态
class Teamstate(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeamState'

#新手教程
class Tutorial(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    string = models.TextField(db_column='STRING', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tutorial'

#UI界面
class Ui(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UI'

#人物升级数据
class Upgradedata(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    ca_level = models.IntegerField(db_column='CA_LEVEL', blank=True, null=True)  # Field name made lowercase.
    ca_experience = models.IntegerField(db_column='CA_EXPERIENCE', blank=True, null=True)  # Field name made lowercase.
    ca_max_hp = models.IntegerField(db_column='CA_MAX_HP', blank=True, null=True)  # Field name made lowercase.
    ca_additional_rage = models.IntegerField(db_column='CA_ADDITIONAL_RAGE', blank=True, null=True)  # Field name made lowercase.
    ca_max_mp = models.IntegerField(db_column='CA_MAX_MP', blank=True, null=True)  # Field name made lowercase.
    ca_physical = models.IntegerField(db_column='CA_PHYSICAL', blank=True, null=True)  # Field name made lowercase.
    ca_toughness = models.IntegerField(db_column='CA_TOUGHNESS', blank=True, null=True)  # Field name made lowercase.
    ca_speed = models.IntegerField(db_column='CA_SPEED', blank=True, null=True)  # Field name made lowercase.
    ca_lucky = models.IntegerField(db_column='CA_LUCKY', blank=True, null=True)  # Field name made lowercase.
    ca_will = models.IntegerField(db_column='CA_WILL', blank=True, null=True)  # Field name made lowercase.
    efe_water = models.IntegerField(db_column='EFE_WATER', blank=True, null=True)  # Field name made lowercase.
    efe_fire = models.IntegerField(db_column='EFE_FIRE', blank=True, null=True)  # Field name made lowercase.
    efe_thunder = models.IntegerField(db_column='EFE_THUNDER', blank=True, null=True)  # Field name made lowercase.
    efe_air = models.IntegerField(db_column='EFE_AIR', blank=True, null=True)  # Field name made lowercase.
    efe_earth = models.IntegerField(db_column='EFE_EARTH', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_additional = models.IntegerField(db_column='CA_ATTACK_PHYSICAL_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_additional = models.IntegerField(db_column='CA_ATTACK_WATER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_additional = models.IntegerField(db_column='CA_ATTACK_FIRE_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_additional = models.IntegerField(db_column='CA_ATTACK_THUNDER_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_additional = models.IntegerField(db_column='CA_ATTACK_AIR_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_additional = models.IntegerField(db_column='CA_ATTACK_EARTH_ADDITIONAL', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_extract = models.FloatField(db_column='CA_ATTACK_PHYSICAL_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_extract = models.FloatField(db_column='CA_ATTACK_WATER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_extract = models.FloatField(db_column='CA_ATTACK_FIRE_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_extract = models.FloatField(db_column='CA_ATTACK_THUNDER_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_extract = models.FloatField(db_column='CA_ATTACK_AIR_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_extract = models.FloatField(db_column='CA_ATTACK_EARTH_EXTRACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_physical_react = models.FloatField(db_column='CA_ATTACK_PHYSICAL_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_water_react = models.FloatField(db_column='CA_ATTACK_WATER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_fire_react = models.FloatField(db_column='CA_ATTACK_FIRE_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_thunder_react = models.FloatField(db_column='CA_ATTACK_THUNDER_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_air_react = models.FloatField(db_column='CA_ATTACK_AIR_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_attack_earth_react = models.FloatField(db_column='CA_ATTACK_EARTH_REACT', blank=True, null=True)  # Field name made lowercase.
    ca_additional_critical = models.FloatField(db_column='CA_ADDITIONAL_CRITICAL', blank=True, null=True)  # Field name made lowercase.
    ca_fend_off = models.FloatField(db_column='CA_FEND_OFF', blank=True, null=True)  # Field name made lowercase.
    ca_additional_hitting = models.FloatField(db_column='CA_ADDITIONAL_HITTING', blank=True, null=True)  # Field name made lowercase.
    ca_pay_for_spare = models.FloatField(db_column='CA_PAY_FOR_SPARE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UpgradeData'

#人物成长参数
class Upgradeparam(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hpupgradeparam1 = models.FloatField(db_column='HpUpgradeParam1', blank=True, null=True)  # Field name made lowercase.
    hpupgradeparam2 = models.FloatField(db_column='HpUpgradeParam2', blank=True, null=True)  # Field name made lowercase.
    hpupgradeparam3 = models.FloatField(db_column='HpUpgradeParam3', blank=True, null=True)  # Field name made lowercase.
    hpupgradeparam4 = models.FloatField(db_column='HpUpgradeParam4', blank=True, null=True)  # Field name made lowercase.
    mpupgradeparam1 = models.FloatField(db_column='MpUpgradeParam1', blank=True, null=True)  # Field name made lowercase.
    mpupgradeparam2 = models.FloatField(db_column='MpUpgradeParam2', blank=True, null=True)  # Field name made lowercase.
    mpupgradeparam3 = models.FloatField(db_column='MpUpgradeParam3', blank=True, null=True)  # Field name made lowercase.
    physicalupgradeparam1 = models.FloatField(db_column='PhysicalUpgradeParam1', blank=True, null=True)  # Field name made lowercase.
    physicalupgradeparam2 = models.FloatField(db_column='PhysicalUpgradeParam2', blank=True, null=True)  # Field name made lowercase.
    physicalupgradeparam3 = models.FloatField(db_column='PhysicalUpgradeParam3', blank=True, null=True)  # Field name made lowercase.
    toughnessupgradeparam1 = models.FloatField(db_column='ToughnessUpgradeParam1', blank=True, null=True)  # Field name made lowercase.
    toughnessupgradeparam2 = models.FloatField(db_column='ToughnessUpgradeParam2', blank=True, null=True)  # Field name made lowercase.
    toughnessupgradeparam3 = models.FloatField(db_column='ToughnessUpgradeParam3', blank=True, null=True)  # Field name made lowercase.
    speedupgradeparam1 = models.FloatField(db_column='SpeedUpgradeParam1', blank=True, null=True)  # Field name made lowercase.
    speedupgradeparam2 = models.FloatField(db_column='SpeedUpgradeParam2', blank=True, null=True)  # Field name made lowercase.
    speedupgradeparam3 = models.FloatField(db_column='SpeedUpgradeParam3', blank=True, null=True)  # Field name made lowercase.
    luckyupgradeparam1 = models.FloatField(db_column='LuckyUpgradeParam1', blank=True, null=True)  # Field name made lowercase.
    luckyupgradeparam2 = models.FloatField(db_column='LuckyUpgradeParam2', blank=True, null=True)  # Field name made lowercase.
    luckyupgradeparam3 = models.FloatField(db_column='LuckyUpgradeParam3', blank=True, null=True)  # Field name made lowercase.
    willupgradeparam1 = models.FloatField(db_column='WillUpgradeParam1', blank=True, null=True)  # Field name made lowercase.
    willupgradeparam2 = models.FloatField(db_column='WillUpgradeParam2', blank=True, null=True)  # Field name made lowercase.
    willupgradeparam3 = models.FloatField(db_column='WillUpgradeParam3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UpgradeParam'

#以下1~9，为9个异常状态表
class Weaknessid1(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_1'


class Weaknessid2(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_2'


class Weaknessid3(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_3'


class Weaknessid4(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_4'


class Weaknessid5(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_5'


class Weaknessid6(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_6'


class Weaknessid7(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_7'


class Weaknessid8(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_8'


class Weaknessid9(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WeaknessID_9'

#五灵属性对照表
class Wuling(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WuLing'

