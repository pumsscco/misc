//从msdata_hard.xml中，解析出各字段
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
    SN uint8 `xml:"序号,attr"`     //序号
    Name string `xml:"名称,attr"`     //名称
    Model uint16 `xml:"模型id,attr"`     //模型id
    FixEf uint16 `xml:"固有特效,attr"`     //固有特效
    HitSnd uint16 `xml:"命中音效,attr"`     //命中音效
    Script uint16 `xml:"脚本id,attr"`     //脚本id
    InfoIcon uint16 `xml:"情报图示id,attr"`     //情报图示id
    FightProf uint16 `xml:"战斗头像id,attr"`     //战斗头像id
    AIScript uint16 `xml:"ai脚本id,attr"`     //ai脚本id
    XZoom uint16 `xml:"x缩放,attr"`     //x缩放
    YZoom uint16 `xml:"y缩放,attr"`     //y缩放
    ZZoom uint16 `xml:"z缩放,attr"`     //z缩放
    EfZoom uint8 `xml:"特效缩放,attr"`     //特效缩放
    DistZoom uint8 `xml:"距离缩放,attr"`     //距离缩放
    DefAct uint16 `xml:"默认动作,attr"`     //默认动作
    RelaxAct uint8 `xml:"休闲动作,attr"`     //休闲动作
    Type uint8 `xml:"类型,attr"`     //类型  
    Race uint8 `xml:"种族,attr"`     //种族
    Seal bool `xml:"封印,attr"`     //封印
    Description string `xml:"描述,attr"`     //描述
    DivSS uint16 `xml:"占卜截图id,attr"`     //占卜截图id
    Money uint16 `xml:"钱,attr"`     //钱
    Exp uint32 `xml:"exp,attr"`     //exp
    Drop1 uint16 `xml:"掉落1id,attr"`     //掉落1id
    Drop2 uint16 `xml:"掉落2id,attr"`     //掉落2id
    Steal uint16 `xml:"偷盗id,attr"`     //偷盗id
    Charm uint16 `xml:"符,attr"`     //符
    SealDiff uint8 `xml:"封印难度,attr"`     //封印难度
    Level uint8 `xml:"等级,attr"`     //等级
    HP uint32 `xml:"hp,attr"`     //hp
    PhysicalAttack uint16 `xml:"物攻,attr"`     //物攻
    MagicAttack uint16 `xml:"仙攻,attr"`     //仙攻
    PhysicalDefense uint16 `xml:"防御,attr"`     //防御
    MagicDefense uint16 `xml:"仙防,attr"`     //仙防
    Speed uint16 `xml:"身法,attr"`     //身法
    Lucky uint8 `xml:"福缘,attr"`     //福缘
    Hitting uint8 `xml:"命中,attr"`     //命中
    Dodge uint8 `xml:"闪避,attr"`     //闪避
    Block uint8 `xml:"招架,attr"`     //招架
    Fly bool `xml:"飞行,attr"`     //飞行
    Weak uint8 `xml:"弱点属性,attr"`     //弱点属性
    Self uint8 `xml:"自身属性,attr"`     //自身属性
    PAAttr uint8 `xml:"物攻属性,attr"`     //物攻属性
    Critical uint8 `xml:"爆击率,attr"`     //爆击率
    ComboRate uint8 `xml:"连击率,attr"`     //连击率
    FreezeResist int16 `xml:"冻结抗性,attr"`     //冻结抗性
    PoisonResist int16 `xml:"中毒抗性,attr"`     //中毒抗性
    TimidResist int16 `xml:"胆怯抗性,attr"`     //胆怯抗性
    WeakResist int16 `xml:"脱力抗性,attr"`     //脱力抗性
    ManaBurnResist int16 `xml:"灼魔抗性,attr"`     //灼魔抗性
    SilentResist int16 `xml:"沉默抗性,attr"`     //沉默抗性
    ChangeResist int16 `xml:"异变抗性,attr"`     //异变抗性
    PalsyResist int16 `xml:"麻痹抗性,attr"`     //麻痹抗性
    SleepResist int16 `xml:"昏睡抗性,attr"`     //昏睡抗性
    DeathResist int16 `xml:"即死抗性,attr"`     //即死抗性
    WaterResist int16 `xml:"水抗性,attr"`     //水抗性
    FireResist int16 `xml:"火抗性,attr"`     //火抗性
    EarthResist int16 `xml:"土抗性,attr"`     //土抗性
    AirResist int16 `xml:"风抗性,attr"`     //风抗性
    ThunderResist int16 `xml:"雷抗性,attr"`     //雷抗性
    YinResist int16 `xml:"阴抗性,attr"`     //阴抗性
    YangResist int16 `xml:"阳抗性,attr"`     //阳抗性
    MstTeam1 uint16 `xml:"怪物组1,attr"`     //怪物组1
    MstTeam2 uint16 `xml:"怪物组2,attr"`     //怪物组2
    MstTeam3 uint16 `xml:"怪物组3,attr"`     //怪物组3
    Map1 uint16 `xml:"地图1,attr"`     //地图1
    Map2 uint16 `xml:"地图2,attr"`     //地图2
    Map3 uint16 `xml:"地图3,attr"`     //地图3
    Comment string `xml:"备注,attr"`     //备注
    ImpAreaL uint8 `xml:"碰撞面积长,attr"`     //碰撞面积长
    ImpAreaW uint8 `xml:"碰撞面积宽,attr"`     //碰撞面积宽
}

type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="msdata_hard"
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