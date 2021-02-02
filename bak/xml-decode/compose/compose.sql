drop table if exists `compose`;
CREATE TABLE `compose` (
 `id` smallint(4) unsigned NOT NULL COMMENT '编号',
 `name` varchar(8) NOT NULL COMMENT '名称',

 `material1` smallint(4) unsigned NOT NULL COMMENT '原料1',
 `quantity1` tinyint(1) unsigned NOT NULL COMMENT '数量1',
 `material2` smallint(4) unsigned NOT NULL COMMENT '原料2',
 `quantity2` tinyint(1) unsigned NOT NULL COMMENT '数量2',
 `material3` smallint(4) unsigned NOT NULL COMMENT '原料3',
 `quantity3` tinyint(1) unsigned NOT NULL COMMENT '数量3',

 `result1` smallint(4) unsigned NOT NULL COMMENT '结果1',
 `result2` smallint(4) unsigned NOT NULL COMMENT '结果2',

  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='合成表';