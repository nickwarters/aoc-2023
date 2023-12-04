import re


def main():
    input_text = open(0).read()
    print(f'part one: {solve_part_one(input_text)}')
    print(f'part two: {solve_part_two(input_text)}')

def solve_part_one(input_text: str) -> int:
    total = 0
    for card in input_text.splitlines():
        card_total = 0
        winners, have = card[card.find(': '):].split(' | ')
        winners = winners.split(' ')
        have = have.split(' ')
        for h in have:
            if h == '':
                continue
            if h in winners:
                card_total = 1 if card_total == 0 else card_total * 2
        total += card_total
    return total


def solve_part_two(input_text: str) -> int:
    card_count = {}
    cards = input_text.splitlines()
    final_cards = []

    for card_id, card in enumerate(cards, 1):
        final_cards.append(card)
        if card_id not in card_count:
            card_count[card_id] = 1
        else:
            card_count[card_id] += 1
        card_total = 0
        winners, have = card[card.find(': '):].split(' | ')
        winners = winners.split(' ')
        have = have.split(' ')
        for _ in range(card_count[card_id]):
            for h in have:
                if h == '':
                    continue
                if h in winners:
                    card_total += 1
            for i in range(1, card_total + 1):
                
                if card_id + i in card_count:
                    card_count[card_id + i] += 1
                else:
                    card_count[card_id + i] = 1

                card_total -= 1
    return sum(card_count.values())

if __name__ == '__main__':
    raise SystemExit(main())

