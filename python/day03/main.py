import re
from typing import Generator, Tuple

def main():
    input_text = open(0).read()
    
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')


def get_neighbours_8(x: int, y: int) -> Generator[Tuple[int, int], None, None]:
    for xd in (-1, 0, 1):
        for yd in (-1, 0, 1):
            if xd == yd == 0:
                continue
            yield x + xd, y + yd

def get_neighbours_4(x: int, y: int) -> Generator[Tuple[int, int], None, None]: 
    yield x - 1, y
    yield x, y - 1
    yield x, y + 1
    yield x + 1, y


def solve_part_one(input_text: str):
    grid = input_text.split('\n')
    total = 0
    for r, row in enumerate(grid):
        matches = re.compile(r'\d{1,}').finditer(row)
        for m in matches:
            match_used = False
            for m_c in range(m.start(), m.end()):
                if match_used:
                    break
                for nr, nc in get_neighbours_8(r, m_c):
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(row):
                        continue
                    x: str = grid[nr][nc] 
                    if x != '.' and not x.isdigit():
                        total += int(m.group(0))
                        match_used = True
                        break    
    
    return total


def solve_part_two(input_text: str):
    grid = input_text.split('\n')
    total = 0
 

    gears = []
    nums = []
    for r, row in enumerate(grid):
        gear_matches = re.compile(r'\*').finditer(row)
        for g in gear_matches:
            gears.append((r, g.start()))

        num_matches = list(re.compile(r'\d{1,}').finditer(row))
       
        for n in num_matches:
            nums.append((int(n.group(0)), r, n.start(), n.end() - 1))

    for g in gears:
        g_nums = []
        for n in nums:
            for nc in range(n[2] - 1, n[3] + 2):
                if g[1] == nc and g[0] in range(n[1] - 1, n[1] + 2):
                    g_nums.append(n[0])
                    break
        if len(g_nums) == 2:
            total += g_nums[0] * g_nums[1]

    return total

if __name__ == '__main__':
    raise SystemExit(main())

