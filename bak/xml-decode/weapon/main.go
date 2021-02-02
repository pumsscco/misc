//从weapon.xml中，解析出各字段
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
    ModelId uint16 `xml:"模型id,attr"`     //模型id
    ModelId2 uint16 `xml:"模型id2,attr"`     //模型id2
    IconId uint16 `xml:"图示id,attr"`     //图示id
    Texture uint16 `xml:"刀光贴图,attr"`     //刀光贴图
    Name string `xml:"名称,attr"`     //名称
    Role uint16 `xml:"角色,attr"`     //角色
    Description string `xml:"描述,attr"`     //描述
    Property string `xml:"作用,attr"`     //作用
    ActionId uint8 `xml:"动作号,attr"`     //动作号
    PhysicalAttack uint16 `xml:"物攻,attr"`     //物攻
    MagicAttack uint16 `xml:"仙攻,attr"`     //仙攻
    PhysicalDefense uint16 `xml:"防御,attr"`     //防御
    MagicDefense uint16 `xml:"仙防,attr"`     //仙防
    Speed uint8 `xml:"身法,attr"`     //身法
    Lucky uint8 `xml:"运势,attr"`     //运势
    Hitting uint8 `xml:"命中,attr"`     //命中
    Dodge uint8 `xml:"闪避,attr"`     //闪避
    Block uint8 `xml:"招架,attr"`     //招架
    Critical uint8 `xml:"爆击,attr"`     //爆击
    ComboRate uint8 `xml:"连击率,attr"`     //连击率
    Field1 string `xml:"field1,attr"`     //field1
    Attribute uint8 `xml:"属性,attr"`     //属性
    Sticks uint8 `xml:"贴符数,attr"`     //贴符数
    Price uint16 `xml:"价格,attr"`     //价格
    CanDrop bool `xml:"卖出丢弃,attr"`     //卖出丢弃
    Field2 string `xml:"field2,attr"`     //field2
    FreezeRate uint8 `xml:"冻结几率,attr"`     //冻结几率
    PoisonRate uint8 `xml:"中毒几率,attr"`     //中毒几率
    WeakRate uint8 `xml:"脱力几率,attr"`     //脱力几率
    PalsyRate uint8 `xml:"麻痹几率,attr"`     //麻痹几率
    SilentRate uint8 `xml:"沉默几率,attr"`     //沉默几率
    ChangeRate uint8 `xml:"异变几率,attr"`     //异变几率
    SleepRate uint8 `xml:"昏睡几率,attr"`     //昏睡几率
    Field3 string `xml:"field3,attr"`     //field3
    WaterAdd uint8 `xml:"水加成,attr"`     //水加成
    FireAdd uint8 `xml:"火加成,attr"`     //火加成
    EarthAdd uint8 `xml:"土加成,attr"`     //土加成
    AirAdd uint8 `xml:"风加成,attr"`     //风加成
    ThunderAdd uint8 `xml:"雷加成,attr"`     //雷加成
    YinAdd uint8 `xml:"阴加成,attr"`     //阴加成
    YangAdd uint8 `xml:"阳加成,attr"`     //阳加成
    Field4 string `xml:"field4,attr"`     //field4
    Comment string `xml:"备注,attr"`     //备注
}
type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="weapon"
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