package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func getKey(x int, y int) string {
	s := strconv.Itoa(x)
	t := strconv.Itoa(y)
	return s + "_" + t
}

func searchMap(elevation [][]rune, old rune, x int, y int, count int, path map[string]bool) int {
	if path[getKey(x, y)] {
		fmt.Print("a")
		return math.MaxInt
	}
	path[getKey(x, y)] = true
	if x < 0 || x >= len(elevation[0]) || y < 0 || y >= len(elevation) {
		fmt.Print("b")
		return math.MaxInt
	}
	new := elevation[y][x]
	if new == 69 {
		if 'z'-old > 1 {
			fmt.Print("c")
			return math.MaxInt
		} else {
			return count
		}
	} else if new-old > 1 {
		fmt.Print("d")
		return math.MaxInt
	} else {
		min := math.MaxInt
		if x := searchMap(elevation, new, x+1, y, count+1, path); x < min {
			min = x
		}
		if x := searchMap(elevation, new, x-1, y, count+1, path); x < min {
			min = x
		}
		if x := searchMap(elevation, new, x, y+1, count+1, path); x < min {
			min = x
		}
		if x := searchMap(elevation, new, x, y-1, count+1, path); x < min {
			min = x
		}
		return min
	}
}

func main() {
	input, err := os.Open("test.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	elevation := [][]rune{}

	Sx := -1
	Sy := -1
	y := 0
	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		row := []rune{}
		for x, c := range line {
			if c == 'S' {
				row = append(row, 'a')
				Sx = x
				Sy = y
			} else {
				row = append(row, c)
			}
		}
		elevation = append(elevation, row)
		y++
	}

	res := searchMap(elevation, 'a', Sx, Sy, 0, map[string]bool{})
	if res == math.MaxInt {
		fmt.Println("Broken")
	} else {
		fmt.Println(res)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
