package utils

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func ReadLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}

	reader := bufio.NewReader(file)

	var text []byte
	_, err = reader.Read(text)

	return strings.Split(string(text), "\n"), err
}