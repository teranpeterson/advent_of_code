package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func moveTail(H_x *int, H_y *int, T_x *int, T_y *int) {
	y_diff := *H_y - *T_y
	x_diff := *H_x - *T_x
	if y_diff == 0 && x_diff > 1 {
		*T_x++
	} else if y_diff == 0 && x_diff < -1 {
		*T_x--
	} else if x_diff == 0 && y_diff > 1 {
		*T_y++
	} else if x_diff == 0 && y_diff < -1 {
		*T_y--
	} else if math.Abs(float64(y_diff)) > 1 || math.Abs(float64(x_diff)) > 1 {
		if y_diff > 0 {
			*T_y++
		} else {
			*T_y--
		}
		if x_diff > 0 {
			*T_x++
		} else {
			*T_x--
		}
	}
}

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

	H_x := 0
	H_y := 0
	T_x := 0
	T_y := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		direction := line[0]
		distance, _ := strconv.Atoi(line[1])
		for i := 0; i < distance; i++ {
			if direction == "R" {
				H_x++
			} else if direction == "L" {
				H_x--
			} else if direction == "U" {
				H_y++
			} else if direction == "D" {
				H_y--
			}
			moveTail(&H_x, &H_y, &T_x, &T_y)
			d[getKey(T_x, T_y)] += 1
		}
	}

	fmt.Println(len(d))

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
