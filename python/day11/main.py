from itertools import combinations


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0

    grid = input_text.splitlines()
    GALAXY = '#'
    galaxies = []
    empty_rows = []
    

    cols = [False for _ in grid[0]]
    
    r = 0

    for r, row in enumerate(grid):
        if row.count(GALAXY) == 0:
            empty_rows.append(r)
            continue

        for c in range(0, len(cols)):
            if grid[r][c] == GALAXY:
                cols[c] = True
                galaxies.append((r, c))

    empty_cols = [c for c, v in enumerate(cols) if not v]


    for (r_a, c_a), (r_b, c_b) in combinations(galaxies, 2):
        for r in range(min(r_a, r_b), max(r_a, r_b)):
            total += 2 if r in empty_rows else 1
        for c in range(min(c_a, c_b), max(c_a, c_b)):
            total += 2 if c in empty_cols else 1

    return total


def solve_part_two(input_text: str) -> int:
    total = 0

    grid = input_text.splitlines()
    GALAXY = '#'
    galaxies = []
    empty_rows = []
    

    cols = [False for _ in grid[0]]
    
    r = 0

    for r, row in enumerate(grid):
        if row.count(GALAXY) == 0:
            empty_rows.append(r)
            continue

        for c in range(0, len(cols)):
            if grid[r][c] == GALAXY:
                cols[c] = True
                galaxies.append((r, c))

    empty_cols = [c for c, v in enumerate(cols) if not v]


    for (r_a, c_a), (r_b, c_b) in combinations(galaxies, 2):
        for r in range(min(r_a, r_b), max(r_a, r_b)):
            total += 1_000_000 if r in empty_rows else 1
        for c in range(min(c_a, c_b), max(c_a, c_b)):
            total += 1_000_000 if c in empty_cols else 1

    return total

if __name__ == '__main__':
    raise SystemExit(main())

