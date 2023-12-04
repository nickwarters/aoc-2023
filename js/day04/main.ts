import fs from 'fs'

function solve_day_one(input: string): number {
    let total = 0

    total = input
        .trim()
        .split('\n')
        .reduce((t, card) => {
            let cardTotal = 0
            const [winners, have] = card
                .replace(/Card \d{1,}: /, '')
                .split(' | ')
                .map(s => s.split(' '))

            have.forEach(h => {
                if (h === '') {
                    return
                }

                if (winners.includes(h)) {
                    cardTotal = cardTotal ? cardTotal * 2 : 1
                }
            })

            return t + cardTotal
        }, total)
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
