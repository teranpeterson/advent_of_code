package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

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
		pair := false
		sand := false
		for i := 0; i < len(line)-1; i++ {
			x := line[i : i+2]
			l_rest := line[:i]
			r_rest := line[i+2:]
			if strings.Contains(l_rest, x) || strings.Contains(r_rest, x) {
				pair = true
				break
			}
		}
		for i := 0; i < len(line)-2; i++ {
			if line[i] == line[i+2] {
				sand = true
				break
			}
		}
		if pair && sand {
			sum += 1
		}
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
