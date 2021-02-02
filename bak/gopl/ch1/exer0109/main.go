// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/

// See page 16.
//!+

// Fetch prints the content found at each specified URL.
package main

import (
	"fmt"
	"net/http"
	"os"
	"io"
	"strings"
)

func main() {
	for _, url := range os.Args[1:] {
		if !strings.HasPrefix(url,"http://") {
			url="http://"+url
		}
		resp, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		n, err :=io.Copy(os.Stdout,resp.Body)
		if err!= nil {
			fmt.Printf("\n write %d err %v \n", n, err)
			os.Exit(1)
		}
		//fmt.Printf("\n response status code:  %d \n", resp.StatusCode)
		fmt.Printf("\n response status:  %s \n", resp.Status)
		resp.Body.Close()
	}
}

//!-
