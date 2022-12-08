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

	santa_x := 0
	santa_y := 0
	robo_x := 0
	robo_y := 0

	d[getKey(santa_x, santa_y)] += 1
	d[getKey(robo_x, robo_y)] += 1
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		for idx, c := range line {
			if idx%2 == 0 {
				if c == 94 {
					santa_y += 1
				} else if c == 62 {
					santa_x += 1
				} else if c == 118 {
					santa_y -= 1
				} else if c == 60 {
					santa_x -= 1
				}
				d[getKey(santa_x, santa_y)] += 1
			} else {
				if c == 94 {
					robo_y += 1
				} else if c == 62 {
					robo_x += 1
				} else if c == 118 {
					robo_y -= 1
				} else if c == 60 {
					robo_x -= 1
				}
				d[getKey(robo_x, robo_y)] += 1
			}
		}
	}

	fmt.Println(len(d))

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
