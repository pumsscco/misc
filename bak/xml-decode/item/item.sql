drop table if exists`item`;
CREATE TABLE `item` (
 `id` smallint(3) unsigned NOT NULL COMMENT '编号',
 `pic` smallint(4) unsigned NOT NULL COMMENT '图示id',
 `icon` tinyint(1)  unsigned NOT NULL COMMENT '图标id',
 `name` varchar(8) NOT NULL COMMENT '名称',
 `description` varchar(64) NOT NULL COMMENT '描述',
 `property` varchar(32) NOT NULL COMMENT '作用',

 `drop_rate` tinyint(3) unsigned NOT NULL COMMENT '掉落',
 `ef` smallint(5) unsigned NOT NULL COMMENT '特效id',
 `script` smallint(4) unsigned NOT NULL COMMENT '脚本id',  
 `kind` tinyint(1) unsigned NOT NULL COMMENT '种类', 
 `attr` tinyint(1) unsigned NOT NULL COMMENT '属性',
 `price` mediumint(6) unsigned NOT NULL COMMENT '价格',
 `short_perm` tinyint(1) unsigned NOT NULL COMMENT '快捷许可',
 `can_drop` tinyint(1) unsigned NOT NULL COMMENT '买卖丢弃',

 `revive` tinyint(1) unsigned NOT NULL COMMENT '复活',
 `object` tinyint(1) unsigned NOT NULL COMMENT '对象',
 `party` tinyint(1) unsigned NOT NULL COMMENT '敌我',
 `usage` tinyint(1) unsigned NOT NULL COMMENT '使用方式',
`use_perm` tinyint(1) unsigned NOT NULL COMMENT '使用许可',
`charm_kind` tinyint(1) unsigned NOT NULL COMMENT '符种类', 
`rarity` tinyint(1) unsigned NOT NULL COMMENT '稀有度', 
`charm_sn` tinyint(2) unsigned NOT NULL COMMENT '符编号',
 `card_kind` varchar(40) NOT NULL COMMENT '卡牌种类',

 `card_sn` tinyint(2) unsigned NOT NULL COMMENT '卡牌编号',
 `comment` varchar(16) NOT NULL COMMENT '备注',
 `info_icon` smallint(5) unsigned NOT NULL COMMENT '情报图id',  
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='道具表';