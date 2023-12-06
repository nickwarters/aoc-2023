import fs from 'fs'

function solve_day_one(input: string): number {
    const [times, records] = input.split('\n').map(x =>
        x
            .split(' ')
            .map(n => parseInt(n))
            .filter(n => !isNaN(n))
    )

    let total = 0

    for (let i = 0; i < times.length; i++) {
        const [time, record] = [times[i], records[i]]
        let c = 0
        for (let n = 1; n < time; n++) {
            const distance = n * (time - n)
            if (distance > record) {
                c++
            }
        }

        total = total ? total * c : c
    }

    return total
}

function solve_day_two(input: string): number {
    const [time, record] = input.split('\n').map(x =>
        parseInt(
            x
                .split(' ')
                .filter(n => !isNaN(parseInt(n)))
                .join('')
        )
    )

    let total = 0

    let c = 0
    for (let n = 1; n < time; n++) {
        const distance = n * (time - n)
        if (distance > record) {
            total++
        }
    }

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
