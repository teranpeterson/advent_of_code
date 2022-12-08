package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func min(nums ...int) int {
	m := math.MaxInt
	for _, n := range nums {
		if n < m {
			m = n
		}
	}
	return m
}

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
		dims := strings.Split(line, "x")
		l, _ := strconv.Atoi(dims[0])
		h, _ := strconv.Atoi(dims[1])
		w, _ := strconv.Atoi(dims[2])
		dim := 2*l*w + 2*w*h + 2*h*l
		slack := min(l*w, w*h, h*l)
		sum += dim + slack
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
