create table MstInfo(
    id int(11) not null auto_increment primary key,
    scene varchar(4) not null comment "场景",
    section varchar(8) not null comment "区块",
    mst_id varchar(10) not null comment "怪物组ID",
    model varchar(4) not null comment "模型",
    init_coor varchar(32) not null comment "初始坐标",
    coor2 varchar(32) not null comment "坐标2",
    fix1 tinyint(1) not null comment "第一个固定的1",
    coor3 varchar(32) not null comment "坐标3",
    mst_no tinyint(1) not null comment "怪物数量",
    mst_list varchar(32) not null comment "怪物详表",
    fix2 varchar(4) not null comment "两个固定的1",
    info varchar(1024) not null comment "详细信息"
)