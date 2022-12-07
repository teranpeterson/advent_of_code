package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type directory struct {
	parent   *directory
	name     string
	size     int64
	children []*directory
	files    []*file
}

type file struct {
	parent *directory
	name   string
	size   int64
}

func (dir *directory) RPrint(indent string) {
	fmt.Printf("%s- %s (dir, size=%d)\n", indent, dir.name, dir.size)
	indent = indent + "  "
	for _, file := range dir.files {
		fmt.Printf("%s- %s (file, size=%d)\n", indent, file.name, file.size)
	}
	for _, child := range dir.children {
		child.RPrint(indent)
	}
}

func (dir *directory) ComputeSize(totalSize *int64) int64 {
	var sum int64 = 0
	for _, file := range dir.files {
		sum += file.size
	}
	for _, child := range dir.children {
		sum += child.ComputeSize(totalSize)
	}
	dir.size = sum
	if sum <= 100000 {
		*totalSize += sum
	}
	return sum
}

func main() {
	input, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer input.Close()

	fs := directory{name: "/"}
	pwd := &fs

	scanner := bufio.NewScanner(input)
	for scanner.Scan() {
		line := strings.Fields(scanner.Text())
		if line[0] == "$" {
			if line[1] == "cd" {
				if line[2] == ".." {
					pwd = pwd.parent
				} else if line[2] == "/" {
					pwd = &fs
				} else {
					for i := range pwd.children {
						if pwd.children[i].name == line[2] {
							pwd = pwd.children[i]
							break
						}
					}
				}
			}
		} else if line[0] == "dir" {
			temp := directory{name: line[1], parent: pwd}
			pwd.children = append(pwd.children, &temp)
		} else if n, err := strconv.ParseInt(line[0], 10, 64); err == nil {
			temp := file{name: line[1], size: n, parent: pwd}
			pwd.files = append(pwd.files, &temp)
		}
	}

	var totalSize int64 = 0
	fs.ComputeSize(&totalSize)
	fmt.Println(totalSize)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
