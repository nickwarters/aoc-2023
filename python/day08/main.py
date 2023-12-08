import math
import re


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0
    
    path_map = {}
    path = input_text.split('\n\n')[0]
    for line in input_text.split('\n\n')[1].splitlines():
        k, v = line.split(' = ')
        path_map[k] = v[1:-1].split(', ')

    start = 'AAA'
    end = 'ZZZ'

    while start != end:
        
        for s in path:
            if start == end:
                break
            total += 1
            if s == 'L':
                start = path_map[start][0]
            else:
                start = path_map[start][1]



    return total


def solve_part_two(input_text: str) -> int:
   
    path_map = {}
    path = input_text.split('\n\n')[0]
    for line in input_text.split('\n\n')[1].splitlines():
        k, v = line.split(' = ')
        path_map[k] = v[1:-1].split(', ')

    start_nodes = list(filter(lambda x: x.endswith('A'), path_map.keys()))
    steps = []

    for n in start_nodes:
        t = 0
        start_node = n
        while not start_node.endswith('Z'):
            
            for s in path:

                if start_node.endswith('Z'):
                    break
                t += 1
                if s == 'L':
                    start_node = path_map[start_node][0]
                else:
                    start_node = path_map[start_node][1]
        steps.append(t)

    total = 1
    for n in steps:
        total = (n * total) // (math.gcd(n, total))

    return total

if __name__ == '__main__':
    raise SystemExit(main())

