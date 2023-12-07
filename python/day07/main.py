from collections import Counter, defaultdict
import re
from typing import List, Tuple


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0
    card_ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    type_ranks = ['h', '1', '2', '3', 'f', '4', '5']
    card_ranks.reverse()
    hand_scores = []

    for i, hand in enumerate(input_text.splitlines()):

        h, bid = hand.split(' ')
        counter = Counter(h)
        card_scores = [card_ranks.index(x) for x in h]
        # print(f'{counter=}, {max(counter.values())=}, {len(counter)=}')
        t = ''
        if max(counter.values()) == 5:
            t = '5'
            
        elif max(counter.values()) == 4:
            t = '4'

        elif max(counter.values()) == 3 and len(counter) == 2:
            t = 'f'

        elif max(counter.values()) == 3 and len(counter) == 3:
            t = '3'

        elif max(counter.values()) == 2 and len(counter) == 3:
            t = '2'

        elif max(counter.values()) == 2 and len(counter) == 4:
            t = '1'

        elif len(counter) == 5:
            t = 'h'
        else:
            raise ValueError('uh oh')

        hand_scores.append((h, t, card_scores, int(bid)))


    def sort(item: Tuple[str, str, List[int], int]):
        # print(item)
        return (type_ranks.index(item[1]), item[2])
    
    # print(hand_scores)

    total = sum([ i * x[3] for i, x in enumerate(sorted(hand_scores, key=sort), 1)])

    

    return total


def solve_part_two(input_text: str) -> int:
    total = 0
    card_ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    type_ranks = ['h', '1', '2', '3', 'f', '4', '5']
    card_ranks.reverse()
    hand_scores = []

    for i, hand in enumerate(input_text.splitlines()):

        h, bid = hand.split(' ')
        counter = Counter(h)
        card_scores = [card_ranks.index(x) for x in h]
        # print(f'{counter=}, {max(counter.values())=}, {len(counter)=}')
        t = ''

        match (max(counter.values()), len(counter)):
            case (5, _):
                t = '5'
            case (4, _):
                if 'J' in counter:
                    t = '5'
                else:
                    t = '4'
            case (3,2):
                if 'J' in counter:
                    t = '5'
                else:
                    t = 'f'
            case (3, 3):
                if 'J' in counter:
                    if counter['J'] == 1:
                        t = '4'
                    else:
                        t = '3'
                else:
                    t = '3'

            case (2, 3):
                if 'J' in counter:
                    t = '4'
                else:
                    t = '2'

            case (2 , 4):
                if 'J' in counter:
                    t = '3'
                else:
                    t = '1'

            case (_, 5):
                if 'J' in counter:
                    t = '1'
                else:
                    t = 'h'
            case _:
                raise ValueError('uh oh')
        

        hand_scores.append((h, t, card_scores, int(bid)))


    def sort(item: Tuple[str, str, List[int], int]):
        # print(item)
        return (type_ranks.index(item[1]), item[2])
    
    # print(hand_scores)

    total = sum([ i * x[3] for i, x in enumerate(sorted(hand_scores, key=sort), 1)])

    

    return total

if __name__ == '__main__':
    raise SystemExit(main())

