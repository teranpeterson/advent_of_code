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

	max := 0

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			c := forestMap[i][j]
			left := 0
			left_j := j
			for left_j > 0 {
				left_j--
				left++
				if forestMap[i][left_j] >= c {
					break
				}
			}

			right := 0
			right_j := j
			for right_j < n-1 {
				right_j++
				right++
				if forestMap[i][right_j] >= c {
					break
				}
			}

			up := 0
			up_i := i
			for up_i > 0 {
				up_i--
				up++
				if forestMap[up_i][j] >= c {
					break
				}
			}

			down := 0
			down_i := i
			for down_i < n-1 {
				down_i++
				down++
				if forestMap[down_i][j] >= c {
					break
				}
			}

			score := right * left * up * down
			if score > max {
				max = score
			}
		}
	}

	fmt.Println(max)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
