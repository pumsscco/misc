// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/

// See page 4.
//!+

// Echo1 prints its command-line arguments.
package echo3

import (
	"fmt"
	"os"
	"strings"
)

func Efficient() {
	fmt.Println(strings.Join(os.Args[1:], " "))
}

//!-
