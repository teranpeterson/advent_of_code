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
		n := 0
		dup := false
		cln := true
		for i := 0; i < len(line); i++ {
			x := string(line[i])
			if strings.Contains("aeiou", x) {
				n += 1
			}
			if i >= len(line)-1 {
				break
			}
			s := line[i : i+2]
			if s == "ab" || s == "cd" || s == "pq" || s == "xy" {
				cln = false
				break
			}
			if line[i] == line[i+1] {
				dup = true
			}
		}
		if n >= 3 && dup && cln {
			sum += 1
		}
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
