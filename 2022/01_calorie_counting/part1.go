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

	max := 0
	sum := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		if len(line) > 0 {
			n, _ := strconv.Atoi(line[0])
			sum += n
		} else {
			if sum > max {
				max = sum
			}
			sum = 0
		}
	}

	fmt.Println(max)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
