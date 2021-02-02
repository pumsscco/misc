//Exer0202
// general converters,  Celsius and Fahrenheit, length in feet and meters, weight in pounds and kilograms
package main

import (
	"fmt"
	"os"
	"strconv"
	"bufio"
	"gopl/ch2/tempconv"
)

type Feet float64
type Meters float64
type Pounds float64
type Kilograms float64

func (f Feet) String() string    { return fmt.Sprintf("%gft", f) }
func (m Meters) String() string { return fmt.Sprintf("%gm", m) }
func (p Pounds) String() string { return fmt.Sprintf("%glb", p) }
func (k Kilograms) String() string { return fmt.Sprintf("%gkg", k) }

// FToM converts a Feet length to Meters.
func FToM(f Feet) Meters { return Meters(f * 0.3048) }
// MToF converts a Meter length to Feet.
func MToF(m Meters) Feet { return Feet(m * 3.2808) }
// PToK converts a Pound weight to Kilograms.
func PToK(p Pounds) Kilograms { return Kilograms(p * 0.4536) }
// KToP converts a Kilogram weight to Pounds.
func KToP(k Kilograms) Pounds { return Pounds(k * 2.2046) }

func conv(t float64) {
	// temperature
	fa := tempconv.Fahrenheit(t)
	c := tempconv.Celsius(t)
	fmt.Printf("%s = %s, %s = %s\n", fa, tempconv.FToC(fa), c, tempconv.CToF(c))
	// length
	fe := Feet(t)
	m := Meters(t)
	fmt.Printf("%s = %s, %s = %s\n", fe, FToM(fe), m, MToF(m))
	// length
	p := Pounds(t)
	k := Kilograms(t)
	fmt.Printf("%s = %s, %s = %s\n", p, PToK(p), k, KToP(k))
}

func main() {
	if len(os.Args)>1 {
		//read from command line arguments
		for _, arg := range os.Args[1:] {
			t, err := strconv.ParseFloat(arg, 64)
			if err != nil {
				fmt.Fprintf(os.Stderr, "exer0202 parse float error: %v\n", err)
				os.Exit(1)
			}
			conv(t)
		}
	} else {
		//read from stdin
		input := bufio.NewScanner(os.Stdin)
		for input.Scan() {
			t, err := strconv.ParseFloat(input.Text(), 64)
			if err != nil {
				fmt.Fprintf(os.Stderr, "exer0202 scan float64 error: %v\n", err)
				os.Exit(1)
			}
			conv(t)
		}
	}
}
