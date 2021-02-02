package main
import (
	"encoding/xml"
	//"io/ioutil"
    //"log"
    "fmt"
)
type Email struct {
	XMLName xml.Name `xml:"email"`
    Where string `xml:"位置,attr"`
}
type Result struct {
    XMLName xml.Name `xml:"person"`
    Email   []Email `xml:"email"`
}
func main() {
	v := Result{}

	data := `
		<person>
			<email 位置="home" />
			<email 位置='work' />
		</person>
	`
	err := xml.Unmarshal([]byte(data), &v)
	if err != nil {
		fmt.Printf("error: %v", err)
		return
	}
	fmt.Printf("XMLName: %#v\n", v.XMLName)
	fmt.Printf("Email: %v\n", v.Email)
}
