// RSTEncDec.cpp: implementation of the CRSTEncDec class.
//
//////////////////////////////////////////////////////////////////////
 
#include "stdafx.h"
#include "Pal4DecPack.h"
#include "RSTEncDec.h"
 
#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif
 
//-----------------------------------------------------------------------------------------------------------------
 
CPALFile::CPALFile()
{
    hOpen =NULL;
    hWrite=NULL;
 
    m_dwCpkRead=0x00;
}
CPALFile::~CPALFile()
{
}
 
int   CPALFile::GetSize(){ return ::GetFileSize(hOpen,NULL); }
 
HANDLE CPALFile::PalOpen(LPCTSTR strOpen,DWORD  dwAccess,DWORD  dwShare,LPSECURITY_ATTRIBUTES lpSAttributes,
                      DWORD dwMode,DWORD dwFlag,HANDLE  hTemp)
{
    hOpen=::CreateFile(strOpen,dwAccess,dwShare,lpSAttributes,
                        dwMode,dwFlag,hTemp);
    return hOpen;
}
 
HANDLE CPALFile::PalOpen(LPCTSTR strOpen)
{
    hOpen=::CreateFile(strOpen,
                     GENERIC_READ,
                     FILE_SHARE_READ,
                     NULL,
                     OPEN_EXISTING,
                     FILE_ATTRIBUTE_NORMAL,
                     NULL);
    return hOpen;
}
 
HANDLE CPALFile::PalCreate(LPCTSTR strCreate)
{
    hWrite=CreateFile(strCreate,
                    GENERIC_READ|GENERIC_WRITE,
                    FILE_SHARE_READ|FILE_SHARE_WRITE,
                    NULL,
                    CREATE_NEW,
                    FILE_ATTRIBUTE_NORMAL,
                    NULL);
   if(hWrite==INVALID_HANDLE_VALUE)
    {
        hWrite=CreateFile(strCreate,
            GENERIC_READ|GENERIC_WRITE,
            FILE_SHARE_READ|FILE_SHARE_WRITE,
            NULL,CREATE_ALWAYS,FILE_ATTRIBUTE_NORMAL,NULL);
        if(hWrite==INVALID_HANDLE_VALUE)
        {
            return NULL;
        }
    }
    return hWrite;
}
 
int CPALFile::PalRead(HANDLE hFile, LPVOID pbuf, DWORD dwlen)
{
    int iRe=ReadFile(hFile,pbuf,dwlen,&m_dwCpkRead,NULL);
 
    int result = iRe==0x01;
 
    if(dwlen != m_dwCpkRead){ result=0; }
    return result;
}
 
int CPALFile::PalRead(HANDLE hFile,DWORD dwSeek, LPVOID pbuf, DWORD dwlen)
{
    OVERLAPPED oap;
    memset(&oap,0x00,sizeof(OVERLAPPED));
    oap.Offset=dwSeek;
    int iRe=ReadFile(hFile,(LPBYTE)pbuf,dwlen,&m_dwCpkRead,&oap);
 
    if(dwlen != m_dwCpkRead){ return m_dwCpkRead; }
    return dwlen;
}
 
int CPALFile::PalWrite(HANDLE hFile, LPVOID pbuf, DWORD dwlen)
{
    int iRe=::WriteFile(hFile,pbuf,dwlen,&m_dwCpkRead,NULL);
 
    int result = iRe==0x01;
 
    if(dwlen != m_dwCpkRead){ result=0; }
    return result;
}
 
int CPALFile::PalWrite(HANDLE hFile,DWORD dwSeek, LPVOID pbuf, DWORD dwlen)
{
    OVERLAPPED oap;
    memset(&oap,0x00,sizeof(OVERLAPPED));
    oap.Offset=dwSeek;
    int iRe=::WriteFile(hFile,(LPBYTE)pbuf,dwlen,&m_dwCpkRead,&oap);
     
    if(dwlen != m_dwCpkRead){ return m_dwCpkRead; }
    return dwlen;
}
 
 
 
 
//---------------------------------------------------------------------------------------------------------------
 
 
 
//---------------------------------------------------------------------------------------------------------------
char    szVampire[0x10] ="Vampire.C.J at ";
char    szTechn  [0x20] ="Softstar Technology (ShangHai)";
char    szCoLtd  [0x10] =" Co., Ltd";
 
DWORD   FILE_LOGON=0x1A545352; //"RST"
 
//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////
 
CRSTEncDec::CRSTEncDec()
{
    memset(DecKey,0x00,0x0100);
}
 
CRSTEncDec::~CRSTEncDec()
{
 
}
 
int       CRSTEncDec::RSTLoadKey(char *key1,char *key2,char *key3)
{
    memset(DecKey,0x00,0x100);
    if(key1==NULL||key2==NULL||key3==NULL)
    {
        strcpy(DecKey,szVampire);
        strcat(DecKey,szTechn);
        strcat(DecKey,szCoLtd);
    }else{
        strcpy(DecKey,key1);
        strcat(DecKey,key2);
        strcat(DecKey,key3);
    }
 
    return 0;
}
 
int       CRSTEncDec::RSTDecrpyt(LPVOID pdat,DWORD  dwnum,LPVOID pkey)
{
    DWORD   dwedx;
    DWORD   dweax;
    DWORD   dwebp;
    DWORD   dwebx = dwnum;
    if(dwebx < 0x02) { return -1; }
 
    if(pkey==NULL){pkey=(LPVOID)&DecKey[0];}
 
    LPDWORD  pdwdat=(LPDWORD)pdat;
    LPDWORD  pdwkey=(LPDWORD)pkey;
 
    DWORD    dwesi=pdwdat[0];
 
    DWORD    esp10=dwebx;
    DWORD    esp14=0x00;
 
    dweax=(DWORD)floor( (double)( 52.00f / (float)esp10 + 6.00f) ) * 0x9E3779B9;
    esp10=dweax;
 
    if(dweax != 0x00)
    {
        do{
            DWORD   dwecx= dweax;
            DWORD   esp1c=(dwecx / 0x04) & 0x03;
 
            dwecx = dwebx -0x01;
 
            if(dwecx > 0x00)
            {
                do{
                    dwedx =pdwdat[dwecx -0x01];
                    dwebx =dwesi * 0x04;
 
                    dweax =dwedx;
                    dwebp =dwedx;
 
                    dweax /= 0x20;
                    dwebx ^= dweax;
                    dweax  =dwesi;
                    dweax /= 0x08;
                    dwebp *= 0x10;
                    dweax ^= dwebp;
                    dwebp  =esp1c;
 
                    dwebx +=dweax;
                    dweax  =dwecx;
                    dweax &=0x03;
                    dweax ^=dwebp;
                    dwebp  =pdwkey[dweax];
                    dweax  =esp10;  //esp+10
                    dwebp ^=dwedx;
                    dwedx  =dweax;
                    dwedx ^=dwesi;
                    dwesi  =pdwdat[dwecx];
                    dwebp +=dwedx;
                    dwebx ^=dwebp;
                    dwesi -=dwebx;
 
                    pdwdat[dwecx] =dwesi;
                    dwecx--;
 
                }while(dwecx);
 
                dwebx = dwnum;
            }
                dwebx = pdwdat[dwebx-1];
                dwedx = dwesi * 0x04;
                dwebp = dwebx;
 
                dwecx &= 0x03;
                dwebp /= 0x20;
                dwedx ^= dwebp;
                dwebp  = dwesi;
                dwebp /= 0x08;
                dwebx *= 0x10;
                dwebp ^= dwebx;
 
                dwebx  = esp1c;
                dwecx ^= dwebx;
                dwedx += dwebp;
 
                dwecx  = pdwkey[dwecx];
                dwebx  = dwnum;
                dwebp  = pdwdat[dwebx-1];
 
                dwecx ^=dwebp;
                dwebp  =dweax;
                dwebp ^=dwesi;
                dwesi  =pdwdat[0];
                dwecx +=dwebp;
                dwedx ^=dwecx;
                dwesi -=dwedx;
                dweax +=0x61C88647;
                pdwdat[0] =dwesi;
                esp10  =dweax;
        }while(dweax);
    }
 
    return 0;
}
 
 
int       CRSTEncDec::RSTDecIndex(LPVOID pbuf,DWORD len)
{
    LPBYTE  pbybuf1=(LPBYTE)pbuf;
    LPBYTE  pbybuf2=&pbybuf1[len-0x1000];
 
    if(len>0x2000)
    {
        RSTLoadKey();
        memset(m_chrData[0x00],0x00,0x1000);
        memset(m_chrData[0x01],0x00,0x1000);
 
        int num=0;
        do{
            memcpy(&m_chrData[0x00][num],&pbybuf1[num],0x08);
            memcpy(&m_chrData[0x01][num + 0x04],&pbybuf2[num -0x01 ],0x08);
            num += 0x08;
        }while(num<0x1000);
 
        RSTDecrpyt( &m_chrData[0x00][0x00],0x0400,DecKey);
        RSTDecrpyt( &m_chrData[0x01][0x04],0x0400,DecKey);
 
        int n=0;
 
        do{
            memcpy(&pbybuf1[n],&m_chrData[0x00][n],0x08);
            memcpy(&pbybuf2[n -0x01 ],&m_chrData[0x01][n + 0x04],0x08);
 
            n++;
            num--;
        }while(num);
 
        return 1;
    }
    return 0;
}
 
 
//----------------------------------------------------------------------------------------------------------------------
 
 
CCPKFile::CCPKFile()
{
    _plist     = NULL;
    m_iListNum = 0;
    dwFileSize = 0;
    pData      = NULL;
    memset(&_hdi,0x00,sizeof(_HEADER_INFO));
}
 
CCPKFile::~CCPKFile()
{
    if(pData!=NULL)
    {
        //删除内存分配
        delete [] pData; pData=NULL;
    }
 
    if(file.hOpen != NULL)
    {
        file.PalClose(file.hOpen);
        file.hOpen =NULL;
    }
}
 
int   CCPKFile::DecCPKFile(LPCTSTR strOpen,LPCTSTR strSave)
{
    if(pData==NULL)
    {
        //分配内存
        pData = new BYTE[0x100000];
    }else{ memset(pData,0x00,0x100000);}
 
    HANDLE  hOpen=file.PalOpen(strOpen);
    if(hOpen==INVALID_HANDLE_VALUE) {return -1;}
 
    //获取文件大小
    dwFileSize=::GetFileSize(hOpen,NULL);
 
    //读取索引头
    DecCPKIndex(strOpen);
 
    CString ss=strSave;
    ss +="index.bin";
    HFILE   hf=::_lcreat(ss,NULL);
    ::_lwrite(hf,(LPCTSTR)pData,0x100000);
    ::_lclose(hf);
 
    //写文件:
    WriteData(strSave);
 
    //清除句柄:
    if(file.hOpen != NULL)
    {
        file.PalClose(file.hOpen);
        file.hOpen =NULL;
    }
 
    if(file.hWrite != NULL)
    {
        file.PalClose(file.hWrite);
        file.hWrite =NULL;
    }
 
    delete [] pData;
 
    return 0;
}
 
int    CCPKFile::DecCPKIndex(LPCTSTR strOpen)
{
    memset(&_hdi,0x00,sizeof(_HEADER_INFO));
    file.PalRead(file.hOpen,&_hdi,sizeof(_HEADER_INFO));
 
    m_iListNum=_hdi._06dwFileNum;
 
    if(_hdi._01dwLogon == FILE_LOGON)
    {
        if(file.PalRead(file.hOpen,pData,_hdi._05dwLenSub*0x20)!=0)
        {
            int re=RSTDecIndex(pData,0x100000);
            _plist=GetIndexList();
            return re;
        }
    }
 
    return 0;
}
 
char*   CCPKFile::GetDecType(LPVOID pheader)
{
    DWORD  dwType=(*(LPDWORD)pheader & 0x00FFFFFF);
 
    if(strcmp((char*)&dwType,"BIK")==0x00){ return "BIK";}
 
    return "unk";
}
 
int     CCPKFile::WriteData(LPCTSTR strpath)
{
    if(dwFileSize<=0x100000){return -1;}
    int     size  = dwFileSize -0x100000;
    int     rsize = 0x100000;
    int     seek  = 0x100000;
     
    char    ss  [MAX_PATH] = {0};
 
    theApp.m_Dlg->AddLog("分配内存 ...!",0x01);
    LPBYTE  pbuf = new BYTE[size];
 
    int     num  = size/0x100000;
    if( size<0x100000 ){ rsize=size; }
    if( (size%0x100000)>0x00 ){ num++; }
     
    //循环读取文件
    do{
        int iRe = file.PalRead(file.hOpen,seek,pbuf +(seek - 0x100000),rsize);
        seek += rsize;
 
        wsprintf(ss,"(%d)装载文件: %d / %d",num,seek - 0x100000 ,size);
        theApp.m_Dlg->AddLog(ss,0x01);
        theApp.m_Dlg->m_pgsLog.SetPos( ((seek/0x1000)*100) /(dwFileSize/0x1000) );
 
        if( (dwFileSize-seek)<0x100000){ rsize = dwFileSize - seek; }
        num--;
    }while(num);
     
    theApp.m_Dlg->AddLog("读取完成,解密文件 ...!",0x01);
     
    //保存文件
    DecData((char*)pbuf,size,strpath);
 
    delete [] pbuf;
 
    return 0;
}
 
int     CCPKFile::DecData(char *pdat,int len,LPCTSTR strpath)
{
    char   ss[MAX_PATH] = {0};
    strcpy(ss,strpath);
 
    for( int num = 0 ; num < m_iListNum ; num++ )
    {  
        int   size        =_plist[num]._05dwLenght1;
        int   seek        =_plist[num]._04dwSeek   -0x100000;
        char*  psrc = pdat + seek;
 
        if(_plist[num]._05dwLenght1==0x00&&_plist[num]._06dwLenght2 == 0x00)
        {
            wsprintf(ss,"%s%s",strpath,(char*)(psrc+size));
            ::CreateDirectory(ss,NULL);
            strcpy(ss,strpath);
            continue;
        }
 
        DWORD   dstlen=0x00;
        if(_plist[num]._06dwLenght2 <= 0x1000) { dstlen=0x1000; }
        if(_plist[num]._06dwLenght2 >  0x1000) { dstlen=(_plist[num]._06dwLenght2/0x1000)*0x1000 + 0x1000 ;}
 
        char*  pdst = new char[dstlen];
 
        if(_plist[num]._05dwLenght1 != _plist[num]._06dwLenght2)
        {
            int iRe=DBDecrpyt(psrc,size,pdst,&dstlen,0x00);
            SaveFile(num,pdst,dstlen,ss,(char*)(psrc+size));
        }else{
            SaveFile(num,psrc,size,ss,(char*)(psrc+size));
        }
 
        delete [] pdst;
    }
    return 0;
}
 
int     CCPKFile::SaveFile(int num,char *pdat,int len,LPCTSTR strpath,LPCTSTR strname)
{
    char    ss  [MAX_PATH] = {0};
    char    path[MAX_PATH] = {0};
 
    wsprintf(path,"%s\\%s",strpath,strname);
    if(file.PalCreate(path)<0)
    {
        wsprintf(ss,"(%d)创建文件[%02X]<0x%08X>:%s  ...创建错误!",
                num,_plist[num]._07dwNumber,_plist[num]._04dwSeek,strname);
 
        theApp.m_Dlg->AddLog(ss);
        return 0;
    }
 
    wsprintf(ss,"(%d)创建文件[%02X]<0x%08X>:%s  ...创建成功!",
            num,_plist[num]._07dwNumber,_plist[num]._04dwSeek,strname);
    theApp.m_Dlg->AddLog(ss);
 
    if( len > 0x00)
    {
        int wlen=0x1000;
        int size=0x00;
        int n = len / 0x1000;
        if( len<0x1000 ){ wlen=len; }
        if( (len % 0x1000)> 0x00 ){ n++; }
 
        do{
            file.PalWrite (file.hWrite,pdat+size,wlen);
            size += wlen;
             
            int p=100;
            if(size > 0x00) {
            if((size/0x1000)>0x00){ p= ((size /0x1000) *100)/ (len /0x1000);}
            }
 
            wsprintf(ss,"(%d)%s: (%d/%d) [%s%d]",
                    num,strname,size ,len ,"%",p);
            theApp.m_Dlg->AddLog(ss,0x01);
            theApp.m_Dlg->m_pgsLog.SetPos( p );
 
            if( (len-size) <0x1000 && (len-size)>0x00 ) { wlen= len-size;}
            if( (len-size) <0x00 ){break;}
            n--;
        }while(n);
    }
 
    file.PalClose(file.hWrite); file.hWrite=NULL;
    return 1;
}
 
/*
 
int     CCPKFile::WriteData(LPCTSTR strpath)
{
    char    path[MAX_PATH] = {0};
    char    ss  [MAX_PATH] = {0};
 
    for(int num =0; num < m_iListNum; num++)
    {
        BYTE    pdat[0x10]={0};
 
        int iRe=file.PalRead(file.hOpen,_plist[num]._04dwSeek,pdat,0x10); if(iRe<0){ break; }
 
        wsprintf(path,"%sPAL4_Dec_%02X.%s",strpath,num,GetDecType(pdat));
        if(file.PalCreate(path)<0)
        {
            wsprintf(ss,"(%d)创建文件[%02X]<0x%08X>:PAL4_Dec_%02X.%s  ...创建错误!",
                num,_plist[num]._07dwNumber,_plist[num]._04dwSeek,num,GetDecType(pdat));
 
            theApp.m_Dlg->AddLog(ss);
            continue;
        }
        wsprintf(ss,"(%d)创建文件[%02X]<0x%08X>:PAL4_Dec_%02X.%s  ...创建成功!",
                num,_plist[num]._07dwNumber,_plist[num]._04dwSeek,num,GetDecType(pdat));
 
        theApp.m_Dlg->AddLog(ss);
 
        SaveFile(num,GetDecType(pdat));
 
        file.PalClose(file.hWrite); file.hWrite=NULL;
 
    }
 
    return 0;
}
 
int     CCPKFile::SaveFile(int num,char *sztype)
{
    char    pdat[0x1000]   = {0};
    char    ss  [MAX_PATH] = {0};
    int   size        =_plist[num]._05dwLenght1;
    int   seek        =_plist[num]._04dwSeek   ;
    int   len         =0;
 
    if(size>=0x1000){ len=0x1000;}else{len=size;}
 
    theApp.m_Dlg->m_pgsLog.SetPos(0);
    int  wsize=0;
 
    do{
        int  iRe=file.PalRead(file.hOpen,seek,pdat,len);if(iRe<0){break;}
        file.PalWrite (file.hWrite,pdat,iRe);
        seek  += len;
        wsize += len;
 
        int p=100;
        if(wsize > 0x00) {
            if((wsize/0x1000)>0x00){ p= ((wsize /0x1000) *100)/ (size /0x1000);}
        }
 
        wsprintf(ss,"PAL4_Dec_%02X.%s ->处理:%d/%d [%s%d]",
                num,sztype,wsize ,_plist[num]._05dwLenght1,"%",
                 p);
         
        theApp.m_Dlg->AddLog(ss,0x01);
        theApp.m_Dlg->m_pgsLog.SetPos( p );
        if((size -wsize) < 0x1000){ len=size -wsize ;}
    }while(len>0);
     
    wsprintf(ss,"(%d)处理成功:PAL4_Dec_%02X.%s ->[处理%dByte/原始%dByte]!",
        num,num,sztype,wsize,_plist[num]._05dwLenght1);
    theApp.m_Dlg->AddLog(ss,0x00);
 
    return 0;
}
*/
 
 
 
//----------------------------------------------------------------------------------------------------------------------
 
 
//----------------------------------------------------------------------------------------------------------------------
 
 
CSMPFile::CSMPFile()
{
    _plist     = NULL;
    m_iListNum = 0;
    dwFileSize = 0;
    pData      = NULL;
    memset(&_hdi,0x00,sizeof(_HEADER_INFO));
}
 
CSMPFile::~CSMPFile()
{
    if(pData!=NULL)
    {
        //删除内存分配
        delete [] pData; pData=NULL;
    }
 
    if(file.hOpen != NULL)
    {
        file.PalClose(file.hOpen);
        file.hOpen =NULL;
    }
}
 
int   CSMPFile::DecSMPFile(LPCTSTR strOpen,LPCTSTR strSave,LPCTSTR name)
{
    if(pData==NULL)
    {
        //分配内存
        pData = new BYTE[0x100000];
    }else{ memset(pData,0x00,0x100000);}
 
    HANDLE  hOpen=file.PalOpen(strOpen);
    if(hOpen==INVALID_HANDLE_VALUE) {return -1;}
 
    //获取文件大小
    dwFileSize=::GetFileSize(hOpen,NULL);
 
    //读取索引头
    DecSMPIndex(strOpen);
 
    if(name==NULL)
    {
    //写文件:
    WriteData(strSave,"PAL4_DEC");
    }else{WriteData(strSave,name);}
 
 
    //清除句柄:
    if(file.hOpen != NULL)
    {
        file.PalClose(file.hOpen);
        file.hOpen =NULL;
    }
 
    if(file.hWrite != NULL)
    {
        file.PalClose(file.hWrite);
        file.hWrite =NULL;
    }
 
    delete [] pData;
 
    return 0;
}
 
int    CSMPFile::DecSMPIndex(LPCTSTR strOpen)
{
    memset(&_hdi,0x00,sizeof(_HEADER_INFO));
    file.PalRead(file.hOpen,&_hdi,sizeof(_HEADER_INFO));
 
    m_iListNum=_hdi._06dwFileNum;
 
    if(_hdi._01dwLogon == FILE_LOGON)
    {
        if(file.PalRead(file.hOpen,pData,_hdi._05dwLenSub*0x20)!=0)
        {
            int re=RSTDecIndex(pData,0x100000);
            _plist=GetIndexList();
            return re;
        }
    }
 
    return 0;
}
 
char*   CSMPFile::GetDecType(LPVOID pheader)
{
    DWORD  dwType=(*(LPDWORD)pheader & 0x00FFFFFF);
 
    //if(strcmp((char*)&dwType,"BIK")==0x00){ return "BIK";}
 
    return "MP3";
}
 
int     CSMPFile::WriteData(LPCTSTR strpath,LPCTSTR name)
{
    char    path[MAX_PATH] = {0};
    char    ss  [MAX_PATH] = {0};
    char    cc  [MAX_PATH] = {0};
 
    RSTLoadKey();
 
    for(int num =0; num < m_iListNum; num++)
    {
        BYTE    pdat[0x10]={0};
 
        int iRe=file.PalRead(file.hOpen,_plist[num]._04dwSeek,pdat,0x10); if(iRe<0){ break; }
 
        if(num==0){wsprintf(cc,"%s.%s",name,GetDecType(pdat));}
        else{wsprintf(cc,"%s_%02X.%s",name,num,GetDecType(pdat));}
 
        wsprintf(path,"%s%s",strpath,cc);
        if(file.PalCreate(path)<0)
        {
            wsprintf(ss,"(%d)创建文件[%02X]<0x%08X>:%s  ...创建错误!",
                num,_plist[num]._07dwNumber,_plist[num]._04dwSeek,cc);
 
            theApp.m_Dlg->AddLog(ss);
            continue;
        }
        wsprintf(ss,"(%d)创建文件[%02X]<0x%08X>:%s  ...创建成功!",
                num,_plist[num]._07dwNumber,_plist[num]._04dwSeek,cc);
 
        theApp.m_Dlg->AddLog(ss);
 
        SaveFile(num,cc);
 
        file.PalClose(file.hWrite); file.hWrite=NULL;
 
    }
 
    return 0;
}
 
int     CSMPFile::SaveFile(int num,char *name)
{
    char  ss[MAX_PATH]= {0};
    int   size        =_plist[num]._05dwLenght1;
    int   seek        =_plist[num]._04dwSeek   ;
    int   len         =0;
 
    char    *pdat=new char[size];
    memset  (pdat,0x00,size);
 
    if(size>=0x1000){ len=0x1000;}else{len=size;}
 
    theApp.m_Dlg->m_pgsLog.SetPos(0);
    int  wsize=0;
    int  iRe=file.PalRead(file.hOpen,seek,pdat,size);
    if(iRe<0){return -1;}
     
    RSTDecrpyt(pdat,size /4);
 
    do{
        file.PalWrite (file.hWrite,&pdat[wsize],len);
        wsize += len;
 
        wsprintf(ss,"%s ->处理:%d/%d [%s%d]",
                name,wsize ,_plist[num]._05dwLenght1,"%",
                ((wsize/0x1000)*100)/(size/0x1000) );
         
        theApp.m_Dlg->AddLog(ss,0x01);
        theApp.m_Dlg->m_pgsLog.SetPos( ((wsize/0x1000)*100)/(size/0x1000) );
        if((size -wsize) < 0x1000){ len=size -wsize ;}
    }while(len>0);
     
    delete [] pdat;
    wsprintf(ss,"(%d)处理成功:%s ->[处理%dByte/原始%dByte]!",
        num,name,wsize,_plist[num]._05dwLenght1);
    theApp.m_Dlg->AddLog(ss,0x00);
 
    return 0;
}