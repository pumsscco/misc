#!/home/py2712/bin/python2.7
#coding=utf-8
#头部的解释器是在公司服务器上调试时追加的，由于使用了外键，其实应该在建表时就追加ENGINE=“INNODB”的设定较为妥当
#__author__ = 'Pluto Chan'

import struct, binascii, sys, csv, os, os.path
import MySQLdb
#以下是数据文件所在目录及具体文件名列表
db_dir='D:\\pluto\\pal4\\'
db_list=['Pal4db.db','shopdb.db','combatDb.db']
#数据库连接信息，前一个正是公司环境
#conn=MySQLdb.connect(host='10.0.3.166',user='pal4',passwd='zuiaimengli',db='Pal4',port=3307,charset='utf8')
conn=MySQLdb.connect(host='172.17.2.172',user='pal4',passwd='zuiaimengli',db='Pal4',port=3306,charset='utf8')
#print 'db connection object: ', conn
curs=conn.cursor()
'''
功能说明：读取数据文件中的表的内容，插入到数据库中
参数说明：fp为文件指针，sect为段标志，0为简单索引表，1为复杂表
'''
def read_table(fp,sect):
    # 依据段的不同，处理方式不少差异，这里开始处理简单表
    if sect==0:
        # 先读表名的长度，再依此读表名
        tb_name_length=struct.unpack('i',fp.read(4))[0]
        tb_name=fp.read(tb_name_length)
        # 表的起始标志判定
        tb_begin_flag=binascii.hexlify(fp.read(4))
        if tb_begin_flag.upper()!='8F183201':
            print 'simple table begin flag error!'
            sys.exit(1)
        # 读表的中文名
        tb_name_length_cn=struct.unpack('i',fp.read(4))[0]
        tb_name_cn=fp.read(tb_name_length_cn).decode('gbk').encode('utf8')
        # 读记录数
        rec_num=struct.unpack('i',fp.read(4))[0]
        #以下会将读取的记录放入记录列表中
        rec_list=[]
        for j in range(rec_num):
            #先读出ID来
            id=struct.unpack('i',fp.read(4))[0]
            #再读对应的字符串内容（CONTENT）
            tmp_str_len=struct.unpack('i',fp.read(4))[0]
            cont=fp.read(tmp_str_len).decode('gbk').encode('utf8')
            rec=[id,cont]
            rec_list.append(rec)
        #读取表的结束标志，并进行判定
        tb_end_flag=binascii.hexlify(fp.read(4))
        if tb_end_flag!='90183201':
            print 'simple table end flag error!'
            sys.exit(1)
        """以下开始将表信息创建MySQL表并导入数据进去，因为是数据库操作，几乎全部进行了异常处理"""
        #先删除已有的表
        dp_tb_sql="DROP TABLE IF EXISTS `%s`" % tb_name
        try:
            curs.execute(dp_tb_sql)
            conn.commit()
        except Exception as e:
            print 'drop table %s failure' % tb_name, ' and error info is:  %s ' % e
            sys.exit(1)
        #再创建新的表
        cr_tb_sql='CREATE TABLE `%s`(`ID` INT NOT NULL PRIMARY KEY, `CONTENT` VARCHAR(512) NOT NULL) COMMENT "%s"' % (tb_name,tb_name_cn)
        try:
            curs.execute(cr_tb_sql)
            conn.commit()
        except Exception as e:
            print 'create table %s failure' % tb_name, ' and error info is:  %s ' % e
            sys.exit(1)
        #插入数据到表中
        #ins_all_rec="INSERT INTO "+tb_name+" (`ID`,`CONTENT`) VALUES ( \%d, \%s)"
        ins_all_rec="INSERT INTO "+tb_name+" VALUES ( %s, %s)"
        try:
            #print 'insert statement: ', ins_all_rec
            #print 'args: ', [tuple(rec) for rec in rec_list]
            curs.executemany(ins_all_rec,[tuple(rec) for rec in rec_list])
            conn.commit()
        except Exception as e:
            print 'error occurs when insert into simple table, and detail error info: ', e
            conn.rollback()
            sys.exit(1)
    #处理复杂表
    elif sect==1:
        #这里和简单表差不多，也是先读表名，以及表开始的判定标志，但标志内容不同
        tb_name_length=struct.unpack('i',fp.read(4))[0]
        tb_name=fp.read(tb_name_length)
        tb_begin_flag=binascii.hexlify(fp.read(4))
        if tb_begin_flag!='41183201':
            print 'complicate table begin flag error!'
            sys.exit(1)
        #这里开始比较奇特，前面是重复的表名，后面是表的中文注释（部分表的中文注释与英文表名相同）
        tb_name_length_en=struct.unpack('i',fp.read(4))[0]
        tb_name_en=fp.read(tb_name_length)
        tb_name_length_cn=struct.unpack('i',fp.read(4))[0]
        tb_name_cn=fp.read(tb_name_length_cn).decode('gbk').encode('utf8')
        #一个未知的空标志判定
        unknown_flag=binascii.hexlify(fp.read(4))
        if unknown_flag!='00000000':
            print 'unknown flag error in comp table!'
            sys.exit(1)
        #然后是字段数量及记录数量
        field_num=struct.unpack('i',fp.read(4))[0]
        rec_num=struct.unpack('i',fp.read(4))[0]
        #以下是用于存储字段的中英文名及类型列表，最后一个是外键字典
        field_list,field_cn_list=[],[]
        type_list=[]
        fk_dict={}
        #先读字段
        for i in range(field_num):
            #先读字段英文名
            fn_len=struct.unpack('i',fp.read(4))[0]
            field_name=fp.read(fn_len)
            field_list.append(field_name)
            #再读数据类型，实际上只有字符串，整型和浮点三种
            type=binascii.hexlify(fp.read(4))
            if type=='01000000':
                tp='int'
            elif type=='02000000':
                tp='str'
            elif type=='03000000':
                tp='float'
            else:
                print 'data type error in comp table'
                sys.exit(1)
            type_list.append(tp)
            #类型有可能有相关的外键表，也读出来
            fk_tb_len=struct.unpack('i',fp.read(4))[0]
            if fk_tb_len!=0:
                fk_tb=fp.read(fk_tb_len)
                fk_dict[field_name]=fk_tb
            #然后是中文名
            fn_cn_len=struct.unpack('i',fp.read(4))[0]
            fn_cn_name=fp.read(fn_cn_len).decode('gbk').encode('utf8')
            field_cn_list.append(fn_cn_name)
        #读记录列表，好在数据量不大，不然这个列表可能会引发Python报单个变量占用内存空间超标之类的报警
        rec_list=[]
        for j in range(rec_num):
            #复杂表的记录的头部标识
            rec_begin_flag=binascii.hexlify(fp.read(4))
            if rec_begin_flag.upper()!='3F183201':
                print 'record begin flag error in comp'
                sys.exit(1)
            rec=[]
            #读该条记录的每个字段
            for k in range(field_num):
                if type_list[k]=='int':
                    tmp_data=struct.unpack('i',fp.read(4))[0]
                elif type_list[k]=='str':
                    tmp_str_len=struct.unpack('i',fp.read(4))[0]
                    tmp_data=fp.read(tmp_str_len).decode('gbk').encode('utf8')
                elif type_list[k]=='float':
                    tmp_data=round(struct.unpack('f',fp.read(4))[0],4)
                rec.append(tmp_data)
            #记录结束标识
            rec_end_flag=binascii.hexlify(fp.read(4))
            if rec_end_flag!='40183201':
                print 'record end flag error in comp'
                sys.exit(1)
            rec_list.append(rec)
        #表结束标识
        tb_end_flag=binascii.hexlify(fp.read(4))
        if tb_end_flag!='42183201':
            print 'table end flag error in comp'
            sys.exit(1)
        #同样是先删除表
        dp_tb_sql="DROP TABLE IF EXISTS `%s`" % tb_name
        curs.execute(dp_tb_sql)
        #再创建表，复杂表的字段较多，只能一个个追加
        cr_tb_pre='CREATE TABLE `%s`' % tb_name
        fields_sect='('
        for l in range(field_num):
            field_def="`%s` " % field_list[l]
            #字段的类型的处理较复杂
            if type_list[l]=='int':
                field_def+=" INT "
            elif type_list[l]=='str':
                #第一个字段均为主键，但第一个字段不都是整形，因此有可能要确定的字段长度
                if l!=0:
                    field_def+=" TEXT "
                else:
                    field_def+=" VARCHAR(100) "
            elif type_list[l]=='float':
                field_def+=" FLOAT "
            #追加主键设定
            if l==0:
                    field_def+=" NOT NULL PRIMARY KEY "
            comment=" COMMENT \""+field_cn_list[l]+"\", "
            field_def+=comment
            fields_sect+=field_def
        #最后的", " 要去除
        fields_sect=fields_sect.rstrip(', ')+')'
        cr_tb=cr_tb_pre+fields_sect+' COMMENT \"'+tb_name_cn+"\""
        try:
            curs.execute(cr_tb)
            conn.commit()
            #print 'create comp table statement:  %s   finished ' % cr_tb
        except Exception as e:
            print 'error occurs in create comp table statement: ', cr_tb
            print 'create comp table %s error! detail err_info: %s' % (tb_name,e)
            sys.exit(1)
        #插入数据
        ins_all_rec="INSERT INTO "+tb_name+" VALUES ("+"%s, "*field_num
        ins_all_rec=ins_all_rec.rstrip(', ')+")"
        try:
            curs.executemany(ins_all_rec,[tuple(rec) for rec in rec_list])
            conn.commit()
            #print 'insert comp table statement:  %s   finished ' % ins_all_rec
        except Exception as e:
            print 'error occurs in insert comp table statement: ', ins_all_rec
            print 'insert comp table %s error! detail err_info: %s' % (tb_name, e)
            conn.rollback()
            sys.exit(1)
        #设置外键
        fk_sql_tpl="ALTER TABLE "+tb_name+" ADD FOREIGN KEY %s (%s) REFERENCES %s (`ID`) "
        for m in fk_dict:
            fk_sql=fk_sql_tpl % (m+'__'+fk_dict[m], m, fk_dict[m])
            try:
                curs.execute(fk_sql)
                conn.commit()
            except Exception as e:
                print 'add foreign of field %s failed,the statement is:  %s' % (m,fk_sql)
                print 'alter comp table %s error when add %s\'s fk \ndetail err_info: %s' % (tb_name,m,e)
                conn.rollback()
                sys.exit(1)
    return fp

if __name__ == '__main__':
    #打开数据库文件目录，读入文件并逐段处理
    os.chdir(db_dir)
    for db_f in db_list:
        db_fh=open(db_f,'rb')
        #先读文件头标识进行合法性判定
        file_header_length=struct.unpack('i',db_fh.read(4))[0]
        file_header=db_fh.read(file_header_length)
        if file_header!='GAME_DB_FLAG':
            print 'file header error!'
            sys.exit(1)
        #然后是段标识
        sec_flag=binascii.hexlify(db_fh.read(4))
        if sec_flag!='44183201':
            print 'sec flag error!'
            sys.exit(1)
        #循环处理两个段
        for i in range(2):
            tb_num=struct.unpack('i',db_fh.read(4))[0]
            for j in range(tb_num):
                db_fh=read_table(db_fh,i)
