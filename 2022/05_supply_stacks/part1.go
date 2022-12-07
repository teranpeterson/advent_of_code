package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	crates := map[string][]string{
		"s1": {"H", "R", "B", "D", "Z", "F", "L", "S"},
		"s2": {"T", "B", "M", "Z", "R"},
		"s3": {"Z", "L", "C", "H", "N", "S"},
		"s4": {"S", "C", "F", "J"},
		"s5": {"P", "G", "H", "W", "R", "Z", "B"},
		"s6": {"V", "J", "Z", "G", "D", "N", "M", "T"},
		"s7": {"G", "L", "N", "W", "F", "S", "P", "Q"},
		"s8": {"M", "Z", "R"},
		"s9": {"M", "C", "L", "G", "V", "R", "T"},
	}

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		moves, _ := strconv.Atoi(line[1])
		for i := 1; i <= moves; i++ {
			stack1 := crates["s"+line[3]]
			stack2 := crates["s"+line[5]]
			if len(stack1) > 0 {
				j := len(stack1) - 1
				x := stack1[j]
				crates["s"+line[3]] = append(stack1[:j], stack1[j+1:]...)
				crates["s"+line[5]] = append(stack2, x)
			}
		}
	}

	fmt.Println(crates)
	for i := 1; i < 10; i++ {
		t := strconv.Itoa(i)
		fmt.Print(crates["s"+t][len(crates["s"+t])-1])
	}
	fmt.Println()

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
