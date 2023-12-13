"""
    --- Day 7: Camel Cards ---

    Find the rank of every hand in your set. What are the total winnings?

"""
import time

debug1 = True

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


hand_types = {'five of a kind': 6, 'four of a kind': 5, 'full house': 4, 'three of a kind': 3, 'two pair': 2,
              'one pair': 1, 'high card': 0}
card_ranks = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1,
              '2': 0}


def get_hand_type_score(cards):
    cards = ''.join(sorted(cards))
    if cards[0] == cards[4]:
        return 'five of a kind'
    if cards[0] == cards[3] or cards[1] == cards[4]:
        return 'four of a kind'
    if cards[0] == cards[2] or cards[1] == cards[3] or cards[2] == cards[4]:
        return 'three of a kind'
    if len(set(cards)) == 2:
        return 'full house'
    if len(set(cards)) == 3:
        return 'two pair'
    if len(set(cards)) == 4:
        return 'one pair'
    return 'high card'


def get_card_score(cards):
    return (13**4) * card_ranks[cards[0]] + (13 ** 3) * card_ranks[cards[1]] + (13 ** 2) * card_ranks[cards[2]]\
        + (13**1) * card_ranks[cards[3]] + card_ranks[cards[4]]


def get_rank(cards):
    return (10 ** 6) * hand_types[get_hand_type_score(cards)] + get_card_score(cards)


def get_hands_from_data(data):
    hands = []
    for line in data:
        hands.append({'cards': line.split(' ')[0], 'rank': int(line.split(' ')[1])})
    return hands


def get_answer_1():
    data = read_file('data/07.txt')
    hands = get_hands_from_data(data)
    if debug1:
        print(f'hands: {hands}')

    hands.sort(key=lambda val: get_rank(val['cards']))
    if debug1:
        print(f'hands: {hands}')

    winnings = 0
    for i in range(len(hands)):
        rank = hands[i]['rank']
        amt = (i+1) * rank
        hand = hands[i]['cards']
        print(f'Hand {i+1}: {hand}, rank: {rank}, winnings amt: {amt}')
        winnings += amt

    return winnings


def get_answer_2():
    data = read_file('data/07.txt')
    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 07, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 07, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 07, 1 is not '245782026' ; too low.
    # The Answer to Advent of Code 2023, 07, 1 is
    # The Answer to Advent of Code 2023, 07, 2 is


if __name__ == "__main__":
    main()
