#coding=gbk
#如果将来写入数据库，要考虑字符集转码的问题，转成MySQL默认的UTF-8，
# 对于以Django方式呈现分析结果，可能会比较理想
#__author__ = 'Pluto Chan'

import struct, binascii, sys, csv
db_f='D:\\pluto\\Pal4DbBrowser\\shopdb.db'
tb_f_dir='D:\\pluto\\Pal4DbBrowser\\'
#用于测试的文件指针位置
#装备表
#offset=0x33CDB
#敌人状态表
#offset=0x7FA
#AI类型表
#offset=0xEC
#默认读取的字节数
#def_read=4
db_fh=open(db_f,'rb')
#db_fh.seek(offset,0)

'''
函数功能：读取表的全部内容，包括字段名及全部记录，已经由简单的直接打印改为输出为CSV了，
未来规划为连接数据库，以文件中的内容为参数，直接创建表，并导入数据
函数参数：
    fp：文件指针
    sect:区段编号，1为简单表，类似索引；2为正式表，字段较多，部分表非常复杂
'''
def read_table(fp,sect):
    if sect==1:
        print '读取的是简单表'
        # 获取表名的长度
        tb_name_length=struct.unpack('i',fp.read(4))[0]
        # 获取表名
        tb_name=fp.read(tb_name_length)
        # 读取表的开始标记（虽然不太准确）
        tb_begin_flag=binascii.hexlify(fp.read(4))
        if tb_begin_flag.upper()!='8F183201':
            print '表起始标记错误'
            sys.exit(1)
        #读取表的中文名
        tb_name_length_cn=struct.unpack('i',fp.read(4))[0]
        tb_name_cn=fp.read(tb_name_length_cn)
        #读取记录数量
        rec_num=struct.unpack('i',fp.read(4))[0]
        #循环读数据记录，每行输出一条记录
        rec_list=[]
        for j in range(rec_num):
            #正式开始循环读该条记录的每个字段
            #读ID
            id=struct.unpack('i',fp.read(4))[0]
            #读内容
            tmp_str_len=struct.unpack('i',fp.read(4))[0]
            cont=fp.read(tmp_str_len)
            rec=[id,cont]
            rec_list.append(rec)
        #读表结束标志
        tb_end_flag=binascii.hexlify(fp.read(4))
        if tb_end_flag!='90183201':
            print '表结束标志错误'
            sys.exit(1)
        #将读取来的表内容单独写一个文件
        #with open(tb_f_dir+tb_name+'.csv', 'wb') as csvfile:
        with open(tb_f_dir+tb_name+'.csv', 'w') as csvfile:
            tbwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            tbwriter.writerow([tb_name_cn])
            tbwriter.writerow(['ID', 'CONTENT'])
            for rec in rec_list:
                tbwriter.writerow(rec)
    elif sect==2:
        print '读取的是复杂表'
        # 获取表名的长度
        tb_name_length=struct.unpack('i',fp.read(4))[0]
        # 获取表名
        tb_name=fp.read(tb_name_length)
        # 读取表的开始标记（虽然不太准确）
        tb_begin_flag=binascii.hexlify(fp.read(4))
        if tb_begin_flag!='41183201':
            print '表起始标记错误'
            sys.exit(1)
         #以下再次读取表的英文名，然后再读取表的中文名
        tb_name_length_en=struct.unpack('i',fp.read(4))[0]
        tb_name_en=fp.read(tb_name_length)
        tb_name_length_cn=struct.unpack('i',fp.read(4))[0]
        tb_name_cn=fp.read(tb_name_length_cn)
        # 这里固定是四个00字节，原因不明，不过似乎没有例外？！暂时认为是表名结束标识吧！
        #print '读完表中文名后的文件位置', str(hex(fp.tell())).upper().rstrip('L')
        unknown_flag=binascii.hexlify(fp.read(4))
        if unknown_flag!='00000000':
            print '表名结束标识错误！'
        #读取字段数量
        filed_num=struct.unpack('i',fp.read(4))[0]
        #读取记录数量
        rec_num=struct.unpack('i',fp.read(4))[0]
        #字段英文及中文名列表各一个
        field_list,field_cn_list=[],[]
        #先创建一个存储字段类型的列表，后续读数据用
        type_list=[]
        #循环读取字段名称，类型，及中文名
        for i in range(filed_num):
            #先读字段名
            fn_len=struct.unpack('i',fp.read(4))[0]
            field_name=fp.read(fn_len)
            field_list.append(field_name)
            #读字段类型
            type=binascii.hexlify(fp.read(4))
            if type=='01000000':
                tp='int'
            elif type=='02000000':
                tp='str'
            elif type=='03000000':
                tp='float'
            else:
                print '非法的数据类型'
                sys.exit(1)
            #将字段类型追加到列表中
            type_list.append(tp)
            #继续读外键字段
            fk_tb_len=struct.unpack('i',fp.read(4))[0]
            if fk_tb_len!=0:
                # 有外键表时，打印出来（后续可能会另外存储起来，导入数据结束时，需要追加表的外键设定）
                fk_tb=fp.read(fk_tb_len)
                print '外键表名： ', fk_tb
            #读字段的中文名
            fn_cn_len=struct.unpack('i',fp.read(4))[0]
            fn_cn_name=fp.read(fn_cn_len)
            field_cn_list.append(fn_cn_name)
        #双重循环读数据记录，每行输出一条记录
        rec_list=[]
        for j in range(rec_num):
            #每条记录的开始标志
            rec_begin_flag=binascii.hexlify(fp.read(4))
            if rec_begin_flag.upper()!='3F183201':
                print '记录起始标志错误'
                sys.exit(1)
            #正式开始循环读该条记录的每个字段
            rec=[]
            for k in range(filed_num):
                #基于具体的数据类型读取记录内容
                if type_list[k]=='int':
                    tmp_data=struct.unpack('i',fp.read(4))[0]
                elif type_list[k]=='str':
                    tmp_str_len=struct.unpack('i',fp.read(4))[0]
                    tmp_data=fp.read(tmp_str_len)
                elif type_list[k]=='float':
                    tmp_data=round(struct.unpack('f',fp.read(4))[0],4)
                rec.append(tmp_data)
            #每条记录的结束标志
            rec_end_flag=binascii.hexlify(fp.read(4))
            if rec_end_flag!='40183201':
                print '记录结束标志错误'
                sys.exit(1)
            rec_list.append(rec)
        #表结束标志
        tb_end_flag=binascii.hexlify(fp.read(4))
        if tb_end_flag!='42183201':
            print '表结束标志错误'
            sys.exit(1)
        #将读取来的表内容单独写一个文件
        #with open(tb_f_dir+tb_name+'.csv', 'wb') as csvfile:
        with open(tb_f_dir+tb_name+'.csv', 'w') as csvfile:
            tbwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            tbwriter.writerow([tb_name_cn])
            tbwriter.writerow(field_list)
            tbwriter.writerow(field_cn_list)
            for rec in rec_list:
                tbwriter.writerow(rec)
    return fp

if __name__ == '__main__':
    #读取文件头标志
    file_header_length=struct.unpack('i',db_fh.read(4))[0]
    file_header=db_fh.read(file_header_length)
    if file_header!='GAME_DB_FLAG':
        print '非法的数据文件！请使用有效的仙剑四数据文件！'
        sys.exit(1)
    #读段起始标志
    sec_flag=binascii.hexlify(db_fh.read(4))
    if sec_flag!='44183201':
        print ''
        sys.exit(1)
    #导出第一个段中的表
    tb_num_s1=struct.unpack('i',db_fh.read(4))[0]
    #print '第一个区段的表的数量', tb_num_s1
    for i in range(tb_num_s1):
        db_fh=read_table(db_fh,1)
    #导出第二个段中的表
    tb_num_s2=struct.unpack('i',db_fh.read(4))[0]
    #print '第二个区段的表的数量', tb_num_s2
    for j in range(tb_num_s2):
        db_fh=read_table(db_fh,2)
