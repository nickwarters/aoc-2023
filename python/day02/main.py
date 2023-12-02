def main():
    input_text = open(0).read()
    
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str):
    game_limits = {'red': 12, 'green': 13, 'blue': 14}
    
    total = 0
    
    lines = input_text.splitlines()
    for line in lines:
        game, hands = line.split(': ')
        game_id = int(game.removeprefix('Game '))
        game_possible = True
        for hand in hands.split('; '):
            if not game_possible:
                break
            cubes = hand.split(', ')
            for cube in cubes:
                count, colour = cube.split(' ')
                if int(count) > game_limits[colour]:
                    game_possible = False
                    break
        if game_possible:
            total += game_id
    return total


def solve_part_two(input_text: str):
    total = 0
    lines = input_text.splitlines()
    for line in lines:
        game, hands = line.split(': ')
        game_id = int(game.removeprefix('Game '))
        game_mins = {}
        for hand in hands.split('; '):
            cubes = hand.split(', ')
            for cube in cubes:
                count, colour = cube.split(' ')
                if colour in game_mins:
                    game_mins[colour] = max(game_mins[colour], int(count))
                else:
                    game_mins[colour] = int(count)
        total += game_mins['green'] * game_mins['red'] * game_mins['blue']
        
    
    return total

if __name__ == '__main__':
    raise SystemExit(main())

