import re
from typing import List, Tuple


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

Point = Tuple[int, int]
def get_possible_paths(g: List[str], pos: Point, prev: Point) -> List[Point]:
    paths = []
    current = g[pos[0]][pos[1]]

    up_down = ((-1, 0), (1, 0))
    right_left = ((0, -1), (0, 1))
    right_down = ((1, 0), (0, 1))
    left_down = ((1, 0), (0, -1))
    right_up = ((-1, 0), (0, 1))
    left_up = ((-1, 0), (0, -1))

    possible_dirs = {
        'F': right_down,
        'J': left_up,
        '-': right_left,
        '|': up_down,
        '7': left_down,
        'L': right_up
    }

    if current == 'S':
        for direction in (*up_down, *right_left):
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos == prev:
                continue
            if new_pos[0] < 0 or new_pos[0] >= len(g) or new_pos[1] < 0 or new_pos[1] >= len(g[0]):
                continue
            if g[new_pos[0]][new_pos[1]] == '.':
                continue

            allowed = False
            
            if direction[0] == -1 and g[new_pos[0]][new_pos[1]] in 'F7|':
                allowed = True
            elif direction[0] == 1 and g[new_pos[0]][new_pos[1]] in '|LJ':
                allowed = True
            elif direction[1] == -1 and g[new_pos[0]][new_pos[1]] in 'L-F':
                allowed = True
            elif direction[1] == 1 and g[new_pos[0]][new_pos[1]] in 'J-7':
                allowed = True

            if allowed :
                paths.append(new_pos)
            
        return paths



    for i, direction in  enumerate(possible_dirs[current]):
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos == prev:
            continue
        if new_pos[0] < 0 or new_pos[0] >= len(g) or new_pos[1] < 0 or new_pos[1] >= len(g[0]):
            continue
        new_char = g[new_pos[0]][new_pos[1]]
              
        if new_char == '.':
            continue

        allowed = False
        if current == '|' and new_char == '|':
            allowed = True
        elif current == '|' and direction[0] == 1 and new_char in 'LJ':
            allowed = True
        elif current == '|' and new_char in 'F7':
            allowed = True

        elif current == '-' and new_char in '-':
            allowed = True
        elif current == '-' and direction[1] == 1 and new_char in 'J7':
            allowed = True
        elif current == '-' and new_char in 'FL':
            allowed = True
        

        elif current == 'F' and direction[0] == 1 and new_char in 'LJ|':
            allowed = True
        elif current == 'F' and new_char in '7-J':
            allowed = True

        elif current == 'J' and direction[0] == -1 and new_char in '|F7':
            allowed = True
        elif current == 'J' and new_char in '-FL':
            allowed = True

        elif current == '7' and direction[0] == 1 and new_char in 'LJ|':
            allowed = True
        elif current == '7' and new_char in 'L-F':
            allowed = True

        elif current == 'L' and direction[0] == -1 and new_char in '|F7':
            allowed = True
        elif current == 'L' and new_char in '-J7':
            allowed = True
        elif new_char == 'S':
            allowed = True

        if allowed:
            paths.append(new_pos)
                
    return paths


def solve_part_one(input_text: str) -> int:
    total = 0
    grid = input_text.splitlines()
    START = 'S'
    start_pos = None
    for r, row in enumerate(grid):
        for c in range(0, len(row)):
            if row[c] == START:
                start_pos = (r, c)
                break
   
    current_char = None
    prev_pos = start_pos

    while current_char != START:
        
        paths = get_possible_paths(grid, start_pos, prev_pos)
       
        prev_pos = start_pos
       
        start_pos = paths[0]
        current_char = grid[start_pos[0]][start_pos[1]]
        total += 1

    return int(total / 2)


def solve_part_two(input_text: str) -> int:
    total = 0
    seen = set()

    grid = input_text.splitlines()
    START = 'S'
    start_pos = None
    for r, row in enumerate(grid):
        for c in range(0, len(row)):
            if row[c] == START:
                start_pos = (r, c)
                break
   
    current_char = None
    prev_pos = start_pos

    start_paths = get_possible_paths(grid, start_pos, prev_pos)
    start_c = None
    if start_paths[0][0] == start_paths[1][0]:
        start_c = '-' if start_paths[0][0] == 0 else '|'
    elif start_paths[0][0] < start_paths[1][0]:
        start_c = 'L' if start_paths[0][1] == 1 else 'J'
    else:
        start_c = 'F' if start_paths[0][1] == 1 else '7'

    assert start_c is not None

    while current_char != START:
        
        paths = get_possible_paths(grid, start_pos, prev_pos)
        
        prev_pos = start_pos
        seen.add(prev_pos)
        start_pos = paths[0]
        current_char = grid[start_pos[0]][start_pos[1]]
        

    check_for = 'L|J'
    for r, row in enumerate(grid):
        
        for c in range(0, len(row)):
            if (r, c) in seen:
                continue
            
            count = 0
            for c2, x in enumerate(row[:c]):
                if (r, c2) in seen and row[c2] in check_for:
                    count += 1

            matches = [(r,c2) for c2, x in enumerate(row[:c]) if (not (r, c2)  in seen) and row[c2] in check_for]
            
            total += int(count % 2 == 1)

    return total

if __name__ == '__main__':
    raise SystemExit(main())

