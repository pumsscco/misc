//使用了复杂映射，居然达到了效果，汗死！！！
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counts := make(map[string]int)
	in_files:=make(map[string]map[string]bool)
	files := os.Args[1:]
	var real_file bool;
	if len(files) == 0 {
		real_file=false
		countLines(os.Stdin, counts, "os.Stdin", in_files)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
				continue
			}
			real_file=true
			countLines(f, counts, arg, in_files)
			f.Close()
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
			if real_file==false {
				fmt.Printf("%s comes from standard input, not files\n", line)
			}else {
				fmt.Printf("%s comes from the following\n", line)
				for file, _ := range in_files[line] {
					fmt.Printf("\t%s", file)	
				}
				fmt.Println("")
			}
		}
	}
}

func countLines(f *os.File, counts map[string]int, filename string, in_files map[string]map[string]bool) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()]++
		in_file:=in_files[input.Text()]
		if in_file == nil {
			in_file=make(map[string]bool)
			in_files[input.Text()]=in_file
		}
		in_file[filename]=true
	}
}
