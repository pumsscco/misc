CREATE TABLE `weapon` (
 `id` smallint(4) unsigned NOT NULL COMMENT '编号',
 `model_id` smallint(5) unsigned NOT NULL COMMENT '模型id',
 `model_id2` smallint(5) unsigned NOT NULL COMMENT '模型id2',
 `icon_id` smallint(3) unsigned NOT NULL COMMENT '图示id',
 `texture` smallint(5) unsigned NOT NULL COMMENT '刀光贴图',
 `name` varchar(8) NOT NULL COMMENT '名称',
 `role` smallint(4) unsigned NOT NULL COMMENT '角色',
 `description` varchar(48) NOT NULL COMMENT '描述',
 `property` varchar(32) NOT NULL COMMENT '作用',
 `action_id` tinyint(1) unsigned NOT NULL COMMENT '动作号',
 `physical_attack` smallint(3) unsigned NOT NULL COMMENT '物攻',
 `magic_attack` smallint(3) unsigned NOT NULL COMMENT '仙攻',
 `physical_defense` smallint(3) unsigned NOT NULL COMMENT '防御',
 `magic_defense` smallint(3) unsigned NOT NULL COMMENT '仙防',
 `speed` tinyint(2) unsigned NOT NULL COMMENT '身法',
 `lucky` tinyint(2) unsigned NOT NULL COMMENT '运势',
 `hitting` tinyint(2) unsigned NOT NULL COMMENT '命中',
 `dodge` tinyint(2) unsigned NOT NULL COMMENT '闪避',
 `block` tinyint(2) unsigned NOT NULL COMMENT '招架',
 `critical` tinyint(2) unsigned NOT NULL COMMENT '爆击',
 `combo_rate` tinyint(2) unsigned NOT NULL COMMENT '连击率',
 `field1` varchar(8) NOT NULL COMMENT 'field1',
 `attribute` tinyint(1) unsigned NOT NULL COMMENT '属性',
 `sticks` tinyint(1) unsigned NOT NULL COMMENT '贴符数',
 `price` smallint(5) unsigned NOT NULL COMMENT '价格',
 `can_drop` tinyint(1) NOT NULL COMMENT '卖出丢弃',
 `field2` varchar(8) NOT NULL COMMENT 'field2',
 `freeze_rate` tinyint(2) unsigned NOT NULL COMMENT '冻结几率',
 `poison_rate` tinyint(2) unsigned NOT NULL COMMENT '中毒几率',
 `weak_rate` tinyint(2) unsigned NOT NULL COMMENT '脱力几率',
 `palsy_rate` tinyint(2) unsigned NOT NULL COMMENT '麻痹几率',
 `silent_rate` tinyint(2) unsigned NOT NULL COMMENT '沉默几率',
 `change_rate` tinyint(2) unsigned NOT NULL COMMENT '异变几率',
 `sleep_rate` tinyint(2) unsigned NOT NULL COMMENT '昏睡几率',
 `field3` varchar(8) NOT NULL COMMENT 'field3',
 `water_add` tinyint(2) unsigned NOT NULL COMMENT '水加成',
 `fire_add` tinyint(2) unsigned NOT NULL COMMENT '火加成',
 `earth_add` tinyint(2) unsigned NOT NULL COMMENT '土加成',
 `air_add` tinyint(2) unsigned NOT NULL COMMENT '风加成',
 `thunder_add` tinyint(2) unsigned NOT NULL COMMENT '雷加成',
 `yin_add` tinyint(2) unsigned NOT NULL COMMENT '阴加成',
 `yang_add` tinyint(2) unsigned NOT NULL COMMENT '阳加成',
 `field4` varchar(8) NOT NULL COMMENT 'field4',
 `comment` varchar(16) NOT NULL COMMENT '备注',
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='武器表'