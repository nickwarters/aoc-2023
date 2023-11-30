function solve_day_one(input: string): number {
	console.log(input)
	return 0
}

function solve_day_two(input: string): number {
	console.log(input)
	return 0
}

process.stdin.on('data', (input) => {
	const part_one_result = solve_day_one(String(input))
	const part_two_result = solve_day_two(String(input))
	console.log(`part one: ${part_one_result}`)
	console.log(`part two: ${part_two_result}`)
})
