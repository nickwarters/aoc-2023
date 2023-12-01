package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func solve_part_one(input_text string, replace bool) int {
	total := 0

	subs := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

	for _, line := range strings.Split(input_text, "\n") {
		if replace {
			for i, s := range subs {
				line = strings.ReplaceAll(line, s, fmt.Sprintf("%c%d%c", s[0], i + 1, s[len(s) - 1]))
			}	
		}
		r := regexp.MustCompile("[0-9]")
		digits := r.FindAllString(line, -1)

		if len(digits) == 0 {
			continue
		}

		n, err := strconv.Atoi(fmt.Sprintf("%s%s", digits[0], digits[len(digits) -1]))
		if (err != nil) {
			panic(err)
		}

		total += n
	}

	return total
}

func solve_part_two(input_text string) int {
	return solve_part_one(input_text, true)
}


func main() {
	stdin, err := io.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}

	input := string(stdin)


	part_one_result := solve_part_one(input, false)
	part_two_result := solve_part_two(input)
	fmt.Printf("part one: %d\n", part_one_result)
	fmt.Printf("part two: %d\n", part_two_result)
}