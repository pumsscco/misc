/*利用多个颜色，为一系列函数画走势图，类似做数学题，具体包括以下函数：
N
N**(1/2)
N**1.5
N**2
N*logN
N*log(logN)
N*(logN)**2
N*log(N**2)
2/N
2**N
2**(N/2)
37
N**2*logN
N**3
*/
package main

import (
	"image"
	"image/color"
	"image/jpeg"
	"os"
	"math"
	"fmt"
	"strconv"
)
var palette = []color.Color{
	color.Black,  
	color.RGBA{0x00, 0xff, 0xff, 0xff}, //aqua
	color.RGBA{0x80, 0x80, 0x80, 0xff}, //gray
	color.RGBA{0x00, 0x00, 0x80, 0xff}, //navy
	color.RGBA{0xc0, 0xc0, 0xc0, 0xff}, //silver
	color.RGBA{0x00, 0x80, 0x00, 0xff}, //green
	color.RGBA{0x80, 0x80, 0x00, 0xff}, //olive
	color.RGBA{0x00, 0x80, 0x80, 0xff}, //teal
	color.RGBA{0x00, 0x00, 0xff, 0xff}, //blue
	color.RGBA{0x00, 0xff, 0x00, 0xff}, //lime
	color.RGBA{0x80, 0x00, 0x80, 0xff}, //purple
	color.RGBA{0xff, 0xff, 0x00, 0xff}, //yellow
	color.RGBA{0xff, 0x00, 0xff, 0xff}, //fuchsia
	color.RGBA{0x80, 0x00, 0x00, 0xff}, //maroon
	color.RGBA{0xff, 0x00, 0x00, 0xff}, //red
	color.White, 
}

const (
	blackIndex = 0 
	aquaIndex = 1 
	grayIndex = 2
	navyIndex = 3 
	silverIndex = 4
	greenIndex = 5
	oliveIndex = 6 
	tealIndex = 7
	blueIndex = 8 
	limeIndex = 9 
	purpleIndex = 10 
	yellowIndex = 11
	fuchsiaIndex = 12 
	maroonIndex = 13
	redIndex = 14
	whiteIndex = 15
)
//N
func  F1(x int)  int {
	return x
}
//N**(1/2)
func  F2(x int)  int {
	return int(math.Pow(float64(x),0.5)+0.5)
}
//N**1.5
func  F3(x int)  int {
	return int(math.Pow(float64(x),1.5)+0.5)
}
//N**2
func  F4(x int)  int {
	return x*x
}
//N*logN
func  F5(x int)  int {
	return int(float64(x)*math.Log2(float64(x))+0.5)
}
//N*log(logN)
func  F6(x int)  int {
	return int(float64(x)*math.Log2(math.Log2(float64(x)))+0.5)
}
//N*(logN)**2
func  F7(x int)  int {
	return int(float64(x)*math.Log2(float64(x))*math.Log2(float64(x))+0.5)
}
//N*log(N**2)
func  F8(x int)  int {
	return int(float64(x)*math.Log2(float64(x*x))+0.5)
}
//2/N
func  F9(x int)  int {
	return int(2.0/float64(x)+0.5)
}
//2**N
func  F10(x int)  int {
	return int(math.Pow(2.0,float64(x))+0.5)
}
//2**(N/2)
func  F11(x int)  int {
	return int(math.Pow(2.0,float64(x)/2.0)+0.5)
}
//37
func  F12(x int)  int {
	return 37
}
//N**2*logN
func  F13(x int)  int {
	return int(float64(x*x)*math.Pow(float64(x),0.5)+0.5)
}
//N**3
func  F14(x int)  int {
	return x*x*x
}
func main() {
	const (
		width, height          = 1920, 1080
	)
	//必须带函数编号与颜色编号
	fn,_:=strconv.ParseInt(os.Args[1],10,8)
	ci,_:=strconv.ParseInt(os.Args[2],10,8)
	var F func(int) int
	switch fn {
	case 1:
		F=F1
	case 2:
		F=F2
	case 3:
		F=F3
	case 4:
		F=F4
	case 5:
		F=F5
	case 6:
		F=F6
	case 7:
		F=F7
	case 8:
		F=F8
	case 9:
		F=F9
	case 10:
		F=F10
	case 11:
		F=F11
	case 12:
		F=F12
	case 13:
		F=F13
	case 14:
		F=F14
	}
	rect := image.Rect(0, 0, width, height)
	img := image.NewPaletted(rect, palette)
	var y int
	for x := 0; x <= width; x++ {
		y = F(x)
		img.SetColorIndex(x, y, uint8(ci))
	}
	fmt.Println("最终纵坐标（可能溢出）：",y)
	jpgname:=fmt.Sprintf("y%d-%d.jpg",fn,ci)
	y1pic,_:=os.Create(jpgname)
	jpeg.Encode(y1pic, img, nil) // NOTE: ignoring errors
}
