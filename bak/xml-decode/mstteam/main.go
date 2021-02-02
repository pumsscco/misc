//从mstteam.xml中，解析出各字段
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
    ShopScript uint16 `xml:"商店脚本,attr"`     //商店脚本
    BeginScript uint16 `xml:"开始脚本,attr"`     //开始脚本
    EndScript uint16 `xml:"结束脚本,attr"`     //结束脚本
    FailScript uint16 `xml:"失败脚本,attr"`     //失败脚本
    TitleScript uint16 `xml:"称号脚本,attr"`     //称号脚本
    EscRate uint8 `xml:"逃跑成功率,attr"`     //逃跑成功率
    Mst1 uint16 `xml:"怪物1,attr"`     //怪物1
    Mst2 uint16 `xml:"怪物2,attr"`     //怪物2
    Mst3 uint16 `xml:"怪物3,attr"`     //怪物3
    Mst4 uint16 `xml:"怪物4,attr"`     //怪物4
    Mst5 uint16 `xml:"怪物5,attr"`     //怪物5
    Loc1 uint8 `xml:"位置1,attr"`     //位置1
    Loc2 uint8 `xml:"位置2,attr"`     //位置2
    Loc3 uint8 `xml:"位置3,attr"`     //位置3
    Loc4 uint8 `xml:"位置4,attr"`     //位置4
    Loc5 uint8 `xml:"位置5,attr"`     //位置5
    RotAngle uint8 `xml:"旋转角度,attr"`     //旋转角度
    Challenge bool `xml:"挑战,attr"`     //挑战
    Compose string `xml:"组成,attr"`     //组成
    Wander uint8 `xml:"游荡模型,attr"`     //游荡模型  
    Comment string `xml:"备注,attr"`     //备注
    Field1 string `xml:"field1,attr"`     //field1
}
type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="mstteam"
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