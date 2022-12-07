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

	sum := 0
	triDict := map[rune]int{}

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		lineDict := map[rune]int{}
		for _, c := range line {
			lineDict[c] += 1
			if lineDict[c] == 1 {
				triDict[c] += 1
				if triDict[c] == 3 {
					x := int(c)
					if x > 64 && x < 91 {
						x -= 64 - 26
					} else if x > 96 && x < 123 {
						x -= 96
					} else {
						fmt.Println("DEAD")
					}
					sum += x
					triDict = map[rune]int{}
					break
				}
			}
		}
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
