package main

import (
	"bufio"
	"fmt"
	"os"
)

func findMatch(s1 string, s2 string, sum *int) {
	for _, c := range s1 {
		for _, d := range s2 {
			if c == d {
				x := int(c)
				if c > 64 && c < 91 {
					x -= 64 - 26
				} else if c > 96 && c < 123 {
					x -= 96
				} else {
					fmt.Println("DEAD")
				}
				*sum += x
				return
			}
		}
	}
}

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	sum := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		firstComp, secondComp := line[:len(line)/2], line[len(line)/2:]
		findMatch(firstComp, secondComp, &sum)
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
