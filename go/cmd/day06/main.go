package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func solve_part_one(input_text string) int {
	total := 0

	times := regexp.MustCompile(`\d{1,}`).FindAllString(strings.Split(input_text, "\n")[0], -1)
	records := regexp.MustCompile(`\d{1,}`).FindAllString(strings.Split(input_text, "\n")[1], -1)

	i := 0
	for i < len(times) {
		t, err := strconv.Atoi(times[i])
		if err != nil {
			panic(err)
		}
		r, err := strconv.Atoi(records[i])
		if err != nil {
			panic(err)
		}

		n := 1
		c := 0
		for n < t {
			d := n * (t - n)
			if d > r {
				c++
			}

			n++
		}

		if total == 0 {
			total = c
		} else {
			total = total * c
		}

		i++

	}

	return total
}

func solve_part_two(input_text string) int {
	total := 0

	t, err := strconv.Atoi(strings.Split(strings.ReplaceAll(strings.Split(input_text, "\n")[0], " ", ""), ":")[1])
	if err != nil {
		panic(err)
	}
	r, err := strconv.Atoi(strings.Split(strings.ReplaceAll(strings.Split(input_text, "\n")[1], " ", ""), ":")[1])
	if err != nil {
		panic(err)
	}

	n := 1
	for n < t {
		d := n * (t - n)
		if d > r {
			total++
		}

		n++
	}

	return total
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
	fmt.Printf("part two: %d\n", part_two_result)
}
