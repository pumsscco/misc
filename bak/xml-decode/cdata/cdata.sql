drop table if exists `cdata`;
CREATE TABLE `cdata` (
    `id` smallint(5) unsigned NOT NULL COMMENT '编号',
    `model` smallint(5) unsigned NOT NULL COMMENT '模型id',
    `port1280` smallint(5) unsigned NOT NULL COMMENT '全身像1280',
    `name` varchar(8) NOT NULL COMMENT '名称',
    `port1440` smallint(5) unsigned NOT NULL COMMENT '全身像1440',
    `fight_prof` smallint(4) unsigned NOT NULL COMMENT '战斗头像id',
    `fight_prof2` smallint(4) unsigned NOT NULL COMMENT '战斗头像id2',
    `queue_prof` smallint(4) unsigned NOT NULL COMMENT '队列头像',
    `save_prof` smallint(4) unsigned NOT NULL COMMENT '存档头像',
    `menu_btn` smallint(4) unsigned NOT NULL COMMENT '菜单按钮',
    `bun_model` smallint(5) unsigned NOT NULL COMMENT '包子模型',
    `queue_prof_s` smallint(4) unsigned NOT NULL COMMENT '队列头像小',
    `s_prof` smallint(4) unsigned NOT NULL COMMENT '小头像',
    `queue_prof_d` smallint(4) unsigned NOT NULL COMMENT '队列头像暗',
    `prog_bar_prof` smallint(4) unsigned NOT NULL COMMENT '进度条头像',
    `prop_prof` smallint(4) unsigned NOT NULL COMMENT '道具头像',
    `assi_ef1` smallint(4) unsigned NOT NULL COMMENT '援护特效1',
    `assi_ef2` smallint(4) unsigned NOT NULL COMMENT '援护特效2',
    `n_btn` smallint(4) unsigned NOT NULL COMMENT '普通按钮',
    `n_btn_s` smallint(4) unsigned NOT NULL COMMENT '普通按钮小',
    `h_l_btn` smallint(4) unsigned NOT NULL COMMENT '高亮按钮',
    `h_l_btn_s` smallint(4) unsigned NOT NULL COMMENT '高亮按钮小',
    `shop_btn1` smallint(4) unsigned NOT NULL COMMENT '商店按钮1',
    `shop_btn2` smallint(4) unsigned NOT NULL COMMENT '商店按钮2',
    `shop_prof` smallint(4) unsigned NOT NULL COMMENT '商店头像',

    `good_magic1` smallint(4) unsigned NOT NULL COMMENT '擅长仙术1',
    `good_magic2` smallint(4) unsigned NOT NULL COMMENT '擅长仙术2',
    `good_magic3` smallint(4) unsigned NOT NULL COMMENT '擅长仙术3',

    `x_zoom` smallint(4) unsigned NOT NULL COMMENT 'x缩放',
    `y_zoom` smallint(4) unsigned NOT NULL COMMENT 'y缩放',
    `z_zoom` smallint(4) unsigned NOT NULL COMMENT 'z缩放',

    `up_script` tinyint(2) unsigned NOT NULL COMMENT '升级脚本',

    `weapon` smallint(4) unsigned NOT NULL COMMENT '武器',
    `clothes` smallint(4) unsigned NOT NULL COMMENT '衣服',
    `shoes` smallint(4) unsigned NOT NULL COMMENT '鞋子',
    `orna1` smallint(4) unsigned NOT NULL COMMENT '饰物1',
    `orna2` smallint(4) unsigned NOT NULL COMMENT '饰物2',

    `lvl` smallint(4) unsigned NOT NULL COMMENT '等级',

    `strength` float NOT NULL COMMENT '力',
    `vitality` float NOT NULL COMMENT '体',
    `speed` float NOT NULL COMMENT '速',
    `mental` float NOT NULL COMMENT '术',
    `luck` float NOT NULL COMMENT '运',

    `ini_hitting` tinyint(2) unsigned NOT NULL COMMENT '初始命中率',
    `ini_dodge` tinyint(2) unsigned NOT NULL COMMENT '初始闪避率',
    `ini_block` tinyint(2) unsigned NOT NULL COMMENT '初始格挡率',
    `ini_critical` tinyint(2) unsigned NOT NULL COMMENT '初始爆击率',
    `ini_combo_rate` tinyint(2) unsigned NOT NULL COMMENT '初始连击率',

    `freeze_resist` tinyint(2) unsigned NOT NULL COMMENT '冻结抗性',
    `poison_resist` tinyint(2) unsigned NOT NULL COMMENT '中毒抗性',
    `chaos_resist` tinyint(2) unsigned NOT NULL COMMENT '混乱抗性',
    `weak_resist` tinyint(2) unsigned NOT NULL COMMENT '脱力抗性',
    `silent_resist` smallint(3) unsigned NOT NULL COMMENT '沉默抗性',
    `change_resist` smallint(3) unsigned NOT NULL COMMENT '异变抗性',
    `palsy_resist` smallint(3) unsigned NOT NULL COMMENT '麻痹抗性',
    `sleep_resist` smallint(3) unsigned NOT NULL COMMENT '昏睡抗性',
    `passive_resist` tinyint(2) unsigned NOT NULL COMMENT '消极抗性',
    `foul_resist` tinyint(2) unsigned NOT NULL COMMENT '污浊抗性',
    `death_resist` smallint(3) unsigned NOT NULL COMMENT '即死抗性',

    `water_resist` smallint(3) unsigned NOT NULL COMMENT '水抗性',
    `fire_resist` smallint(3) NOT NULL COMMENT '火抗性',
    `earth_resist` smallint(3) NOT NULL COMMENT '土抗性',
    `air_resist` smallint(3) NOT NULL COMMENT '风抗性',
    `thunder_resist` smallint(3) NOT NULL COMMENT '雷抗性',
    `yin_resist` smallint(3) NOT NULL COMMENT '阴抗性',

    `water_prac_inc` smallint(3) NOT NULL COMMENT '水修为增量',
    `fire_prac_inc` smallint(3) NOT NULL COMMENT '火修为增量',
    `earth_prac_inc` smallint(3) NOT NULL COMMENT '土修为增量',
    `air_prac_inc` smallint(3) NOT NULL COMMENT '风修为增量',
    `thunder_prac_inc` smallint(3) NOT NULL COMMENT '雷修为增量',
    `yin_prac_inc` smallint(3) NOT NULL COMMENT '阴修为增量',
    `yang_prac_inc` smallint(3) NOT NULL COMMENT '阳修为增量',

    `water_prac` smallint(3) NOT NULL COMMENT '水修为',
    `fire_prac` smallint(3) NOT NULL COMMENT '火修为',
    `earth_prac` smallint(3) NOT NULL COMMENT '土修为',
    `air_prac` smallint(3) NOT NULL COMMENT '风修为',
    `thunder_prac` smallint(3) NOT NULL COMMENT '雷修为',
    `yin_prac` smallint(3) NOT NULL COMMENT '阴修为',
    `yang_prac` smallint(3) NOT NULL COMMENT '阳修为',

    `water_add` tinyint(2) unsigned NOT NULL COMMENT '水加成',
    `fire_add` tinyint(2) unsigned NOT NULL COMMENT '火加成',
    `earth_add` tinyint(2) unsigned NOT NULL COMMENT '土加成',
    `air_add` tinyint(2) unsigned NOT NULL COMMENT '风加成',
    `thunder_add` tinyint(2) unsigned NOT NULL COMMENT '雷加成',
    `yin_add` tinyint(2) unsigned NOT NULL COMMENT '阴加成',
    `yang_add` tinyint(2) unsigned NOT NULL COMMENT '阳加成',

    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='主角信息表';