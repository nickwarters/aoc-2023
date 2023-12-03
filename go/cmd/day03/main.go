package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

type N struct {
	value int
	row int
	startCol int
	endCol int
}

type S struct {
	value string
	row int
	col int
}

func solve_part_one(input_text string) int {
	total := 0

	grid := strings.Split(input_text, "\n")

	numbers := []N{}
	symbols := []S{}

	for r, row := range grid{
		inNum := false
		num := ""
		numstart := 0
		for c, ch := range row{
			_, err := strconv.Atoi(string(ch))
			if err != nil {
				if inNum {
					n, _ := strconv.Atoi(num)
					numbers = append(numbers, N{
						value: n,
						startCol: numstart,
						endCol: c - 1,
						row: r,
					})
					inNum = false
					numstart = 0
					num = ""
				}

				if string(ch) != "." {
					symbols = append(symbols, S{
						row: r,
						col: c,
						value: string(ch),
					})
				}

			} else {
				if !inNum {
					numstart = c
				}
				inNum = true
				num += string(ch)
			}
		}
	}

	// directions := [][]int{
	// 	[]int{-1, -1},
	// 	[]int{-1, 0},
	// 	[]int{-1, 1},
	// 	[]int{0, -1},
	// 	[]int{0, 1},
	// 	[]int{1, -1},
	// 	[]int{1, -1},
	// 	[]int{1, 1},
	// }

	for _, n := range numbers {
		valid := false
		for _, s := range symbols {
			if s.row >= n.row -1 && s.row <= n.row + 1 && s.col >= n.startCol - 1 && s.col <= n.endCol + 1{
				valid = true
				// fmt.Printf("added --> num: %v, sym: %v\n", n, s)
				break
			}
		}
		if valid{
			total += n.value
		} else {
			fmt.Printf("not added --> num: %v\n", n)
		}
	}



	// fmt.Printf("NUMBERS\n%v\n\nSYMBOLS\n%v\n", numbers, symbols)


	return total
}

func solve_part_two(input_text string) int {
	total := 0

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
