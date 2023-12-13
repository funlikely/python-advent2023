"""
    --- Day 4: Scratchcards ---

    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

    In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83,
    86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers!
    That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three
    matches after the first).

        Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
        Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
        Card 4 has one winning number (84), so it is worth 1 point.
        Card 5 has no winning numbers, so it is worth no points.
        Card 6 has no winning numbers, so it is worth no points.

    So, in this example, the Elf's pile of scratchcards is worth 13 points.

    Take a seat in the large pile of colorful cards. How many points are they worth in total?

"""
import time
import re

debug1 = False

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_winner_numbers(line):
    winners = [int(s) for s in line[line.index(':')+1 : line.index('|')].strip(' ').split(' ') if s != '']
    return winners


def get_guessed_numbers(line):
    return [int(s) for s in line[line.index('|')+1 :].strip(' ').split(' ') if s != '']

def get_answer_1():
    data = read_file('data/04.txt')

    total = 0

    for line in data:
        winners = get_winner_numbers(line)
        guessers = get_guessed_numbers(line)
        corrects = len(set(winners).intersection(set(guessers)))
        points = 2 ** (corrects - 1) if corrects > 0 else 0
        print(f'winners: {winners}, guessers: {guessers}, corrects: {corrects}, points = {points}')
        total += points
    return total


def get_answer_2():
    data = read_file('data/04.txt')
    answer = 0
    return answer


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 04, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 04, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 04, 1 is
    # The Answer to Advent of Code 2023, 04, 2 is


if __name__ == "__main__":
    main()
