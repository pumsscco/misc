#!/usr/bin/python
#coding=utf-8
import struct,re,glob,os.path,os,sys
import MySQLdb
sd_dir='/root/sd/'
conn=MySQLdb.connect(host='localhost',user='pal4',passwd='zuiaimengli',db='Pal4',port=3306,charset='utf8')
curs=conn.cursor()
gob_f='GameObjs.gob'
"""
功能：搜索关键标记字符串
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
        if 1<str_len<=55:
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
"""
功能：解析单个GameObjs.gob的主函数
参数：
    gob_f：gob完整路径名
返回值：
    True或False，直接将数据写入库，如果全部操作成功，则返回True，否则返回False
"""
def deco_gob(scene,section,gob_f):
    #取得文件指针及大小
    gfp=open(gob_f,'rb')
    gf_size=os.path.getsize(gob_f)
    #先搜索item标志
    gfp,si_flag=search_flags(gfp,gf_size,'item[0-9]{2,3}')
    while si_flag:
        #进入物品项内部进行分析了
        si_id=si_flag.rstrip('\x00')
        #先读模型路径出来
        model_path_len=struct.unpack('i',gfp.read(4))[0]
        si_model_path=gfp.read(model_path_len).rstrip('\x00')
        #再读模型
        model_len=struct.unpack('i',gfp.read(4))[0]
        si_model=gfp.read(model_len).rstrip('\x00')
        #贴图
        texture_len=struct.unpack('i',gfp.read(4))[0]
        si_texture=gfp.read(texture_len).rstrip('\x00')
        #XYZ座标
        si_coor_x=round(struct.unpack('f',gfp.read(4))[0],3)
        si_coor_y=round(struct.unpack('f',gfp.read(4))[0],3)
        si_coor_z=round(struct.unpack('f',gfp.read(4))[0],3)
        #将物品明细数据初始化
        si_ea_id=si_pa_id=si_num=si_money=0
        si_item={}
        si_item['SI_ITEM_MONEY']=0
        #宝箱类的情况，最多只有六个物品
        for i in range(1,7):
            si_item['SI_ITEM_'+str(i)+'_ID']=0
            si_item['SI_ITEM_'+str(i)+'_NUM']=0
        #分析模型编号
        if re.search('OM(0[789]|10)',si_model):
            #处理宝箱类型物品的内部详细情况
            #先把物品计数初始化
            item_no=0
            gfp,si_flag=search_flags(gfp,gf_size,'getitem_(id|money)|item[0-9]{2,3}')
            #循环搜索物品项或钱，碰到item标记则退出到上一层
            while si_flag and not re.search('item[0-9]{3}',si_flag):
                if 'getitem_id' in si_flag:
                    #读取箱内物品的ID及数量
                    item_id=struct.unpack('i',gfp.read(4))[0]
                    item_no+=1
                    si_item['SI_ITEM_'+str(item_no)+'_ID']=item_id
                    gfp.seek(len('PAL4_GOMTask_getitem_num')+8,os.SEEK_CUR)
                    item_num=struct.unpack('i',gfp.read(4))[0]
                    si_item['SI_ITEM_'+str(item_no)+'_NUM']=item_num
                elif 'getitem_money' in si_flag:
                    #读钱的数量
                    money=struct.unpack('i',gfp.read(4))[0]
                    si_item['SI_ITEM_MONEY']=money
                gfp,si_flag=search_flags(gfp,gf_size,'getitem_(id|money)|item[0-9]{2,3}')
        else:
            #处理非宝箱类物品
            gfp,si_flag=search_flags(gfp,gf_size,'getItem-EquipID|getitem_money')
            #处理物品为道具或装备的情形
            if 'getItem-EquipID' in si_flag:
                ea_id=struct.unpack('i',gfp.read(4))[0]
                if ea_id:
                    si_ea_id=ea_id
                gfp.seek(len('PAL4_GameObject-getItem-PropID')+8,os.SEEK_CUR)
                pa_id=struct.unpack('i',gfp.read(4))[0]
                if pa_id:
                    si_pa_id=pa_id
                gfp.seek(len('PAL4_GameObject-getItem-num')+8,os.SEEK_CUR)
                num=struct.unpack('i',gfp.read(4))[0]
                si_num=num
            #处理直接是钱的情形
            elif 'getitem_money' in si_flag:
                #读钱的数量
                money=struct.unpack('i',gfp.read(4))[0]
                si_money=money
        #构造记录的全部字段，并执行插入
        si_l=[scene.upper(),section,si_id,si_model_path,si_model,si_texture,si_coor_x,si_coor_y,si_coor_z,si_ea_id,si_pa_id,si_num,si_money,si_item['SI_ITEM_1_ID'],si_item['SI_ITEM_1_NUM'],si_item['SI_ITEM_2_ID'],si_item['SI_ITEM_2_NUM'],si_item['SI_ITEM_3_ID'],si_item['SI_ITEM_3_NUM'],si_item['SI_ITEM_4_ID'],si_item['SI_ITEM_4_NUM'],si_item['SI_ITEM_5_ID'],si_item['SI_ITEM_5_NUM'],si_item['SI_ITEM_6_ID'],si_item['SI_ITEM_6_NUM'],si_item['SI_ITEM_MONEY']]
        ins_sql="""insert into `SceneItem` (`SCENE`,`SECTION`,`SI_ID`,`SI_MODEL_PATH`,`SI_MODEL`,`SI_TEXTURE`,`SI_COOR_X`,`SI_COOR_Y`,`SI_COOR_Z`,`SI_EA_ID`,`SI_PA_ID`,`SI_NUM`,`SI_MONEY`,`SI_ITEM_1_ID`,`SI_ITEM_1_NUM`,`SI_ITEM_2_ID`,`SI_ITEM_2_NUM`,`SI_ITEM_3_ID`,`SI_ITEM_3_NUM`,`SI_ITEM_4_ID`,`SI_ITEM_4_NUM`,`SI_ITEM_5_ID`,`SI_ITEM_5_NUM`,`SI_ITEM_6_ID`,`SI_ITEM_6_NUM`,`SI_ITEM_MONEY`) values ("""+"%s, "*26
        ins_sql=ins_sql.rstrip(', ')+")"
        curs.execute(ins_sql,tuple(si_l))
        conn.commit()
        #如果前面分析物品明细时最后的搜索结果不是下一条item，则继续搜索item
        if si_flag and not re.search('item[0-9]{3}',si_flag):
            gfp,si_flag=search_flags(gfp,gf_size,'item[0-9]{2,3}')

if __name__ == '__main__':
    #取出scenedata目录下的场景目录
    for scene in sorted(os.listdir(sd_dir)):
        #再取出区块目录
        for section in sorted(os.listdir(os.path.join(sd_dir,scene))):
            #拼出游戏对象文件的完整路径，并检测其是否存在
            gob_f_path=os.path.join(sd_dir,scene,section,gob_f)
            if os.path.exists(gob_f_path):
                deco_gob(scene,section,gob_f_path)

