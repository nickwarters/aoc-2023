from typing import List


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')



def count_variations(springs: str, broken_springs: List[int], i: int, bi: int, c: int, cache: dict):
    key = (i, bi, c)
    
    if key in cache:
        return cache[key]

    if i == len(springs):
        if len(broken_springs) == bi and c == 0: 
            # got all of the broken springs needed so this is a valid combination - last character IS NOT the end of the last count of broken springs
            return 1
        
        if len(broken_springs) - 1  == bi and broken_springs[bi] == c:
            # got all of the broken springs needed so this is a valid combination - last character IS the end of the last count of broken springs
            return 1
        
        # not satisfied all the broken springs so this is invalid

        return 0
    

    count = 0

    for ch in ('.', '#'):
        if springs[i] == ch or springs[i] == '?':
            if ch == '.' and c == 0:
                # nothing we can do, move on
                count += count_variations(springs, broken_springs, i + 1, bi, c, cache)
            elif ch == '.' and bi < len(broken_springs) and c > 0 and broken_springs[bi] == c:
                # we have reached the end of a set of possibly broken and known 
                # broken springs. Start checking for the next group of springs 
                # and reset the count
                count += count_variations(springs, broken_springs, i + 1, bi + 1, 0, cache)
            elif ch == '#':
                # either the spring is known broken, or possibly broken, using 
                # the current broken index we are checking for, increment the 
                # broken count
                count += count_variations(springs, broken_springs, i + 1, bi, c + 1, cache)
    
    cache[key] = count
    return count




def solve_part_one(input_text: str) -> int:
    total = 0
    for i, line in enumerate(input_text.splitlines()):
        all_springs = line.split(' ')[0]
        broken_springs = list(map(int, line.split(' ')[1].split(',')))
 
        total += count_variations(all_springs, broken_springs, 0, 0, 0, {})

    return total


def solve_part_two(input_text: str) -> int:
    total = 0

    for i, line in enumerate(input_text.splitlines()):

        all_springs = '?'.join([line.split(' ')[0] for _ in range(5)])
        broken_springs = list(map(int, line.split(' ')[1].split(','))) * 5
        
        total += count_variations(all_springs, broken_springs, 0, 0, 0, {})

    return total

if __name__ == '__main__':
    raise SystemExit(main())

