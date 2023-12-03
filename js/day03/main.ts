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
}

function solve_day_one(input: string): number {
    let total = 0

    const grid = input.split('\n')

    const symbols: S[] = []
    const numbers: N[] = []

    const allNumbers = '1234567890'

    grid.forEach((row, r, rows) => {
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

            if ((c == grid[0].length - 1 && isNumber) || (!isNumber && num != '')) {
                numbers.push({
                    value: Number(num),
                    row: r,
                    start: numStart,
                    end: c - 1,
                })

                num = ''
                numStart = 0
                isValid = false
            }
        })
    })
    total = numbers
        .filter(n => {
            let isValid = false

            for (let sr = n.row - 1; sr < n.row + 2 && sr < grid.length; sr++) {
                for (let sc = n.start - 1; sc < n.end + 2; sc++) {
                    if (sr < 0 || sc < 0) {
                        continue
                    }
                    if (grid[sr][sc] !== '.' && !allNumbers.includes(grid[sr][sc])) {
                        isValid = true
                    }
                }
            }
            return isValid
        })
        .reduce((sum, n) => sum + n.value, 0)

    return total
}

function solve_day_two(input: string): number {
    let total = 0

    const grid = input.split('\n')

    const symbols: S[] = []
    const numbers: N[] = []

    const allNumbers = '1234567890'

    grid.forEach((row, r, rows) => {
        let inNum = false
        let num = ''
        let numStart = 0

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
                if (ch === '*') {
                    symbols.push({
                        row: r,
                        column: c,
                        value: '*',
                    })
                }
            }

            if ((c == grid[0].length - 1 && isNumber) || (!isNumber && num != '')) {
                numbers.push({
                    value: Number(num),
                    row: r,
                    start: numStart,
                    end: c - 1,
                })

                num = ''
                numStart = 0
            }
        })
    })

    total = symbols.reduce((t, s) => {
        const g_nums = []

        for (const n of numbers) {
            if (n.row - 1 <= s.row && n.row + 1 >= s.row && n.start - 1 <= s.column && n.end + 1 >= s.column) {
                g_nums.push(n)
            }
        }

        if (g_nums.length == 2) {
            t += g_nums[0].value * g_nums[1].value
        }
        return t
    }, 0)

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
