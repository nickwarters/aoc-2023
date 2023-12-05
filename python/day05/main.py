import re


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


def solve_part_two(input_text: str) -> int:
    seedsies = [int(x) for x in input_text.split('\n\n')[0].replace('seeds: ', '').split(' ')]
    seeds = []
    for i, s in enumerate(seedsies):
        if i % 2 != 0:
            seeds.append((seedsies[i - 1], s))
    seed_map = {}
    for seed_s, seed_r in seeds:
        for s in range(seed_s, seed_s + seed_r):
            source = s
            d = source
            for section in [x.splitlines()[1:] for x in input_text.split('\n\n')[1:]]:
                for row in section:
                    d_start, s_start, r = list(map(int, row.split(' ')))

                    if s_start <= source < (s_start + r):
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


if __name__ == '__main__':
    raise SystemExit(main())

