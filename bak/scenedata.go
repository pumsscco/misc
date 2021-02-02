/*
get item data from scenedata
*/
package main
import (
    "encoding/json"
    "time"
    "encoding/binary"
    "path/filepath"
    "bytes"
    "fmt"
    "os"
    "io"
    "regexp"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
)
var files,_=filepath.Glob("/home/pluto/learn/scenedata/*/*/GameObjs.gob")
var ch chan string=make(chan string,len(files))
func getInt(fp *os.File) int {
    tmpS := make([]byte,4)
    _,err:=fp.Read(tmpS)
    if err==io.EOF {
        return 0
    }
    var i int32
    binary.Read(bytes.NewReader(tmpS),binary.LittleEndian,&i)
    return int(i)
}
func getFloat(fp *os.File)(f float32){
    tmpS := make([]byte,4)
    fp.Read(tmpS)
    binary.Read(bytes.NewReader(tmpS),binary.LittleEndian,&f)
    return
}
func getFlag(fp *os.File,l int) string {
    tmpS := make([]byte,l)
    fp.Read(tmpS)
    return fmt.Sprintf("%0X", tmpS)
}
func getStr(fp *os.File,l int) string {
    tmpS := make([]byte,l)
    fp.Read(tmpS)
    return string(tmpS)
}
type gameObj struct {
    scene,sect string
    kind int
    obj,path,model,texture string
    x,y,z float32
    unknownB string
    props [][]interface{}
}
//get all game objects from one file and insert them into SceneData table
func insertGameObjs(file string,db *sql.DB) {
    layout:="2006-01-02 15:04:05"
    start:=time.Now().Format(layout)
    gobjs:=[]gameObj{}
    scene:=filepath.Base(filepath.Dir(filepath.Dir(file)))
    sect:=filepath.Base(filepath.Dir(file))
    fp,_:=os.Open(file)
    defer fp.Close()
    qty:=getInt(fp)
    //type list
    kinds:=[]int{}
    for i:=0;i<qty;i++ {
        kinds=append(kinds,getInt(fp))
    }
    for j:=0;j<qty;j++ {
        //gobj:=getGO(fp,scene,sect,types[j])
        //get obj, path, model and texture,if not empty string ,should strip the \x00 byte!
        obj:=getStr(fp,getInt(fp))
        obj=obj[:len(obj)-1]
        path:=getStr(fp,getInt(fp))
        path=path[:len(path)-1]
        model:=getStr(fp,getInt(fp))
        model=model[:len(model)-1]
        texture:=getStr(fp,getInt(fp))
        if len(texture)!=0 {
            texture=texture[:len(texture)-1]
        } else {
            texture=""
        }
        //3d location
        x:=getFloat(fp)
        y:=getFloat(fp)
        z:=getFloat(fp)
        //try skip the unknown bytes block,may be 41 bytes or 49 bytes,
        //+the first prop after this block is "PAL4-GameOject",no exception
        oldOffset1,_:=fp.Seek(0,1)
        unknownB:=getFlag(fp,41)
        l:=getInt(fp)
        if l!=15 {
            fp.Seek(oldOffset1,0)
            unknownB=getFlag(fp,49)
            l=getInt(fp)
        }
        props:=[][]interface{}{}
        props=append(props, []interface{}{getStr(fp,l),getInt(fp),getInt(fp)})
        //get the rest props
        for {
            //save offset for EOF 
            oldOffset2,_:=fp.Seek(0,1)
            propL:=getInt(fp)
            if propL==0 {
                break
            }
            prop:=getStr(fp,propL)
            if match1, _ := regexp.MatchString("^(PAL4|CSTR)", prop); match1{
                var value1 interface{}
                if match2, _ := regexp.MatchString("(name|func|launchEff)$", prop); match2{
                    value1=getStr(fp,getInt(fp))
                } else if match3, _ := regexp.MatchString("(time|scale|X|Y|Z|amplitude|frequency|maxval|minval|effDuration|effTime|effHurt|tMax|tMin|thrust|directDist|suction)$", prop); match3 {
                    value1=fmt.Sprintf("%.5g",getFloat(fp))
                } else {
                    value1=getInt(fp)
                }
                value2:=getInt(fp)
                props=append(props, []interface{}{prop,value1,value2})
            } else {
                fp.Seek(oldOffset2,0)
                break
            }
        }
        gobjs=append(gobjs,gameObj{scene,sect,kinds[j],obj,path,model,texture,x,y,z,unknownB,props})
    }
    if len(gobjs)>0 {
        //insert all recs into table,should change props to json!!!
        insertSql := "INSERT INTO `SceneData`(SCENE,SECTION,KIND,OBJ,MODEL_PATH,MODEL,TEXTURE,X,Y,Z,UNKNOWN_B,PROPS) VALUES "
        vals:=[]interface{}{}
        for _, gobj := range gobjs {
            insertSql += "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?),"
            propsJSON, _ := json.Marshal(gobj.props)
            vals = append(vals, gobj.scene,gobj.sect,gobj.kind,gobj.obj,gobj.path,gobj.model,gobj.texture,gobj.x,gobj.y,gobj.z,gobj.unknownB,propsJSON)
        }
        insertSql = insertSql[:len(insertSql)-1]
        db.Exec(insertSql,vals...)
    }
    end:=time.Now().Format(layout)
    ch<-fmt.Sprintf("insert GameObjs file %v start at %v complete at %v",file,start,end)
}
func main() {
    db, _ := sql.Open("mysql", "golang:ktnpu9hxm27sr26g@/pal4_go")
    defer db.Close()
    for _,f:=range files {
        go insertGameObjs(f,db)
    }
    for j:=0;j<len(files);j++ {
        msg:=<-ch
        fmt.Println(msg)
    }
}
