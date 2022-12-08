package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func getKey(x int, y int) string {
	s := strconv.Itoa(x)
	t := strconv.Itoa(y)
	return s + "_" + t
}

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	d := map[string]int{}

	x := 0
	y := 0

	d[getKey(x, y)] += 1
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		for _, c := range line {
			if c == 94 {
				y += 1
			} else if c == 62 {
				x += 1
			} else if c == 118 {
				y -= 1
			} else if c == 60 {
				x -= 1
			}
			d[getKey(x, y)] += 1
		}
	}

	fmt.Println(len(d))

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
