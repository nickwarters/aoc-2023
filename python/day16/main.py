from typing import List, Set, Tuple


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')


def test_solve_part_one():
    input_text = '''.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....'''
    expected = 46
    result = solve_part_one(input_text)
    assert result == expected


def test_solve_part_two():
    input_text = '''.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....'''
    expected = 51
    result = solve_part_two(input_text)
    assert result == expected


def solve_part_one(input_text: str) -> int:
    total = 0
    grid = input_text.splitlines()
    seen: Set[Tuple[Tuple[int, int], str]] = set()
    queue: List[Tuple[Tuple[int, int], str]] = [((0, 0), 'r')]
    out_grid = [list(r) for r in grid]
    out_grid[0][0] = '#'

    while queue:
        current, d = queue.pop()
        if (current, d) in seen:
            continue

        if current[0] < 0 or current[0] >= len(grid) or current[1] < 0 or current[1] >= len(grid[0]):
            continue

        seen.add((current, d))
        out_grid[current[0]][current[1]] = '#'

        ch = grid[current[0]][current[1]]

        if ch == '|' and d in ('l', 'r'):
            queue.append(((current[0] - 1, current[1]), 'u'))
            queue.append(((current[0] + 1, current[1]), 'd'))
        elif ch in ('|', '.') and d == 'u':
            queue.append(((current[0] - 1, current[1]), 'u'))
        elif ch in ('|', '.') and d == 'd':
            queue.append(((current[0] + 1, current[1]), 'd'))
        elif ch == '-' and d in ('u', 'd'):
            queue.append(((current[0], current[1] - 1), 'l'))
            queue.append(((current[0], current[1] + 1), 'r'))
        elif ch in ('-', '.') and d == 'r':
            queue.append(((current[0], current[1] + 1), 'r'))
        elif ch in ('-', '.') and d == 'l':
            queue.append(((current[0], current[1] - 1), 'l'))
        elif ch == '/':
            if d == 'u':
                queue.append(((current[0], current[1] + 1), 'r'))
            elif d == 'd':
                queue.append(((current[0], current[1] - 1), 'l'))
            elif d == 'r':
                queue.append(((current[0] - 1, current[1]), 'u'))
            elif d == 'l':
                queue.append(((current[0] + 1, current[1]), 'd'))
        elif ch == '\\':
            if d == 'u':
                queue.append(((current[0], current[1] - 1), 'l'))
            elif d == 'd':
                queue.append(((current[0], current[1] + 1), 'r'))
            elif d == 'r':
                queue.append(((current[0] + 1, current[1]), 'd'))
            elif d == 'l':
                queue.append(((current[0] - 1, current[1]), 'u'))

    total = len(set(s[0] for s in seen))
    
    return total


def solve_part_two(input_text: str) -> int:
    grid = input_text.splitlines()
    
    starts = [
        *[((0, c), 'd') for c in range(len(grid[0]))],
        *[((r, 0), 'r') for r in range(1, len(grid))],
        *[((len(grid) - 1, c), 'u') for c in range(len(grid[0]))],
        *[((r, len(grid[0]) - 1), 'l') for r in range(len(grid))]
    ]

    results = []

    for start in starts:

        seen: Set[Tuple[Tuple[int, int], str]] = set()
        queue: List[Tuple[Tuple[int, int], str]] = [start]

        while queue:
            current, d = queue.pop()
            if (current, d) in seen:
                continue

            if current[0] < 0 or current[0] >= len(grid) or current[1] < 0 or current[1] >= len(grid[0]):
                continue

            seen.add((current, d))

            ch = grid[current[0]][current[1]]

            if ch == '|' and d in ('l', 'r'):
                queue.append(((current[0] - 1, current[1]), 'u'))
                queue.append(((current[0] + 1, current[1]), 'd'))
            elif ch in ('|', '.') and d == 'u':
                queue.append(((current[0] - 1, current[1]), 'u'))
            elif ch in ('|', '.') and d == 'd':
                queue.append(((current[0] + 1, current[1]), 'd'))
            elif ch == '-' and d in ('u', 'd'):
                queue.append(((current[0], current[1] - 1), 'l'))
                queue.append(((current[0], current[1] + 1), 'r'))
            elif ch in ('-', '.') and d == 'r':
                queue.append(((current[0], current[1] + 1), 'r'))
            elif ch in ('-', '.') and d == 'l':
                queue.append(((current[0], current[1] - 1), 'l'))
            elif ch == '/':
                if d == 'u':
                    queue.append(((current[0], current[1] + 1), 'r'))
                elif d == 'd':
                    queue.append(((current[0], current[1] - 1), 'l'))
                elif d == 'r':
                    queue.append(((current[0] - 1, current[1]), 'u'))
                elif d == 'l':
                    queue.append(((current[0] + 1, current[1]), 'd'))
            elif ch == '\\':
                if d == 'u':
                    queue.append(((current[0], current[1] - 1), 'l'))
                elif d == 'd':
                    queue.append(((current[0], current[1] + 1), 'r'))
                elif d == 'r':
                    queue.append(((current[0] + 1, current[1]), 'd'))
                elif d == 'l':
                    queue.append(((current[0] - 1, current[1]), 'u'))

        total = len(set(s[0] for s in seen))
        results.append(total)
        
    return max(results)

if __name__ == '__main__':
    raise SystemExit(main())

