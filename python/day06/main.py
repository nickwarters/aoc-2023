import re


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0

    times = [int(x) for x in input_text.splitlines()[0].removeprefix('Time:').split(' ') if x != '']
    distances = [int(x) for x in input_text.splitlines()[1].removeprefix('Distance:').split(' ') if x != '']
    
    for t, r in zip(times, distances):
        c = 0
        for n in range(1, t):
            d = n * (t - n)
            if d > r:
                c += 1
        total = c if total == 0 else total * c


    return total


def solve_part_two(input_text: str) -> int:
    total = 0

    allowed_time = int(''.join([x for x in input_text.splitlines()[0].removeprefix('Time:').split(' ') if x != '']))
    record = int(''.join([x for x in input_text.splitlines()[1].removeprefix('Distance:').split(' ') if x != '']))
    
    c = 0
    for n in range(1, allowed_time):
        d = n * (allowed_time- n)
        if d > record:
            c += 1
      

    return c

if __name__ == '__main__':
    raise SystemExit(main())

