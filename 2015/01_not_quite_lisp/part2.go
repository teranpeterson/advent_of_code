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

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		i := 0
		j := 0
		for _, c := range line {
			j += 1
			if c == 40 {
				i += 1
			} else if c == 41 {
				i -= 1
			}
			if i < 0 {
				fmt.Println(j)
				os.Exit(0)
			}
		}
		fmt.Println(i)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
