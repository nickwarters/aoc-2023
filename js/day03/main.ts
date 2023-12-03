import fs from 'fs'

type S = {
	row: number
	column: number
	value: string
}

type N = {
	value: number
	row: number
	start: number
	end: number
	isValid: boolean
}

function solve_day_one(input: string): number {
	let total = 0

	const grid = input.split('\n')

	const symbols: S[] = []
	const numbers: N[] = []

	const allNumbers = '1234567890'

	const directions = [
		[-1, 0],
		[-1, -1],
		[-1, 1],
		[0, -1],
		[0, 1],
		[1, -1],
		[1, 0],
		[1, 1],
	]

	total = input
		.split('\n')
		.reduce((numbers, row, r, rows) => {
			let inNum = false
			let num = ''
			let numStart = 0
			let isValid = false

			row.split('').forEach((ch, c) => {
				const isNumber = allNumbers.includes(ch)
				if (isNumber) {
					num += ch
					if (!inNum) {
						numStart = c
					}
					inNum = true
				} else {
					inNum = false
				}

				if (!isValid && (isNumber || num !== '')) {
					let sr: number
					let sc: number

					for (const d of directions) {
						sr = r + d[0]
						sc = c + d[1]
						if (sr < 0 || sr >= rows.length || sc < 0 || sc >= row.length) {
							continue
						}

						if (rows[sr][sc] !== '.' && !allNumbers.includes(rows[sr][sc])) {
							isValid = true
							// console.log({ r, c, ch, sr, sc, sym: rows[sr][sc] })
							break
						}
					}
				}

				if (!isNumber && num != '') {
					numbers.push({
						value: Number(num),
						row: r,
						start: numStart,
						end: c - 1,
						isValid,
					})

					num = ''
					numStart = 0
					isValid = false
				}
			})

			return numbers
		}, numbers)
		.filter((n) => {
			// console.log(n)
			return n.isValid
		})
		.reduce((sum, n) => sum + n.value, 0)

	// console.log(
	// 	numbers.filter(
	// 		(n) =>
	// 			symbols.filter(
	// 				(s) =>
	// 					!(
	// 						s.row >= n.row - 1 &&
	// 						s.row <= n.row + 1 &&
	// 						s.column >= n.start - 1 &&
	// 						s.column <= n.end + 1
	// 					)
	// 			).length > 0
	// 	)
	// )

	// total = numbers
	// 	.filter(
	// 		(n) =>
	// 			symbols.filter((s) => {
	// 				return (
	// 					s.row >= n.row - 1 &&
	// 					s.row <= n.row + 1 &&
	// 					s.column >= n.start - 1 &&
	// 					s.column <= n.end + 1
	// 				)
	// 			}).length > 0
	// 	)
	// 	.reduce((t, n) => {
	// 		console.log(n)
	// 		return t + n.value
	// 	}, 0)

	return total
}

function solve_day_two(input: string): number {
    let total = 0

    return total
}

function main() {
    const data = fs.readFileSync(0, 'utf-8')
    const part_one_result = solve_day_one(String(data))
    const part_two_result = solve_day_two(String(data))
    console.log(`part one: ${part_one_result}`)
    console.log(`part two: ${part_two_result}`)
}

main()
