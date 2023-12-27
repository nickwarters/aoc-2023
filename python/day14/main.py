

from typing import Counter, List, Tuple


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0
    grid = [list(line) for line in input_text.splitlines()]
    
    new_positions = set()
    freed_positions = set()

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in ('#', '.'):
                continue
        
            rr = r - 1
            while True:
                if rr < 0 or grid[rr][c] == '#' or (rr, c) in new_positions:
                    new_positions.add((rr + 1, c))
                    break

                rr -= 1

    counter = Counter([x[0] for x in new_positions])
    total = sum([(len(grid) - k) * v for k, v in counter.items()])

    return total


def find_new_position(grid: Tuple) -> Tuple:
    for _ in range(4):
        grid = tuple(map(''.join, zip(*grid)))
        grid = tuple('#'.join(''.join(sorted(list(g), reverse=True)) for g in row.split('#')) for row in grid)
        grid = tuple(r[::-1] for r in grid)
    return grid



def solve_part_two(input_text: str) -> int:
    total = 0
    grid = tuple(input_text.splitlines())
    seen = {grid}
    seen_ind = [grid]
    count = 0

    while True:

        grid = find_new_position(grid)

        count += 1
        if grid in seen:
            break
        # printgrid(grid)
        seen.add(grid)
        seen_ind.append(grid)

    first = seen_ind.index(grid)
    cycle = count - first
    index = (1000000000 - first) % cycle + first

    print(f'{first=}, {cycle=}, {count=}, {index=}')
    entry = seen_ind[index]
    counts = [r.count('O') * (len(entry) - i) for i, r in enumerate(entry)]
    total = sum(counts)

    return total

if __name__ == '__main__':
    raise SystemExit(main())

