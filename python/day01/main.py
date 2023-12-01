import re

def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str):
    
    total = 0

    try:
    
        for i, line in enumerate(input_text.split('\n')):
            if line == '':
                continue
            
            digits = re.findall('\d', line)
            total += int(digits[0] + digits[-1])
    finally:

        return total


def solve_part_two(input_text: str):
    total = 0

    number_map = (
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    )
    
    for i, line in enumerate(input_text.split('\n')):
        if line == '':
            continue
        
        for i, s in enumerate(number_map):
            line = line.replace(s, s[0] + str(i +1) + s[-1])
        
        digits = re.findall('\d', line)

        total += int(digits[0] + digits[-1])

    return total

if __name__ == '__main__':
    raise SystemExit(main())

