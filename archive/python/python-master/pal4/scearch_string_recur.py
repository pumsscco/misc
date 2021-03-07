#!/usr/bin/python
#coding=utf-8
import struct,re,glob,os.path,os,sys
import MySQLdb
pal4_dir='/root/pal4/'
conn=MySQLdb.connect(host='localhost',user='pal4',passwd='zuiaimengli',db='Pal4',port=3306,charset='utf8')
curs=conn.cursor()
gob_f='GameObjs.gob'
"""
功能：搜索关键标字符串
参数：
    fp：文件指针
    pattern：字符串正则表达式
    f_size：文件大小
返回值：
    fp：文件指针
    flag_str：匹配的字符串
"""
def search_flags(fp,f_size,pattern):
    #先保存当前指针位置
    fp_old=fp.tell()
    while fp.tell()<f_size-4:
        #读字符串长度
        str_len=struct.unpack('i',fp.read(4))[0]
        #选择可能的最长的标记串长度进行处理，对于不匹配字符串模式的，以及长度超标的，指针跳回原指针的下一个位置重读
        if 1<str_len<=255:
            ret_str=fp.read(str_len)
            if re.search(pattern,ret_str):
                return fp,ret_str
            else:
                fp_old+=1
                fp.seek(fp_old)
        else:
            fp_old+=1
            fp.seek(fp_old)
    else:
        return None,None

if __name__ == '__main__':
    #取出scenedata目录下的场景目录
    for f in glob.glob(pal4_dir+'*/*.*'):
        f_size=os.path.getsize(f)
        fp,_=search_flags(fp,f_size,'昆仑琼华派')
        print '文件名：%s,字符串所在地址: %d' (f,hex(fp.tell()))

