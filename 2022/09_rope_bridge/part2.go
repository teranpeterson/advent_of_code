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

	H0x := 0
	H0y := 0
	H1x := 0
	H1y := 0
	H2x := 0
	H2y := 0
	H3x := 0
	H3y := 0
	H4x := 0
	H4y := 0
	H5x := 0
	H5y := 0
	H6x := 0
	H6y := 0
	H7x := 0
	H7y := 0
	H8x := 0
	H8y := 0
	H9x := 0
	H9y := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		direction := line[0]
		distance, _ := strconv.Atoi(line[1])
		for i := 0; i < distance; i++ {
			if direction == "R" {
				H0x++
			} else if direction == "L" {
				H0x--
			} else if direction == "U" {
				H0y++
			} else if direction == "D" {
				H0y--
			}
			moveTail(&H0x, &H0y, &H1x, &H1y)
			moveTail(&H1x, &H1y, &H2x, &H2y)
			moveTail(&H2x, &H2y, &H3x, &H3y)
			moveTail(&H3x, &H3y, &H4x, &H4y)
			moveTail(&H4x, &H4y, &H5x, &H5y)
			moveTail(&H5x, &H5y, &H6x, &H6y)
			moveTail(&H6x, &H6y, &H7x, &H7y)
			moveTail(&H7x, &H7y, &H8x, &H8y)
			moveTail(&H8x, &H8y, &H9x, &H9y)

			d[getKey(H9x, H9y)] += 1
		}
	}

	fmt.Println(len(d))

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
