def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0
    coords = []
    start = (0, 0)
    current = start
    coords.append(current)
    dir_map = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    for line in input_text.splitlines():
        d, c, _ = line.split(' ')
        current = (current[0] + dir_map[d][0] * int(c), current[1] + dir_map[d][1] * int(c))
        coords.append(current)

    min_r = 0 
    max_r = 0
    min_c = 0 
    max_c = 0

    for r, c in coords:


    print(f'{coords=}, {total=}')

    return total


def solve_part_two(input_text: str) -> int:
    total = 0

    return total

if __name__ == '__main__':
    raise SystemExit(main())

