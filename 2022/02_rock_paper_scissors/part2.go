package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	A_X := 0 + 3
	A_Y := 3 + 1
	A_Z := 6 + 2
	B_X := 0 + 1
	B_Y := 3 + 2
	B_Z := 6 + 3
	C_X := 0 + 2
	C_Y := 3 + 3
	C_Z := 6 + 1

	sum := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()

		if line == "A X" {
			sum += A_X
		} else if line == "A Y" {
			sum += A_Y
		} else if line == "A Z" {
			sum += A_Z
		} else if line == "B X" {
			sum += B_X
		} else if line == "B Y" {
			sum += B_Y
		} else if line == "B Z" {
			sum += B_Z
		} else if line == "C X" {
			sum += C_X
		} else if line == "C Y" {
			sum += C_Y
		} else if line == "C Z" {
			sum += C_Z
		} else {
			fmt.Println(line)
		}
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
