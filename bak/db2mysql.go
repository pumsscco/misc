/*
Analyze Pal4 db file, and insert into mysql,using goroutine with channel
*/
package main
import (
    "time"
    "encoding/binary"
    "path/filepath"
    "bytes"
    "fmt"
    "os"
    "golang.org/x/text/encoding/simplifiedchinese"
    "golang.org/x/text/transform"
    "io/ioutil"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
)
var files,_=filepath.Glob("../../learn/*.db")
var ch chan string=make(chan string,len(files))
//fuctions to get all kinds of data
func getInt(dbf *os.File) int {
    tmpS := make([]byte,4)
    dbf.Read(tmpS)
    var i int32
    binary.Read(bytes.NewReader(tmpS),binary.LittleEndian,&i)
    return int(i)
}
func getFloat(dbf *os.File)(f float32){
    tmpS := make([]byte,4)
    dbf.Read(tmpS)
    binary.Read(bytes.NewReader(tmpS),binary.LittleEndian,&f)
    return
}
func getFlag(dbf *os.File) string {
    tmpS := make([]byte,4)
    dbf.Read(tmpS)
    return fmt.Sprintf("%0X", tmpS)
}
func getEn(dbf *os.File,l int) string {
    tmpS := make([]byte,l)
    dbf.Read(tmpS)
    return string(tmpS)
}
func getChi(dbf *os.File,l int) string {
    tmpS := make([]byte,l)
    dbf.Read(tmpS)
    tmpChi,_:=ioutil.ReadAll(transform.NewReader(bytes.NewReader(tmpS), simplifiedchinese.GBK.NewDecoder()))
    return string(tmpChi)
}
//get and insert simple table
func insertSimpTable(dbf *os.File,db *sql.DB){
    type Rec struct {
        index int
        content string
    }
    tableName:=getEn(dbf,getInt(dbf))
    // skip table content start flag
    getFlag(dbf)
    tableChiName:=getChi(dbf,getInt(dbf))
    recQty:=getInt(dbf)
    recs:=make([]Rec,0)
    for j:=0;j<recQty;j++ {
        index:=getInt(dbf)
        content:=getChi(dbf,getInt(dbf))
        rec:=Rec{index,content}
        recs=append(recs,rec)
    }
    //skip table content end flag
    getFlag(dbf)
    //create table 
    createSql := "CREATE TABLE IF NOT EXISTS `"+tableName+"`(`ID` INT NOT NULL PRIMARY KEY, `CONTENT` VARCHAR(512) NOT NULL) COMMENT \""+tableChiName+"\""
    db.Exec(createSql)
    //insert all recs into table
    insertSql := "INSERT INTO `"+tableName+"` VALUES "
    vals:=[]interface{}{}
    for _, rec := range recs {
        insertSql += "(?, ?),"
        vals = append(vals, rec.index, rec.content)
    }
    insertSql = insertSql[:len(insertSql)-1]
    db.Exec(insertSql,vals...)
}
//get and insert complex table
func insertCompTable(dbf *os.File,db *sql.DB){
    type Field struct {
        name,fk,chiName string
        fType int
    }
    tableName:=getEn(dbf,getInt(dbf))
    // skip fields start flag
    getFlag(dbf)
    //skip second table english name !
    getEn(dbf,getInt(dbf))
    tableChiName:=getChi(dbf,getInt(dbf))
    // skip unknown bytes ,content is 00000000
    getFlag(dbf)
    fieldQty:=getInt(dbf)
    fields:=make([]Field,0)
    recQty:=getInt(dbf)

    //dealing with fields
    for i:=0;i<fieldQty;i++ {
        var field Field
        field.name=getEn(dbf,getInt(dbf))
        field.fType=getInt(dbf)
        fkLen:=getInt(dbf)
        if fkLen!=0 {
            field.fk=getEn(dbf,fkLen)
        } else {
            field.fk=""
        }
        field.chiName=getChi(dbf,getInt(dbf))
        fields=append(fields,field)
    }

    recs:=[][]interface{}{}
    //get records
    for j:=0;j<recQty;j++ {
        rec:=make([]interface{},0)
        //skip rec start flag
        getFlag(dbf)
        for k:=0;k<fieldQty;k++ {
            switch fields[k].fType {
                case 1:
                    rec=append(rec,getInt(dbf))
                case 2:
                    rec=append(rec,getChi(dbf,getInt(dbf)))
                case 3:
                    rec=append(rec,getFloat(dbf))
                default:
                    fmt.Println("FATAL ERROR!  field type: Uknown")
                    os.Exit(1)
            }
        }
        // rec end flag
        getFlag(dbf)
        recs=append(recs,rec)
    }
    // table content end flag
    getFlag(dbf)
    //create table 
    createSql := "CREATE TABLE `"+tableName+"`"
    fieldSect:="("
    for l,f:=range fields {
        fieldSect+="`"+f.name+"` "
        switch f.fType {
            case 1:
                fieldSect+="INT "
            case 2:
                if l!=0 {
                    fieldSect+="TEXT "
                } else {
                    fieldSect+="VARCHAR(100) "
                }
            case 3:
                fieldSect+="FLOAT "
            default:
                fmt.Println("wrong field type!")
                os.Exit(1)
        }
        if l==0 {
            fieldSect+="NOT NULL PRIMARY KEY "
        }
        fieldSect+="COMMENT \""+f.chiName+"\", "
    }
    fieldSect=fieldSect[:len(fieldSect)-2]+")"
    createSql+=fieldSect+" COMMENT \""+tableChiName+"\""
    db.Exec(createSql)
    //insert all recs into table
    insertSql := "INSERT INTO `"+tableName+"`VALUES "
    vals:=[]interface{}{}
    for _, rec := range recs {
        insertSql+="("
        for m:=0;m<len(rec);m++ {
            insertSql+="?,"
        }
        insertSql=insertSql[:len(insertSql)-1]+"),"
        vals = append(vals, rec...)
    }
    insertSql = insertSql[:len(insertSql)-1]
    db.Exec(insertSql,vals...)
    //add foreign key contraint 
    for _,fi:=range fields {
        fkSql:=""
        if fi.fk!="" {
            fkSql+="ALTER TABLE `"+tableName+"`"+" ADD FOREIGN KEY "+fi.name+"__"+fi.fk+" ("+fi.name+") REFERENCES "+fi.fk+" (`ID`)"
            db.Exec(fkSql)
        }
    }
}
//get all data for  simple  and complex table, and insert them respectively
func insertTables(file string,dbf *os.File,db *sql.DB){
    layout:="2006-01-02 15:04:05"
    start:=time.Now().Format(layout)
    //skip db flag
    getEn(dbf,getInt(dbf))

    //extract simple tables! first, skip simple table start flag
    getFlag(dbf)
    simpTableQty:=getInt(dbf)
    for i:=0;i<simpTableQty;i++ {
        insertSimpTable(dbf,db)
    }
    //extract complex table! first get complex table quantity
    compTableQty:=getInt(dbf)
    for j:=0;j<compTableQty;j++ {
        insertCompTable(dbf,db)
    }
    end:=time.Now().Format(layout)
    ch<-fmt.Sprintf("insert db file %v start at %v complete at %v",file,start,end)
}
func main() {
    db, _ := sql.Open("mysql", "golang:ktnpu9hxm27sr26g@/pal4_go")
    defer db.Close()
    for _,f:=range files {
        fp, _ := os.Open(f)
        go insertTables(f,fp,db)
    }
    for j:=0;j<len(files);j++ {
        msg:=<-ch
        fmt.Println(msg)
    }
}
