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
card_ranks_j = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2,
                '2': 1, 'J': 0}


def get_hand_type_score(cards):
    cards = ''.join(sorted(cards))
    if cards[0] == cards[4]:
        return 'five of a kind'
    if cards[0] == cards[3] or cards[1] == cards[4]:
        return 'four of a kind'
    if len(set(cards)) == 2:
        return 'full house'
    if cards[0] == cards[2] or cards[1] == cards[3] or cards[2] == cards[4]:
        return 'three of a kind'
    if len(set(cards)) == 3:
        return 'two pair'
    if len(set(cards)) == 4:
        return 'one pair'
    return 'high card'


def get_card_score(cards):
    return (13 ** 4) * card_ranks[cards[0]] + (13 ** 3) * card_ranks[cards[1]] + (13 ** 2) * card_ranks[cards[2]] \
        + (13 ** 1) * card_ranks[cards[3]] + card_ranks[cards[4]]


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
        amt = (i + 1) * rank
        cards = hands[i]['cards']
        print(f'Hand {i + 1}: {cards}, rank: {rank}, hand type: {get_hand_type_score(cards)} winnings amt: {amt}')
        winnings += amt

    return winnings


def get_hand_type_score_with_jokers(cards):
    cards = ''.join(sorted(cards))
    j_count = sum([1 for c in cards if c == 'J'])
    if j_count == 0:
        return get_hand_type_score(cards)
    elif j_count >=4:
        return 'five of a kind'
    elif j_count == 3:
        if len(set(cards)) == 2:
            return 'five of a kind'
        else:
            return 'four of a kind'
    elif j_count == 2:
        simple_hand_type = get_hand_type_score(cards)
        if simple_hand_type in ['one pair']:
            return 'three of a kind'
        elif simple_hand_type in ['two pair']:
            return 'four of a kind'
        elif simple_hand_type in ['full house']:
            return 'five of a kind'

    elif j_count == 1:
        simple_hand_type = get_hand_type_score(cards)
        if simple_hand_type in ['high card']:
            return 'one pair'
        elif simple_hand_type in ['one pair']:
            return 'three of a kind'
        elif simple_hand_type in ['two pair']:
            return 'full house'
        elif simple_hand_type in ['three of a kind']:
            return 'four of a kind'
        elif simple_hand_type in ['four of a kind']:
            return 'five of a kind'
    return 'high card'


def get_card_score_with_jokers(cards):
    return (13 ** 4) * card_ranks_j[cards[0]] + (13 ** 3) * card_ranks_j[cards[1]] + (13 ** 2) * card_ranks_j[cards[2]] \
        + (13 ** 1) * card_ranks_j[cards[3]] + card_ranks_j[cards[4]]


def get_rank_with_jokers(cards):
    return (10 ** 6) * hand_types[get_hand_type_score_with_jokers(cards)] + get_card_score_with_jokers(cards)


def get_answer_2():
    data = read_file('data/07.txt')
    hands = get_hands_from_data(data)
    if debug1:
        print(f'hands: {hands}')

    hands.sort(key=lambda val: get_rank_with_jokers(val['cards']))
    if debug1:
        print(f'hands: {hands}')

    winnings = 0
    for i in range(len(hands)):
        rank = hands[i]['rank']
        amt = (i + 1) * rank
        cards = hands[i]['cards']
        print(f'Hand {i + 1}: {cards}, rank: {rank}, hand type: {get_hand_type_score(cards)} winnings amt: {amt}')
        winnings += amt

    return winnings


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 07, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 07, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 07, 1 is '245794640'
    # The Answer to Advent of Code 2023, 07, 2 is '247899149'


if __name__ == "__main__":
    main()
