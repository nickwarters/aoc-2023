import math
from collections import Counter
from typing import List, Tuple


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')


def solve_part_one(input_text: str) -> int:
    total = 0
    seeds = [int(x) for x in input_text.split('\n\n')[0].replace('seeds: ', '').split(' ')]
    seed_map = {}
    for s in seeds:

        source = s
        d = source
        for section in [x.splitlines()[1:] for x in input_text.split('\n\n')[1:]]:
           
            for row in section:
                d_start, s_start, r = list(map(int, row.split(' ')))
                
                if s_start < source < (s_start + r):
                    if d_start > s_start:
                        offset = d_start - s_start
                        m = 1
                    else:
                        offset = s_start - d_start
                        m = -1
                    d = source + offset * m
            source = d
        seed_map[s] = d

    total = min(seed_map.values())

    return total


def map_to_many(seed_ranges: List[Tuple[int, int]], maps: List[str]) -> List[Tuple[int, int]]:
    mapped = []
    for row in maps:
        ds, ss, r = list(map(int, row.split(' ')))
        se = ss + r
        new = []
        while seed_ranges:
            s, e = seed_ranges.pop()
            b = (s, min(e, ss))
            i = (max(s, ss), min(se, e))
            a = (max(se, s), e)
            
            if i[1] > i[0]:
                mapped.append((i[0] + ds - ss, i[1] + ds - ss))

            if b[0] < b[1]:
                new.append(b)

            if a[0] < a[1]:
                new.append(a)

        seed_ranges = new

    return mapped + seed_ranges


def solve_part_two(input_text: str) -> int:
    seedsies = [int(x) for x in input_text.split('\n\n')[0].replace('seeds: ', '').split(' ')]
    seeds = []
    for i in range(0, len(seedsies), 2):
        seeds.append((seedsies[i], seedsies[i + 1]))

    sections = [x.splitlines()[1:] for x in input_text.split('\n\n')[1:]]
    dests = []
    for s, c in seeds:
        start = [(s, s+c)]
        for section in sections:
            start = map_to_many(start, section)
        dests.append(min(start)[0])

    return min(dests)


if __name__ == '__main__':
    raise SystemExit(main())

