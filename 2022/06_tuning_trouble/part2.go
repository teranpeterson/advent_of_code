package main

import (
	"bufio"
	"fmt"
	"os"
)

func checkIfUnique(s string) bool {
	m := map[rune]bool{}

	for _, t := range s {
		if m[t] {
			return false
		}
		m[t] = true
	}
	return true
}

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		for i := 0; i < len(line)-13; i++ {
			tag := line[i : i+14]
			if checkIfUnique(tag) {
				fmt.Println(i + 14)
				break
			}
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
