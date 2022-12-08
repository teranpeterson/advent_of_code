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

	n := 99
	forestMap := make([][]int, n)

	i := 0
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		row := strings.Split(line, "")
		ints := make([]int, len(row))
		for i, s := range row {
			ints[i], _ = strconv.Atoi(s)
		}
		forestMap[i] = append(forestMap[i], ints...)
		i++
	}

	bitMap := make([][]int, n)
	for i := range bitMap {
		bitMap[i] = make([]int, n)
	}

	top_height := []int{}
	for i := 0; i < n; i++ {
		top_height = append(top_height, -1)
	}
	left_height := []int{}
	for i := 0; i < n; i++ {
		left_height = append(left_height, -1)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			c := forestMap[i][j]
			if c > left_height[i] {
				bitMap[i][j] = 1
				left_height[i] = c
			}
			if c > top_height[j] {
				bitMap[i][j] = 1
				top_height[j] = c
			}
		}
	}

	bottom_height := []int{}
	for i := 0; i < n; i++ {
		bottom_height = append(bottom_height, -1)
	}
	right_height := []int{}
	for i := 0; i < n; i++ {
		right_height = append(right_height, -1)
	}
	for i := n - 1; i > -1; i-- {
		for j := n - 1; j > -1; j-- {
			c := forestMap[i][j]
			if c > right_height[i] {
				bitMap[i][j] = 1
				right_height[i] = c
			}
			if c > bottom_height[j] {
				bitMap[i][j] = 1
				bottom_height[j] = c
			}
		}
	}

	counter := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			c := bitMap[i][j]
			if c == 1 {
				counter++
			}
			fmt.Print(c)
		}
		fmt.Println()
	}

	fmt.Println(counter)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
