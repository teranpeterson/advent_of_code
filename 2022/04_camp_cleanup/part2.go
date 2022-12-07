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

	sum := 0

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := scanner.Text()
		elfs := strings.Split(line, ",")
		elf1, elf2 := strings.Split(elfs[0], "-"), strings.Split(elfs[1], "-")
		elf1_start, elf1_end := elf1[0], elf1[1]
		elf2_start, elf2_end := elf2[0], elf2[1]
		elf1_start_n, _ := strconv.Atoi(elf1_start)
		elf1_end_n, _ := strconv.Atoi(elf1_end)
		elf2_start_n, _ := strconv.Atoi(elf2_start)
		elf2_end_n, _ := strconv.Atoi(elf2_end)
		if (elf1_end_n >= elf2_start_n && elf1_start_n <= elf2_end_n) || (elf2_end_n >= elf1_start_n && elf2_start_n <= elf1_end_n) {
			sum += 1
		}
	}

	fmt.Println(sum)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
