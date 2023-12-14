

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


def find_new_position(grid: List[List[str]], r: int, c: int, d: Tuple[int, int]) -> List[List[str]]:
    if grid[r][c] in ('#', '.'):
        return grid
    new_pos = [r + d[0], c + d[1]]
    while True:
        if new_pos[0] < 0 or new_pos[0] == len(grid) or new_pos[1] < 0 or new_pos[1] == len(grid[0]) or grid[new_pos[0]][new_pos[1]] in ('#', 'O'):
            grid[r][c] = '.'
            print(f'moving ({r},{c}) -> ({new_pos[0] - d[0]}, {new_pos[1] - d[1]})')
            grid[new_pos[0] - d[0]][new_pos[1] - d[1]] = 'O'
            break

        new_pos[0] += d[0]
        new_pos[1] += d[1]
    return grid


def printgrid(grid: List[List[str]]) -> None:
    for row in grid:
        print(row)
    print('------')


def solve_part_two(input_text: str) -> int:
    total = 0
    grid = list(list(line) for line in input_text.splitlines())
    seen = []
    count = 0
    print('START GRID')
    printgrid(grid)
    
    while True:
        if count == 2000:
            break

        for d in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            start_r = 0 if d[0] <= 0 else len(grid) - 1
            end_r = len(grid) if d[0] <= 0 else -1
            start_c = 0 if d[1] <= 0 else len(grid[0]) - 1
            end_c = len(grid[0]) if d[1] <= 0 else - 1
            for r in range(start_r, end_r):
                for c in range(start_c, end_c):
                    grid = find_new_position(grid, r, c, d)
        
        count += 1
        if str(grid) in seen:
            break
        print(f'AFTER {count}')
        printgrid(grid)
        seen.append(str(grid))

    print(f'{count=} to make a loop')
    print(f'{1000000000 % count=}, {len(seen)}')
    counter = Counter([r for r, row in enumerate(seen[(1000000000 % count) - 1]) for c in row if c == 'O'])
    total = sum([(len(grid) - k) * v for k, v in counter.items()])

    return total

if __name__ == '__main__':
    raise SystemExit(main())

