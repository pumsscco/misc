/*将所有文件，从gbk编码，转为utf8编码
第一步，先用weapon.xml来试验，再一步步扩容
*/
package main
import (
	"bytes"
	"golang.org/x/text/transform"
    "io/ioutil"
    "golang.org/x/text/encoding/simplifiedchinese"
    "log"
)
//将gbk文件轮换为utf8文件
func gbkToUTF8(src,dest string) {
    gbkContent,err:=ioutil.ReadFile(src)
    if err != nil {
        log.Fatal(err)
    }
    utfContent,_:=ioutil.ReadAll(transform.NewReader(bytes.NewReader(gbkContent), simplifiedchinese.GBK.NewDecoder()))
    ioutil.WriteFile(dest,utfContent,0644)
}
func main() {
    base:="/home/pluto/tmp"
    flist:=[]string{
        "accouterment.xml",
        "cdata.xml",
        "clothes.xml",
        "compose.xml",
        "help.xml",
        "item.xml",
        "journal.xml",
        "level.xml",
        "map.xml",
        "msdata_easy.xml",
        "msdata_hard.xml",
        "msdata.xml",
        "mstteam.xml",
        "mweapon.xml",
        "npcdata.xml",
        "shoes.xml",
        "skill.xml",
        "state.xml",
        "str.xml",
        "title.xml",
        "weapon.xml",
    }
    for _, f := range flist {
        gbkToUTF8(base+"/src/"+f,base+"/dest/"+f)
    }
}