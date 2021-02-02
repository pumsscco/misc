package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"os"
	"path/filepath"
)

func getInt(fp *os.File) int {
	tmpS := make([]byte, 4)
	fp.Read(tmpS)
	var i int32
	binary.Read(bytes.NewReader(tmpS), binary.LittleEndian, &i)
	return int(i)
}
func main() {
	var files, _ = filepath.Glob("/home/pluto/tmp/scenedata/*/*/mstInfo.mst")
	var wholeRecs int
	for _, f := range files {
		fp, _ := os.Open(f)
		rec := getInt(fp)
		fp.Close()
		wholeRecs += rec
	}
	fmt.Println(wholeRecs)
}
