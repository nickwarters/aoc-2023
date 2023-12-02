import fs from 'fs'

function solve_day_one(input: string): number {
    const gameLimits = {
        red: 12,
        green: 13,
        blue: 14,
    }
    const total = input
        .split('\n')
        .map(line => line.split(': '))
        .map(([game, hands]) => {
            return {
                gameId: Number(game.replace('Game ', '')),
                hands: hands.split('; '),
                possible: true,
            }
        })
        .map(game => {
            game.possible = game.hands.every(hand =>
                hand.split(', ').every(cube => {
                    const [count, colour] = cube.split(' ')
                    return Number(count) <= gameLimits[colour]
                })
            )
            return game
        })
        .reduce((prev, game) => {
            return prev + (game.possible ? game.gameId : 0)
        }, 0)

    return total
}

function solve_day_two(input: string): number {
    const total = input
        .split('\n')
        .map(line => line.split(': '))
        .map(([game, hands]) => {
            return {
                gameMins: { red: 0, green: 0, blue: 0 },
                hands: hands.split('; '),
            }
        })
        .map(game => {
            game.hands.forEach(hand =>
                hand.split(', ').forEach(cube => {
                    const [count, colour] = cube.split(' ')
                    game.gameMins[colour] = Math.max(Number(count), game.gameMins[colour])
                })
            )
            return game
        })
        .reduce((prev, game) => {
            return prev + game.gameMins.red * game.gameMins.green * game.gameMins.blue
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
