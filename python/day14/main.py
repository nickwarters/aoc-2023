

from typing import Counter


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




def solve_part_two(input_text: str) -> int:
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

if __name__ == '__main__':
    raise SystemExit(main())

