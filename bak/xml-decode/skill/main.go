//从skill.xml中，解析出各字段
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
    Ef uint16 `xml:"特效id,attr"`     //特效id
    Icon uint16 `xml:"图标id,attr"`     //图标id
    Script uint16 `xml:"脚本id,attr"`     //脚本id
    Name string `xml:"名称,attr"`     //名称
    Desc string `xml:"描述,attr"`     //描述
    Type uint8 `xml:"类型,attr"`     //类型
    Loc uint8 `xml:"位置,attr"`     //位置
    Attr uint8 `xml:"属性,attr"`     //属性
    Fend bool `xml:"击退,attr"`     //击退
    ShortPerm bool `xml:"快捷许可,attr"`     //快捷许可
    ProfReq uint16 `xml:"修为要求,attr"`     //修为要求
    TrumpReq bool `xml:"法宝需求,attr"`     //法宝需求
    CondStat uint8 `xml:"条件状态,attr"`     //条件状态
    Role uint16 `xml:"角色,attr"`     //角色
    EnvEf bool `xml:"环境影响,attr"`     //环境影响
    MP uint8 `xml:"mp,attr"`     //mp
    Summon uint8 `xml:"召唤值,attr"`     //召唤值
    FightWill uint8 `xml:"斗志,attr"`     //斗志
    Power float32 `xml:"威力,attr"`     //威力
    Object uint8 `xml:"对象,attr"`     //对象
    Party uint8 `xml:"敌我,attr"`     //敌我
    Renew uint8 `xml:"回气,attr"`     //回气
    ToAir bool `xml:"对飞行,attr"`     //对飞行
    Usage uint8 `xml:"使用方式,attr"`     //使用方式
    UsePerm uint8 `xml:"使用许可,attr"`     //使用许可
    Revive bool `xml:"复活,attr"`     //复活
    Comment string `xml:"备注,attr"`     //备注
}
type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="skill"
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
            case reflect.Uint8,reflect.Uint16:
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