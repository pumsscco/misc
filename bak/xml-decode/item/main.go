//从item.xml中，解析出各字段
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
    //XMLName xml.Name `xml:"row"`
    Id uint16 `xml:"编号,attr"`     //编号
    Pic uint16 `xml:"图示id,attr"`     //图示id
    Icon uint16 `xml:"图标id,attr"`     //图标id
    Name string `xml:"名称,attr"`     //名称
    Desc string `xml:"描述,attr"`     //描述
    Property string `xml:"作用,attr"`     //作用

    DropRate uint8 `xml:"掉落,attr"`     //掉落
    Ef uint16 `xml:"特效id,attr"`     //特效id
    Script uint16 `xml:"脚本id,attr"`     //脚本id
    Kind uint8 `xml:"种类,attr"`     //种类
    Attr uint8 `xml:"属性,attr"`     //属性
    Price uint32 `xml:"价格,attr"`     //价格
    ShortPerm bool `xml:"快捷许可,attr"`     //快捷许可
    CanDrop bool `xml:"买卖丢弃,attr"`     //买卖丢弃
    
    Revive bool `xml:"复活,attr"`     //复活
    Object uint8 `xml:"对象,attr"`     //对象
    Party uint8 `xml:"敌我,attr"`     //敌我
    Usage uint8 `xml:"使用方式,attr"`     //使用方式
    UsePerm uint8 `xml:"使用许可,attr"`     //使用许可
    CharmKind uint8 `xml:"符种类,attr"`     //符种类
    Rarity uint16 `xml:"稀有度,attr"`     //稀有度
    CharmSN uint8 `xml:"符编号,attr"`     //符编号
    CharmCnt uint8 `xml:"符计数,attr"`     //符计数
    CardKind string `xml:"卡牌种类,attr"`     //卡牌种类
    
    CardSN uint8 `xml:"卡牌编号,attr"`     //卡牌编号
    Comment string `xml:"备注,attr"`     //备注
    InfoIcon uint16 `xml:"情报图id,attr"`     //情报图id
}
type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="item"
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
            case reflect.Int8,reflect.Int16:
                all=append(all,f.Int())
            case reflect.Uint8,reflect.Uint16,reflect.Uint32:
                all=append(all,f.Uint())
            case reflect.String:
                all=append(all,f.String())
            case reflect.Bool:
                all=append(all,f.Bool())
            case reflect.Float32,reflect.Float64:
                all=append(all,f.Float())
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