// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/
//Exer1.12
//!+main

// Lissajous generates GIF animations of random Lissajous figures.
package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"math"
	"math/rand"
	"os"
	"fmt"
	"log"
	"net/http"
	"time"
	"strconv"
)

//!+main

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
	blackIndex = 0 // first color in palette
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
	whiteIndex = 15 // next color in palette
)

func lissajous(cycles float64, colorIndex uint8, out io.Writer) {
	const (
		//cycles  = 5     // number of complete x oscillator revolutions
		res     = 0.001 // angular resolution
		size    = 100   // image canvas covers [-size..+size]
		nframes = 64    // number of animation frames
		delay   = 8     // delay between frames in 10ms units
	)
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 // phase difference
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5),
				colorIndex)
		}
		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
}

func handler(w http.ResponseWriter, r *http.Request) {
    if err := r.ParseForm(); err != nil {
        log.Print(err)
    }
	var cycles float64 = 5
	var colorIndex uint8 = 10
    for k, v := range r.Form {
        if k == "cycles" {
			i,err := strconv.Atoi(v[0])
			if err != nil {
				fmt.Fprint(w,"exer0112 strconv error: %v\n ",err)
				os.Exit(1)
			}
			cycles = float64(i)
		} else if k == "colorIndex" {
			i,err := strconv.Atoi(v[0])
			if err != nil {
				fmt.Fprint(w,"exer0112 strconv error: %v\n ",err)
				os.Exit(1)
			}
			colorIndex = uint8(i)
		}
    }
	lissajous(cycles, colorIndex, w)
}

func main() {
	//!-main
	// The sequence of images is deterministic unless we seed
	// the pseudo-random number generator using the current time.
	// Thanks to Randall McPherson for pointing out the omission.
	rand.Seed(time.Now().UTC().UnixNano())
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe("192.168.23.57:8000", nil))
}

