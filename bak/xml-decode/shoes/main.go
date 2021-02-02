//从shoes.xml中，解析出各字段
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
    Icon uint16 `xml:"图示id,attr"`     //图示id
    Role uint16 `xml:"角色,attr"`     //角色  
    Description string `xml:"描述,attr"`     //描述
    Property string `xml:"作用,attr"`     //作用
    PhysicalAttack uint8 `xml:"物攻,attr"`     //物攻
    MagicAttack uint8 `xml:"仙攻,attr"`     //仙攻
    PhysicalDefense uint8 `xml:"防御,attr"`     //防御
    MagicDefense uint8 `xml:"仙防,attr"`     //仙防
    Speed uint8 `xml:"身法,attr"`     //身法
    Lucky uint8 `xml:"运势,attr"`     //运势
    Hitting uint8 `xml:"命中,attr"`     //命中
    Dodge uint8 `xml:"闪避,attr"`     //闪避
    Block uint8 `xml:"招架,attr"`     //招架
    Field1 string `xml:"field1,attr"`     //field1
    Price uint16 `xml:"价格,attr"`     //价格
    CanDrop bool `xml:"卖出丢弃,attr"`     //卖出丢弃
    Field2 string `xml:"field2,attr"`     //field2
    FreezeResist uint8 `xml:"冻结抗性,attr"`     //冻结抗性
    PoisonResist uint8 `xml:"中毒抗性,attr"`     //中毒抗性
    ManaBurnRate uint8 `xml:"灼魔几率,attr"`     //灼魔几率
    ChaosResist uint8 `xml:"混乱抗性,attr"`     //混乱抗性
    WeakResist uint8 `xml:"脱力抗性,attr"`     //脱力抗性
    PalsyResist uint8 `xml:"麻痹抗性,attr"`     //麻痹抗性
    SilentResist uint8 `xml:"沉默抗性,attr"`     //沉默抗性
    ChangeResist uint8 `xml:"异变抗性,attr"`     //异变抗性
    SleepResist uint8 `xml:"昏睡抗性,attr"`     //昏睡抗性
    PassiveResist uint8 `xml:"消极抗性,attr"`     //消极抗性
    FoulResist uint8 `xml:"污浊抗性,attr"`     //污浊抗性
    Field3 string `xml:"field3,attr"`     //field3
    WaterResist uint8 `xml:"水抗性,attr"`     //水抗性
    FireResist uint8 `xml:"火抗性,attr"`     //火抗性
    EarthResist uint8 `xml:"土抗性,attr"`     //土抗性
    AirResist uint8 `xml:"风抗性,attr"`     //风抗性
    ThunderResist uint8 `xml:"雷抗性,attr"`     //雷抗性
    YinResist uint8 `xml:"阴抗性,attr"`     //阴抗性
    YangResist uint8 `xml:"阳抗性,attr"`     //阳抗性
    Field4 string `xml:"field4,attr"`     //field4
    WaterAdd uint8 `xml:"水加成,attr"`     //水加成
    FireAdd uint8 `xml:"火加成,attr"`     //火加成
    EarthAdd uint8 `xml:"土加成,attr"`     //土加成
    AirAdd uint8 `xml:"风加成,attr"`     //风加成
    ThunderAdd uint8 `xml:"雷加成,attr"`     //雷加成
    YinAdd uint8 `xml:"阴加成,attr"`     //阴加成
    YangAdd uint8 `xml:"阳加成,attr"`     //阳加成
    Field5 string `xml:"field5,attr"`     //field5
    Comment string `xml:"备注,attr"`     //备注
}
type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="shoes"
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