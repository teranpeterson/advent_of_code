package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
	"strings"
)

func getMD5Hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func main() {
	i := 0
	for true {
		i += 1
		s := strconv.Itoa(i)

		text := "yzbqklnj" + s

		hash := getMD5Hash(text)
		if strings.HasPrefix(hash, "00000") {
			fmt.Println(i)
			break
		}
	}
}
