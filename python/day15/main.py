def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0
    for group in input_text.strip().split(','):
        group_total = 0
        for i, ch in enumerate(group):
            group_total += ord(ch)
            group_total *= 17
            group_total = group_total % 256
        total += group_total
    return total


def solve_part_two(input_text: str) -> int:
    total = 0
    boxes = {i: [] for i in range(256)}
    for group in input_text.strip().split(','):
        h = 0
        label = ''
        
        i = 0

        while i < len(group):
            if group[i] == '-':
                boxes[h] = list(filter(lambda x: x[0] != label, boxes[h]))
                break

            if group[i] == '=':
                added = False
                for ii, item in enumerate(boxes[h]):
                    if item[0] == label:
                        boxes[h][ii] = (label, int(group[i + 1]))
                        added = True
                if not added:
                    boxes[h].append((label, int(group[i + 1])))
                break

            label += group[i]
            h += ord(group[i])
            h *= 17
            h = h % 256
            i += 1


    for box, contents in boxes.items():
        box_total = 0
        for i, lens in enumerate(contents, 1):
            box_total += (int(box) + 1) * i * lens[1]
        total += box_total
    return total

if __name__ == '__main__':
    raise SystemExit(main())

