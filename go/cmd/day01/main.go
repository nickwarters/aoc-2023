package main

import (
	"fmt"
	"io"
	"os"
)

func solve_part_one(input_text string) int {
	return 0
}

func solve_part_two(input_text string) int {
	return 0
}


func main() {
	stdin, err := io.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}

	input := string(stdin)


	part_one_result := solve_part_one(input)
	part_two_result := solve_part_two(input)
	fmt.Printf("part one: %d\n", part_one_result)
	fmt.Printf("part one: %d\n", part_two_result)
}