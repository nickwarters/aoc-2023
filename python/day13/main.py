from typing import List

def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')


def solve_part_one(input_text: str) -> int:
    total = 0
    total_cols_before = 0
    total_rows_before = 0
    for i, block in enumerate(input_text.split('\n\n')):
        rows = block.splitlines()
        cols = [''.join([line[c] for line in block.splitlines()]) for c in range(len(block.splitlines()[0]))]
        possible_mirror_rows = []
        possible_mirror_cols = []

        for r in range(0, len(rows) - 1):
            if rows[r] == rows[r + 1]:
                possible_mirror_rows.append(r)
        for c in range(0, len(cols) - 1):
            if cols[c] == cols[c + 1]:
                possible_mirror_cols.append(c)

        for possible_mirror_row in possible_mirror_rows:

            actual_mirror_row = True
            if possible_mirror_row is not None:
                left, right = rows[:possible_mirror_row + 1], rows[possible_mirror_row + 1:]
                left.reverse()
                for lr, rr in zip(left, right):
                    if rr != lr:
                        actual_mirror_row = False
                        break

            if actual_mirror_row:
                total_rows_before += possible_mirror_row + 1

                break

        for possible_mirror_col in possible_mirror_cols:
            actual_mirror_col = True
            if possible_mirror_col is not None:
                left, right = cols[:possible_mirror_col + 1], cols[possible_mirror_col + 1:]
                left.reverse()
                for lr, rr in zip(left, right):
                    if rr != lr:
                        actual_mirror_col = False
                        break

            if actual_mirror_col and possible_mirror_col is not None:
                total_cols_before += possible_mirror_col + 1
                break

    total = total_cols_before + 100 * total_rows_before
    return total


def attempt_comparisons(left: str, right: str) -> bool:
    for i in range(len(left)):
        new_left_c = '.' if left[i] == '#' else '#'
        new_right_c = '.' if right[i] == '#' else '#'
        new_left = left[:i] + new_left_c + left[i+1:]
        new_right = right[:i] + new_right_c + right[i+1:]
        if new_left == right or new_right == left:
            return True

    return False


def get_diff_index(arr: List[str], allowed_diffs: int) -> int:
    for r in range(len(arr)):
        count = 0
        left = arr[:r][::-1]
        right = arr[r:]
        for l_row, r_row in zip(left, right):
            for lr, rr in zip(l_row, r_row):
                count += int(lr != rr)

        if count == allowed_diffs:
            return r
    return 0


def solve_part_two(input_text: str) -> int:
    total = 0
    for _, block in enumerate(input_text.split('\n\n'), 1):
        rows = block.splitlines()
        cols = [''.join([line[c] for line in block.splitlines()]) for c in range(len(block.splitlines()[0]))]
        row_ind = get_diff_index(rows, 1)
        total += 100 * row_ind
        if not row_ind:
            total += get_diff_index(cols, 1)

    return total


if __name__ == '__main__':
    raise SystemExit(main())

