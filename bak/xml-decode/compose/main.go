//从compose.xml中，解析出各字段
package main
import (
	"encoding/xml"
	"io/ioutil"
    "log"
    "database/sql"
    "reflect"
    _ "github.com/go-sql-driver/mysql"
)
type Row struct {
    Id uint16 `xml:"编号,attr"`     //编号
    Name string `xml:"名称,attr"`     //名称

    Material1 uint16 `xml:"原料1,attr"`     //原料1
    Quantity1 uint8 `xml:"数量1,attr"`     //数量1  
    Material2 uint16 `xml:"原料2,attr"`     //原料2
    Quantity2 uint8 `xml:"数量2,attr"`     //数量2
    Material3 uint16 `xml:"原料3,attr"`     //原料3
    Quantity3 uint8 `xml:"数量3,attr"`     //数量3

    Result1 uint16 `xml:"结果1,attr"`     //结果1
    Result2 uint16 `xml:"结果2,attr"`     //结果2
}
type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="compose"
    db, _ := sql.Open("mysql", "pal5q:DJzwQCjJAeC5JUYVhLpc@/pal5q")
    defer db.Close()
    content,_:=ioutil.ReadFile("/home/pluto/tmp/dest/"+table+".xml")
    w:=Data{}
    err:=xml.Unmarshal([]byte(content),&w)
    if err!=nil {
        log.Fatal(err)
    }
    rs:=len(w.Row)
    vf:=reflect.ValueOf(w.Row[0])
    fs:=vf.NumField()
    all:=[]interface{}{}
    for i:=0;i<rs;i++ {
        r:=reflect.ValueOf(w.Row[i])
        for j:=0;j<fs;j++ {
            f:=r.Field(j)
            switch f.Kind() {
            case reflect.Uint8,reflect.Uint16:
                all=append(all,f.Uint())
            case reflect.String:
                all=append(all,f.String())
            case reflect.Bool:
                all=append(all,f.Bool())
            }
        }
    }
    //log.Print(all)
    //insert all recs into table
    insertSql := "INSERT INTO `"+table+"` VALUES "
    for range w.Row {
        insertSql+="("
        for m:=0;m<fs;m++ {
            insertSql+="?,"
        }
        insertSql=insertSql[:len(insertSql)-1]+"),"
    }
    insertSql = insertSql[:len(insertSql)-1]
    //log.Print(insertSql)
    result,err:=db.Exec(insertSql,all...)
    if err!=nil {
        log.Fatal(err)
    } else {
        log.Print(result)
    }
}