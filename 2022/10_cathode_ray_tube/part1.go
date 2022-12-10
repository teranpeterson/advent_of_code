package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func printReg(cycles int, X int) int {
	if cycles == 20 || cycles == 60 || cycles == 100 || cycles == 140 || cycles == 180 || cycles == 220 {
		strength := cycles * X
		fmt.Printf("%d: %d = %d\n", cycles, X, strength)
		return strength
	} else {
		return 0
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
	sum := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		inst := line[0]
		if inst == "addx" {
			val, _ := strconv.Atoi(line[1])
			sum += printReg(cycles, X)
			cycles++
			sum += printReg(cycles, X)
			cycles++
			X += val
		} else {
			sum += printReg(cycles, X)
			cycles += 1
		}
	}
	sum += printReg(cycles, X)
	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
