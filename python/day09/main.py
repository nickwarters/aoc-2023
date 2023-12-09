import re


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0

    for i, line in enumerate(input_text.splitlines()):
        nums = [int(x) for x in line.split()]
        diffs = []
        while True:
            if diffs and sum(diffs[-1]) == 0:
                break
            
            start = nums if not diffs else diffs[-1]
            d = [start[ind] - start[ind -1] for ind in range(1, len(start))]
            diffs.append(d)
        ind = len(diffs) - 1
        while ind > 0:
            diffs[ind - 1].append(diffs[ind - 1][-1] + diffs[ind][-1])
            ind -= 1

        nums.append(nums[-1] + diffs[0][-1])
        total += nums[-1]
                    
            

    return total


def solve_part_two(input_text: str) -> int:
    total = 0

    for i, line in enumerate(input_text.splitlines()):
        nums = [int(x) for x in line.split()]
        diffs = []
        while True:
            if diffs and sum(diffs[-1]) == 0:
                break
            
            start = nums if not diffs else diffs[-1]
            d = [start[ind] - start[ind -1] for ind in range(1, len(start))]
            diffs.append(d)
        ind = len(diffs) - 1
        while ind > 0:
            diffs[ind - 1].insert(0, diffs[ind - 1][0] - diffs[ind][0])
            ind -= 1

        nums.insert(0, nums[0] - diffs[0][0])
        total += nums[0]

    return total

if __name__ == '__main__':
    raise SystemExit(main())

