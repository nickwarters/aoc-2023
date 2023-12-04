package main

import (
	"fmt"
	"io"
	"math"
	"os"
	"strings"
)

func solve_part_one(input_text string) int {
	total := 0
	for _, card := range strings.Split(input_text, "\n") {
		cardTotal := 0
		winners_have := strings.Split(card, " | ")
		winners := strings.Split(strings.Split(winners_have[0], ": ")[1], " ")
		have := strings.Split(winners_have[1], " ")

		for _, h := range have {
			if h == "" {
				continue
			}
			for _, w := range winners {
				if h == w {
					cardTotal++
				}
			}
		}

		total += int(math.Pow(2, float64(cardTotal)-1))
	}

	return total
}

func solve_part_two(input_text string) int {
	total := 0
	cardCounts := map[int]int{}

	for i, card := range strings.Split(input_text, "\n") {
		if cardCounts[i] == 0 {
			cardCounts[i]++
		}
		cardTotal := 0
		winners_have := strings.Split(card, " | ")
		winners := strings.Split(strings.Split(winners_have[0], ": ")[1], " ")
		have := strings.Split(winners_have[1], " ")

		for _, h := range have {
			if h == "" {
				continue
			}
			for _, w := range winners {
				if h == w {
					cardTotal++
				}
			}
		}

		for n := i + 1; n < i+cardTotal+1; n++ {
			cardCounts[n] = int(math.Max(float64(1), float64(cardCounts[n]))) + cardCounts[i]
		}

	}

	for _, v := range cardCounts {
		total += v
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
