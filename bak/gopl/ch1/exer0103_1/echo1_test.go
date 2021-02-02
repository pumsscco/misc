// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/

package echo1

import (
	"fmt"
	//"math/rand"
	"time"
)

//!+bench

import "testing"

func BenchmarkInefficient(b *testing.B) {
	start := time.Now()
	for i := 0; i < b.N; i++ {
		Inefficient()
	}
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}
