package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	sums := []int{}
	sum := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		if len(line) > 0 {
			n, _ := strconv.Atoi(line[0])
			sum += n
		} else {
			sums = append(sums, sum)
			sum = 0
		}
	}

	sort.Sort(sort.Reverse(sort.IntSlice(sums)))
	fmt.Println(sums[0] + sums[1] + sums[2])

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
