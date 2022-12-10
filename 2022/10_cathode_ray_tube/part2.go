package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func printReg(d int, X int) {
	cycles := d % 40
	if X == cycles || X+1 == cycles || X+2 == cycles {
		fmt.Print("#")
	} else {
		fmt.Print(".")
	}
	if cycles == 0 {
		fmt.Println()
	}
}

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	X := 1
	cycles := 1

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		inst := line[0]
		if inst == "addx" {
			val, _ := strconv.Atoi(line[1])
			printReg(cycles, X)
			cycles++
			printReg(cycles, X)
			cycles++
			X += val
		} else {
			printReg(cycles, X)
			cycles += 1
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
