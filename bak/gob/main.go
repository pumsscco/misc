//场景物体信息再次解析
package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"log"
)
func GetInt(fp *os.File) int {
    tmpS := make([]byte,4)
    fp.Read(tmpS)
    var i int32
    binary.Read(bytes.NewReader(tmpS),binary.LittleEndian,&i)
    return int(i)
}
func GetFloat(fp *os.File)(f float32){
    tmpS := make([]byte,4)
    fp.Read(tmpS)
    binary.Read(bytes.NewReader(tmpS),binary.LittleEndian,&f)
    return
}
func GetStr(fp *os.File,l int) string {
    tmpS := make([]byte,l)
    fp.Read(tmpS)
    return string(tmpS)
}
func GetFlag(fp *os.File,l int) string {
    tmpS := make([]byte,l)
    fp.Read(tmpS)
    return fmt.Sprintf("%0X", tmpS)
}
type Gob struct {
    Scene,Sect,Id,Path,Model,Texture string
	InitCoor,Coor2,TripleInt,Func string
	Kind int
	UnkFloat float32
    Attr string
}
func GobDecode(file string) (gobs []Gob, errinfo string) {
	scene:=filepath.Base(filepath.Dir(filepath.Dir(file)))
    sect:=filepath.Base(filepath.Dir(file))
	fp,_:=os.Open(file)
	defer fp.Close()
	recs:=GetInt(fp)
	var kinds []int
    for i:=0;i<recs;i++ {
        kinds=append(kinds,GetInt(fp))
    }
	for j:=0; j<recs; j++ {
		var gob Gob
		gob.Scene,gob.Sect=scene,sect
		gob.Kind=kinds[j]
		gob.Id=GetStr(fp,GetInt(fp))
		gob.Id=gob.Id[:len(gob.Id)-1]
		gob.Path=GetStr(fp,GetInt(fp))
		gob.Path=gob.Path[:len(gob.Path)-1]
		gob.Model=GetStr(fp,GetInt(fp))
		gob.Model=gob.Model[:len(gob.Model)-1]
		gob.Texture=GetStr(fp,GetInt(fp))
		if gob.Texture!="" {
			gob.Texture=gob.Texture[:len(gob.Texture)-1]
		}
		gob.InitCoor=fmt.Sprintf("%5.3f, %5.3f, %5.3f",GetFloat(fp),GetFloat(fp),GetFloat(fp))
		gob.Coor2=fmt.Sprintf("%5.3f, %5.3f, %5.3f",GetFloat(fp),GetFloat(fp),GetFloat(fp))
		gob.Func=GetStr(fp,GetInt(fp))
		gob.Func=gob.Func[:len(gob.Func)-1]
		gob.TripleInt=fmt.Sprintf("%d, %d, %d",GetInt(fp),GetInt(fp),GetInt(fp))
		gob.UnkFloat=GetFloat(fp)
		GetFlag(fp,8)
		var (
			field,s1 string
			i1,i2 int
			f1 float32
		)
		field=GetStr(fp,GetInt(fp))
		i1,i2=GetInt(fp),GetInt(fp)
		field=fmt.Sprintf("%s: %d, %d;\n",field,i1,i2)
		gob.Attr+=field
		for {
			offset,_:=fp.Seek(0,1)
			field=GetStr(fp,GetInt(fp))
			if match, _ := regexp.MatchString("^(PAL4|CSTR)", field); !match {
				fp.Seek(offset,0)
				break
			} else if match,_=regexp.MatchString("(name|func|launchEff)$",field); match {
				s1,i2=GetStr(fp,GetInt(fp)),GetInt(fp)
				field=fmt.Sprintf("%s: %s, %d;\n",field,s1,i2)
				gob.Attr+=field
			} else if match,_=regexp.MatchString("(time|scale|X|Y|Z|amplitude|frequency|maxval|minval|effDuration|effTime|effHurt|tMax|tMin|thrust|directDist|suction)$",field); match {
				f1,i2=GetFloat(fp),GetInt(fp)
				field=fmt.Sprintf("%s: %5.3f, %d;\n",field,f1,i2)
				gob.Attr+=field
			} else  {
				i1,i2=GetInt(fp),GetInt(fp)
				field=fmt.Sprintf("%s: %d, %d;\n",field,i1,i2)
				gob.Attr+=field
			}
		}
		if gob==(Gob{}) {
			errinfo="文件解析出错"
			offset,_:=fp.Seek(0,1)
			log.Fatalf("%s，地址：%0X\n",errinfo,offset)
		}
		gobs=append(gobs,gob)
	}
	return
}
func main() {
	var gobFiles,_=filepath.Glob("/home/pluto/tmp/scenedata/*/*/GameObjs.gob")
	for _,f:=range gobFiles {
		fmt.Println(f)
		/*
		gobs,errinfo:=GobDecode(f)
		if errinfo=="文件解析出错" {
			fmt.Printf("%+v",gobs)
		}
		*/
		GobDecode(f)
	}
}
