//从cdata.xml中，解析出各字段
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
    Model uint16 `xml:"模型id,attr"`     //模型id
    Port1280 uint16 `xml:"全身像1280,attr"`     //全身像1280
    Name string `xml:"名称,attr"`     //名称
    Port1440 uint16 `xml:"全身像1440,attr"`     //全身像1440
    FightProf uint16 `xml:"战斗头像id,attr"`     //战斗头像id
    FightProf2 uint16 `xml:"战斗头像id2,attr"`     //战斗头像id2
    QueueProf uint16 `xml:"队列头像,attr"`     //队列头像
    SaveProf uint16 `xml:"存档头像,attr"`     //存档头像
    MenuBtn uint16 `xml:"菜单按钮,attr"`     //菜单按钮
    BunModel uint16 `xml:"包子模型,attr"`     //包子模型
    QueueProfS uint16 `xml:"队列头像小,attr"`     //队列头像小
    SProf uint16 `xml:"小头像,attr"`     //小头像
    QueueProfD uint16 `xml:"队列头像暗,attr"`     //队列头像暗
    ProgBarProf uint16 `xml:"进度条头像,attr"`     //进度条头像
    PropProf uint16 `xml:"道具头像,attr"`     //道具头像
    AssiEf1 uint16 `xml:"援护特效1,attr"`     //援护特效1
    AssiEf2 uint16 `xml:"援护特效2,attr"`     //援护特效2
    NBtn uint16 `xml:"普通按钮,attr"`     //普通按钮
    NBtnS uint16 `xml:"普通按钮小,attr"`     //普通按钮小
    HLBtn uint16 `xml:"高亮按钮,attr"`     //高亮按钮
    HLBtnS uint16 `xml:"高亮按钮小,attr"`     //高亮按钮小
    ShopBtn1 uint16 `xml:"商店按钮1,attr"`     //商店按钮1
    ShopBtn2 uint16 `xml:"商店按钮2,attr"`     //商店按钮2
    ShopProf uint16 `xml:"商店头像,attr"`     //商店头像

    GoodMagic1 uint16 `xml:"擅长仙术1,attr"`     //擅长仙术1
    GoodMagic2 uint16 `xml:"擅长仙术2,attr"`     //擅长仙术2
    GoodMagic3 uint16 `xml:"擅长仙术3,attr"`     //擅长仙术3

    XZoom uint16 `xml:"x缩放,attr"`     //x缩放
    YZoom uint16 `xml:"y缩放,attr"`     //y缩放
    ZZoom uint16 `xml:"z缩放,attr"`     //z缩放

    UpScript uint16 `xml:"升级脚本,attr"`     //升级脚本

    Weapon uint16 `xml:"武器,attr"`     //武器
    Clothes uint16 `xml:"衣服,attr"`     //衣服
    Shoes uint16 `xml:"鞋子,attr"`     //鞋子
    
    Strength float32 `xml:"力,attr"`     //力
    Vitality float32 `xml:"体,attr"`     //体
    Speed float32 `xml:"速,attr"`     //速
    Mental float32 `xml:"术,attr"`     //术
    Luck float32 `xml:"运,attr"`     //运

    IniHitting uint8 `xml:"初始命中率,attr"`     //初始命中率
    IniDodge uint8 `xml:"初始闪避率,attr"`     //初始闪避率
    IniBlock uint8 `xml:"初始格挡率,attr"`     //初始格挡率
    IniCritical uint8 `xml:"初始爆击率,attr"`     //初始爆击率
    IniComboRate uint8 `xml:"初始连击率,attr"`     //初始连击率

    FreezeResist int16 `xml:"冻结抗性,attr"`     //冻结抗性
    PoisonResist int16 `xml:"中毒抗性,attr"`     //中毒抗性
    ChaosResist int16 `xml:"混乱抗性,attr"`     //混乱抗性
    WeakResist int16 `xml:"脱力抗性,attr"`     //脱力抗性
    SilentResist int16 `xml:"沉默抗性,attr"`     //沉默抗性
    ChangeResist int16 `xml:"异变抗性,attr"`     //异变抗性
    PalsyResist int16 `xml:"麻痹抗性,attr"`     //麻痹抗性
    SleepResist int16 `xml:"昏睡抗性,attr"`     //昏睡抗性
    PassiveResist int16 `xml:"消极抗性,attr"`     //消极抗性
    FoulResist int16 `xml:"污浊抗性,attr"`     //污浊抗性
    DeathResist int16 `xml:"即死抗性,attr"`     //即死抗性

    WaterResist int16 `xml:"水抗性,attr"`     //水抗性
    FireResist int16 `xml:"火抗性,attr"`     //火抗性
    EarthResist int16 `xml:"土抗性,attr"`     //土抗性
    AirResist int16 `xml:"风抗性,attr"`     //风抗性
    ThunderResist int16 `xml:"雷抗性,attr"`     //雷抗性
    YinResist int16 `xml:"阴抗性,attr"`     //阴抗性

    WaterPracInc int16 `xml:"水修为增量,attr"`     //水修为增量
    FirePracInc int16 `xml:"火修为增量,attr"`     //火修为增量
    EarthPracInc int16 `xml:"土修为增量,attr"`     //土修为增量
    AirPracInc int16 `xml:"风修为增量,attr"`     //风修为增量
    ThunderPracInc int16 `xml:"雷修为增量,attr"`     //雷修为增量
    YinPracInc int16 `xml:"阴修为增量,attr"`     //阴修为增量
    YangPracInc int16 `xml:"阳修为增量,attr"`     //阳修为增量

    WaterPrac int16 `xml:"水修为,attr"`     //水修为
    FirePrac int16 `xml:"火修为,attr"`     //火修为
    EarthPrac int16 `xml:"土修为,attr"`     //土修为
    AirPrac int16 `xml:"风修为,attr"`     //风修为
    ThunderPrac int16 `xml:"雷修为,attr"`     //雷修为
    YinPrac int16 `xml:"阴修为,attr"`     //阴修为
    YangPrac int16 `xml:"阳修为,attr"`     //阳修为

    WaterAdd uint8 `xml:"水加成,attr"`     //水加成
    FireAdd uint8 `xml:"火加成,attr"`     //火加成
    EarthAdd uint8 `xml:"土加成,attr"`     //土加成
    AirAdd uint8 `xml:"风加成,attr"`     //风加成
    ThunderAdd uint8 `xml:"雷加成,attr"`     //雷加成
    YinAdd uint8 `xml:"阴加成,attr"`     //阴加成
    YangAdd uint8 `xml:"阳加成,attr"`     //阳加成
}

type Data struct {
    //XMLName xml.Name `xml:"data"`
    Row []Row `xml:"row"`
}

func main() {
    table:="cdata"
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