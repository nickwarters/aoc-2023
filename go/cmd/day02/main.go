package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func solve_part_one(input_text string) int {
	total := 0

	game_limits := map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}

	for _, line := range strings.Split(input_text, "\n") {
		game_hands := strings.Split(line, ": ")
		game, hands := game_hands[0], game_hands[1]
		game_id, err := strconv.Atoi(strings.Replace(game, "Game ", "", -1))
		if err != nil {
			panic(err)
		}
		game_possible := true
		for _, hand := range strings.Split(hands, "; ") {
			if !game_possible {
				break
			}

			for _, cube := range strings.Split(hand, ", ") {
				count_colour := strings.Split(cube, " ")
				count, err := strconv.Atoi(count_colour[0])
				if err != nil {
					panic(err)
				}

				if game_limits[count_colour[1]] < count {
					game_id = 0
				}
			}
		}

		total += game_id

	}

	return total
}

func solve_part_two(input_text string) int {
	total := 0

	for _, line := range strings.Split(input_text, "\n") {
		game_hands := strings.Split(line, ": ")
		_, hands := game_hands[0], game_hands[1]

		game_mins := map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}

		for _, hand := range strings.Split(hands, "; ") {
			for _, cube := range strings.Split(hand, ", ") {
				count_colour := strings.Split(cube, " ")
				count, err := strconv.Atoi(count_colour[0])
				if err != nil {
					panic(err)
				}

				if game_mins[count_colour[1]] < count {
					game_mins[count_colour[1]] = count
				}
			}
		}

		total += game_mins["red"] * game_mins["green"] * game_mins["blue"]

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
