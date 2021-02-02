drop table if exists `clothes`;
CREATE TABLE `clothes` (
 `id` smallint(4) unsigned NOT NULL COMMENT '编号',
 `name` varchar(8) NOT NULL COMMENT '名称',
 `icon` smallint(4) unsigned NOT NULL COMMENT '图示id',
 `role` smallint(4) unsigned NOT NULL COMMENT '角色',
 `description` varchar(48) NOT NULL COMMENT '描述',
 `property` varchar(40) NOT NULL COMMENT '作用',

 `physical_defense` smallint(3) unsigned NOT NULL COMMENT '防御',
 `magic_defense` smallint(3) unsigned NOT NULL COMMENT '仙防',
 `speed` tinyint(2) unsigned NOT NULL COMMENT '身法',
 `lucky` tinyint(2) unsigned NOT NULL COMMENT '运势',
 `hitting` tinyint(2) unsigned NOT NULL COMMENT '命中',
 `dodge` tinyint(2) unsigned NOT NULL COMMENT '闪避',
 `block` tinyint(2) unsigned NOT NULL COMMENT '招架',

 `price` smallint(5) unsigned NOT NULL COMMENT '价格',
 `sticks` tinyint(1) unsigned NOT NULL COMMENT '贴符数',
 `can_drop` tinyint(1) NOT NULL COMMENT '卖出丢弃',

 `freeze_resist` tinyint(2) unsigned NOT NULL COMMENT '冻结抗性',
 `poison_resist` tinyint(2) unsigned NOT NULL COMMENT '中毒抗性',
 `mana_burn_rate` tinyint(2) unsigned NOT NULL COMMENT '灼魔几率',
 `chaos_resist` tinyint(2) unsigned NOT NULL COMMENT '混乱抗性',
 `weak_resist` tinyint(2) unsigned NOT NULL COMMENT '脱力抗性',
 `palsy_resist` tinyint(2) unsigned NOT NULL COMMENT '麻痹抗性',
 `silent_resist` tinyint(2) unsigned NOT NULL COMMENT '沉默抗性',
 `change_resist` tinyint(2) unsigned NOT NULL COMMENT '异变抗性',
 `sleep_resist` tinyint(2) unsigned NOT NULL COMMENT '昏睡抗性',
 `passive_resist` tinyint(2) unsigned NOT NULL COMMENT '消极抗性',
 `foul_resist` tinyint(2) unsigned NOT NULL COMMENT '污浊抗性',
 
 `water_resist` tinyint(2) unsigned NOT NULL COMMENT '水抗性',
 `fire_resist` tinyint(2) unsigned NOT NULL COMMENT '火抗性',
 `earth_resist` tinyint(2) unsigned NOT NULL COMMENT '土抗性',
 `air_resist` tinyint(2) unsigned NOT NULL COMMENT '风抗性',
 `thunder_resist` tinyint(2) unsigned NOT NULL COMMENT '雷抗性',
 `yin_resist` tinyint(2) unsigned NOT NULL COMMENT '阴抗性',
 
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='衣服表';