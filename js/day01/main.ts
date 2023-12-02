import fs from 'fs'

function solve_day_one(input: string, replace: boolean = false): number {
    let total = 0
    const subs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for (let line of input.split('\n')) {
        if (!line) {
            continue
        }

        const linePre = line

        if (replace) {
            for (let i = 0; i < subs.length; i++) {
                line = line.replaceAll(subs[i], subs[i].substring(0, 1) + String(i + 1) + subs[i].substring(subs[i].length - 1))
            }
        }

        const digits = Array.from(line.matchAll(/\d/g))

        total += Number(String(digits[0]) + String(digits[digits.length - 1]))
    }

    return total
}

function solve_day_two(input: string): number {
    return solve_day_one(input, true)
}

function main() {
    const data = fs.readFileSync(0, 'utf-8')
    const part_one_result = solve_day_one(String(data))
    const part_two_result = solve_day_two(String(data))
    console.log(`part one: ${part_one_result}`)
    console.log(`part two: ${part_two_result}`)
}

main()
