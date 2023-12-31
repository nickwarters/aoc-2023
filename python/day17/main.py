import time
from typing import List, Set, Tuple

import pytest

def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')


def test_solve_part_one():
    s = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''
    expected = 102
    result = solve_part_one(s)
    assert result == expected


@pytest.mark.parametrize(
    's, expected', 
    [
        (
            '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533''', 94
        ),
        (
        '''111111111111
999999999991
999999999991
999999999991
999999999991''', 71
        )

    ]
)
def test_solve_part_two(s, expected):
    result = solve_part_two(s)
    assert result == expected


def solve_part_one(input_text: str) -> int:
    total = 0
    grid = [list(map(int, r)) for r in input_text.splitlines()]

    start = (0, 0, 0, 0, 0, 0)
    dest = (len(grid) - 1, len(grid[0]) - 1)
    queue: List[Tuple[int, int, int, int, int, int]] = [start]
    seen: Set[Tuple[int, int, int, int, int]] = set()

    while queue:
        t, r, c, dr, dc, n = queue.pop()
        
        if (r, c, dr, dc, n) in seen:
            continue


        if (r, c) == dest:
            total = t
            break

        seen.add((r, c, dr, dc, n))
        
        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                queue.append((t + grid[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (dr, dc) == (-ndr, -ndc) or (dr, dc) == (ndr, ndc):
                continue

            nr = r + ndr
            nc = c + ndc
            
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue

            queue.append((t + grid[nr][nc], nr, nc, ndr, ndc, 1))

        queue = sorted(queue, reverse=True)

    return total


def solve_part_two(input_text: str) -> int:
    total = 0
    grid = [list(map(int, r)) for r in input_text.splitlines()]

    start = (0, 0, 0, 0, 0, 0)
    dest = (len(grid) - 1, len(grid[0]) - 1)
    queue: List[Tuple[int, int, int, int, int, int]] = [start]
    seen: Set[Tuple[int, int, int, int, int]] = set()

    while queue:
        t, r, c, dr, dc, n = queue.pop()
        
        if (r, c, dr, dc, n) in seen:
            continue


        if (r, c) == dest and n >= 4:
            total = t
            break

        seen.add((r, c, dr, dc, n))
        
        if n < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                queue.append((t + grid[nr][nc], nr, nc, dr, dc, n + 1))
        if n < 4 and (dr, dc) != (0, 0):
            continue

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (dr, dc) == (-ndr, -ndc) or (dr, dc) == (ndr, ndc):
                continue

            nr = r + ndr
            nc = c + ndc
            
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue

            queue.append((t + grid[nr][nc], nr, nc, ndr, ndc, 1))

        queue = sorted(queue, reverse=True)

    return total

if __name__ == '__main__':
    raise SystemExit(main())

