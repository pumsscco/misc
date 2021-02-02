// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/

// See page 45.

// (Package doc comment intentionally malformed to demonstrate golint.)
//!+
package popcount
// PopCount returns the population count (number of set bits) of x.
func PopCount(x uint64) int {
	var pc int = 0
	for {
		if x == 0 {
			return pc
		} else {
			x = x&(x-1)
			pc++
		}
	}
}

//!-
