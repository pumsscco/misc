#!/usr/bin/python3
'''
终极目标：将数据库中的人才，按智与武谁大，分为两组，
其中智组按智、廉、名的顺序排列，武组按武、忠、名的顺序排列，
然后对武组，先打印前10个，再打印中间20个，最后打印剩余的部分，
对智组，则是20、30、剩余
'''
import pymysql
#打印人才属性专用
def tal_info(batch_info,batch):
    print(batch_info)
    for t in batch:
        print('%s\t%s\t%s\t%s\t%s' % (t['name'],t['intelligence'],t['military'],t['honest'],t['loyalty']))
    print('-'*37)
#从mysql中获得剩余tuya key数量
m=pymysql.connect(
    host='localhost',
    user='emperor',
    password='cmke6J6p7hfUFLr5',
    db='emperor',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
cur=m.cursor()
#先处理智组
int_sql='''select name,intelligence,military,honest,loyalty 
from celebrity 
where intelligence>military 
order by intelligence,honest,name'''
cur.execute(int_sql)
int_l=cur.fetchall()
tal_info('第一批智：',int_l[:22])
tal_info('第二批智：',int_l[22:54])
tal_info('第三批智：',int_l[54:])
#再处理武组
mil_sql='''select name,intelligence,military,honest,loyalty 
from celebrity 
where intelligence<military 
order by military,loyalty,name'''
cur.execute(mil_sql)
mil_l=cur.fetchall()
tal_info('第一批武：',mil_l[:11])
tal_info('第二批武：',mil_l[11:32])
tal_info('第三批武：',mil_l[32:])
