// RSTEncDec.h: interface for the CRSTEncDec class.
//
//////////////////////////////////////////////////////////////////////
 
#if !defined(AFX_RSTENCDEC_H__20112A8E_16B6_4E06_9829_9CB5FC1F209C__INCLUDED_)
#define AFX_RSTENCDEC_H__20112A8E_16B6_4E06_9829_9CB5FC1F209C__INCLUDED_
 
#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
 
#include "DBDecEnc.h"
 
//-------------------------------------------------------------------------------------------------------------
typedef struct  _PACKFILE_HEADER_INFO{
    DWORD   _01dwLogon; //0x1A545352 "RST"
    DWORD   _02dwUnk  ; //04
    DWORD   _03dwIndexSeek  ; //08
    DWORD   _04dwDataSeek   ; //0C
    DWORD   _05dwLenSub  ; //10
    DWORD   _06dwFileNum ; //14
    DWORD   _07dwUnk  ; //18
    DWORD   _08dwUnk  ; //1C
    DWORD   _09dwUnk  ; //20
    DWORD   _0AdwUnk  ; //24
    DWORD   _0BdwUnk  ; //28
    DWORD   _0CdwFileSize  ; //2C
    DWORD   _10dwUnk[0x14] ; //30
}_HEADER_INFO,_HEADERINFO;
 
 
class CPALFile
{
public:
    CPALFile();
    virtual ~CPALFile();
public:
    HANDLE  hOpen;
    HANDLE  hWrite;
    DWORD   m_dwCpkRead;
public:
    int       GetSize();
public:
    HANDLE    PalOpen(LPCTSTR strOpen);
    HANDLE    PalOpen(LPCTSTR strOpen,DWORD dwAccess,DWORD  dwShare,LPSECURITY_ATTRIBUTES lpSAttributes,
                      DWORD dwMode,DWORD dwFlag,HANDLE  hTemp);
    HANDLE    PalCreate(LPCTSTR strCreate);
    int       PalRead  (HANDLE hFile, LPVOID pbuf, DWORD dwlen);
    int       PalRead  (HANDLE hFile, DWORD dwSeek,LPVOID pbuf, DWORD dwlen);
    int       PalWrite (HANDLE hFile, LPVOID pbuf, DWORD dwlen);
    int       PalWrite (HANDLE hFile, DWORD dwSeek,LPVOID pbuf, DWORD dwlen);
    void      PalClose (HANDLE hFile) { ::CloseHandle(hFile); hFile=NULL; }
};
 
//-------------------------------------------------------------------------------------------------------------
typedef struct  _RST_DATA_INDEXLIST{
    DWORD   _01dwUnk;
    DWORD   _02dwUnk;
    DWORD   _03dwUnk;
    DWORD   _04dwSeek;     //文件位置
    DWORD   _05dwLenght1;  //加密后长度
    DWORD   _06dwLenght2;  //解密后长度
    DWORD   _07dwNumber;
    DWORD   _08dwEnd;
}_DATA_LIST;
 
class CRSTEncDec 
{
public:
    CRSTEncDec();
    virtual ~CRSTEncDec();
private:
    char      DecKey[0x0100];
public:
    char      m_chrData[0x02][0x1000];
public:
    int       RSTLoadKey(char *key1=NULL,char *key2=NULL,char *key3=NULL);
    int       RSTDecrpyt(LPVOID pdat,DWORD  dwnum,LPVOID pkey=NULL);
    int       RSTDecIndex(LPVOID pbuf,DWORD len);
};
 
 
class CCPKFile : public CRSTEncDec,public CDBDecEnc
{
public:
    CCPKFile();
    virtual ~CCPKFile();
public:
    CPALFile        file;
    _HEADERINFO     _hdi;
    _DATA_LIST     *_plist;
    int            m_iListNum;
    DWORD           dwFileSize;
    LPBYTE          pData;
public:
    _DATA_LIST*   GetIndexList()
    {
        return (_DATA_LIST*)pData;
    }
public:
    int   DecCPKFile(LPCTSTR strOpen,LPCTSTR strSave);
    int   DecCPKIndex(LPCTSTR strOpen);
    int   WriteData(LPCTSTR strpath);
    char* GetDecType(LPVOID pheader);
 
public:
    int   DecData (char *pdat,int len,LPCTSTR strpath);
    int   SaveFile(int num,char *pdat,int len,LPCTSTR strpath,LPCTSTR strname);
};
 
class CSMPFile : public CRSTEncDec
{
public:
    CSMPFile();
    virtual ~CSMPFile();
public:
    CPALFile        file;
    _HEADERINFO     _hdi;
    _DATA_LIST     *_plist;
    int            m_iListNum;
    DWORD           dwFileSize;
    LPBYTE          pData;
public:
    _DATA_LIST*   GetIndexList()
    {
        return (_DATA_LIST*)pData;
    }
public:
    int   DecSMPFile(LPCTSTR strOpen,LPCTSTR strSave,LPCTSTR name=NULL);
    int   DecSMPIndex(LPCTSTR strOpen);
    int   WriteData(LPCTSTR strpath,LPCTSTR name);
    char* GetDecType(LPVOID pheader);
public:
    int   SaveFile(int num,char *name);
};
 
#endif // !defined(AFX_RSTENCDEC_H__20112A8E_16B6_4E06_9829_9CB5FC1F209C__INCLUDED_)