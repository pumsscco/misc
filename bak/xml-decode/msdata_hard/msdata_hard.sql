DROP TABLE IF EXISTS `msdata_hard`;
CREATE TABLE `msdata_hard` (
  `id` smallint(5) unsigned NOT NULL COMMENT '编号',      -- **
  `name` varchar(8) NOT NULL COMMENT '名称',      -- **
  `race` tinyint(1) unsigned NOT NULL COMMENT '种族',     -- **
  `charm` smallint(3) unsigned NOT NULL COMMENT '符',         -- **
  `seal_diff` tinyint(2) unsigned NOT NULL COMMENT '封印难度',        -- **
  `hp` mediumint(7) unsigned NOT NULL COMMENT 'hp',       -- **
  `physical_attack` smallint(5) unsigned NOT NULL COMMENT '物攻',         -- **
  `magic_attack` smallint(4) unsigned NOT NULL COMMENT '仙攻',          -- **
  `physical_defense` smallint(4) unsigned NOT NULL COMMENT '防御',        -- **
  `magic_defense` smallint(4) unsigned NOT NULL COMMENT '仙防',       -- **
  `speed` smallint(3) unsigned NOT NULL COMMENT '身法',     -- **
  `hitting` tinyint(3) unsigned NOT NULL COMMENT '命中',        -- **
  `dodge` tinyint(2) unsigned NOT NULL COMMENT '闪避',      -- **
  `block` tinyint(2) unsigned NOT NULL COMMENT '招架',      -- **
  `weak` tinyint(1) unsigned NOT NULL COMMENT '弱点属性',       -- **
  `self` tinyint(1) unsigned NOT NULL COMMENT '自身属性',       -- **
  `pa_attr` tinyint(1) unsigned NOT NULL COMMENT '物攻属性',      -- **
  `critical` tinyint(2) unsigned NOT NULL COMMENT '爆击率',     -- **
  `combo_rate` tinyint(2) unsigned NOT NULL COMMENT '连击率',         -- **
  `water_resist` smallint(3) NOT NULL COMMENT '水抗性',       -- **
  `fire_resist` smallint(3) NOT NULL COMMENT '火抗性',        -- **
  `earth_resist` smallint(3) NOT NULL COMMENT '土抗性',     -- **
  `air_resist` smallint(3) NOT NULL COMMENT '风抗性',       -- **
  `thunder_resist` smallint(3) NOT NULL COMMENT '雷抗性',     -- **
  `yin_resist` smallint(3) NOT NULL COMMENT '阴抗性',       -- **
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='怪物信息表（困难难度）';

SELECT id,name,`exp`,`level`,hp,water_resist,fire_resist,earth_resist,air_resist,thunder_resist FROM `msdata_hard`

SELECT n.id,n.name,n.hp,e.hp,h.hp 
FROM `msdata_easy` as e ,`msdata` as n, `msdata_hard` as h 
where n.id=e.id and n.id=h.id;


SELECT id,name,race,level,hp,
physical_attack,physical_defense,magic_attack,magic_defense,
water_resist,fire_resist,thunder_resist,air_resist,earth_resist,yin_resist,yang_resist
FROM `msdata_hard` where name='瀚漠蝎王'
