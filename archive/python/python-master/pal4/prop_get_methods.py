#coding=utf-8
import MySQLdb, sys, os
#测试用道具
pa_name='毒龙胆'
pa_id=8113
conn=MySQLdb.connect(
    host='172.17.2.172', db='Pal4',
    user='pal4', passwd='zuiaimengli',
    port=3306, charset='utf8'
)
curs=conn.cursor()
'''
#先依据道具名找出ID，类别，以及属性说明
p_sql="""select ID,PA_PROPERTY,TYPE from Property
where PA_NAME = '%s'""" % pa_name
curs.execute(p_sql)
pa_id,pa_property,pa_type=curs.fetchone()
#根据道具大类表或者道具大类名称
pc_sql="""select CONTENT from PropertyClass
where ID='%s'""" % pa_type
curs.execute(pc_sql)
pc_content=curs.fetchone()[0]
print '道具ID: ',pa_id
print '道具名称： ',pa_name
print '道具属性说明： ',pa_property
print '道具大类： ',pc_content
'''
"""
函数功能：根据物品ID（装备，道具，配方均可），获得能够买到该物品的商铺信息
参数：物品ID
返回值：店铺所属区域名称，店铺名称（后续会追加附加的开放条件），目前返回值为二维数组，形式如下
[
[店铺区域，店铺类型，店铺名称]
[店铺区域，店铺类型，店铺名称]
......
[店铺区域，店铺类型，店铺名称]
]
后续可能会换成由字典构成的数组，更优雅一些
"""
def buy_source(item_id):
    #先根据商品ID查询Good表得到店铺ID列表
    g_sql="""select SHOP_ID from Good
            where GOODS_ID='%d'""" % item_id
    curs.execute(g_sql)
    shops_result=curs.fetchall()
    shop_id_list=[]
    for shop in shops_result:
        shop_id_list.append(shop[0])
    #再根据店铺ID获得店铺详细信息（区域，类型，名称）
    shop_info_list=[]
    for shop_id in shop_id_list:
        shop_info=[]
        #从ShopProperty表获取名称，位置编号，类型编号
        sp_sql="""select NAME,POSITION,TYPE from ShopProperty
             where ID='%s'""" % shop_id
        curs.execute(sp_sql)
        shop_name,shop_position,shop_type=curs.fetchone()
        #再从ShopType获取类型名称
        st_sql="""select CONTENT from ShopType
                where ID='%d'""" % shop_type
        curs.execute(st_sql)
        shop_type_name=curs.fetchone()[0]
        #从Scene表获取对应场景的所有室外区块的编号与名称
        s_sql="""select SECTION,NAME from Scene
               where TYPE=0 and SCENE='%s'""" % shop_position
        curs.execute(s_sql)
        outer_list =curs.fetchall()
        #再从Scene表中获取店铺名称对应的区块编号SECTION
        s2_sql = """select SECTION from Scene
                       where SCENE='%s' and NAME='%s'""" % (shop_position,shop_name)
        curs.execute(s2_sql)
        outer_list = curs.fetchall()
        for
        #然后组合，并追加到商铺信息表里
        shop_info=[shop_scene,shop_type_name,shop_name]
        shop_info_list.append(shop_info)
    #print  shop_info_list
    return shop_info_list

"""
函数功能：根据物品ID（装备，道具，配方均可），获得能够掉落该物品的敌人信息
参数：物品ID
返回值：敌人ID，敌人名称，目前返回值为二维数组，形式如下
[
[敌人ID，是否BOSS，敌人名称]
......
[敌人ID，是否BOSS，敌人名称]
]
后续换数组+字典模式
"""
def drop_source(item_id):
    m_sql="""select MONSTER_ID,MA_NAME,IS_BOSS from Monster
            where MDT_1_ID='%d' or MDT_2_ID='%d' or MDT_3_ID='%d' or MDT_4_ID='%d'""" % item_id
    curs.execute(m_sql)
    m_result=curs.fetchall()
    m_info_list=[]
    for monster_id,ma_name,is_boss in m_result:
        m_info_list.append([monster_id,ma_name,is_boss])
    return  m_info_list
"""
函数功能：根据物品ID（装备，道具，配方均可），获取能够偷窃到该物品的敌人信息
参数：物品ID
返回值：与物品掉落相同
"""
def steal_source(item_id):
    m_sql="""select MONSTER_ID,MA_NAME from Monster
            where CA_LOSABLE_PROPERTY='%d'""" % item_id
    curs.execute(m_sql)
    m_result=curs.fetchall()
    m_info_list=[]
    for monster_id,ma_name in m_result:
        m_info_list.append([monster_id,ma_name])
    return  m_info_list

if __name__ == '__main__':
    #shop_info_list=buy_source(pa_id)
    m_info_list=drop_source(pa_id)
    i=0
    '''for shop_info in shop_info_list:
        i+=1
        print '第%d家商铺信息： ' % i
        #这里取区域的前3个字符很蹩脚，但没什么更好的招了
        print '\t店铺所在区域： ', shop_info[0][:3]
        print '\t店铺类型名称： ', shop_info[1]
        print '\t店铺名称： ',  shop_info[2]'''
    for m_info in m_info_list:
        i+=1
        print '第%d个敌人信息： ' % i
        #这里取区域的前3个字符很蹩脚，但没什么更好的招了
        print '\t敌人ID： ', m_info[0]
        print '\t敌人名称： ', m_info[1]
        flag='是' if m_info[2]==1 else '否'
        print '\t是否BOSS： '，flag
