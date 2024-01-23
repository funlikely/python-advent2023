"""
    --- Day 16: The Floor Will Be Lava ---

    The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing
    the current situation. With the beam starting in the top-left heading right, how many tiles end up being
    energized?"""

import math
import time

debug1 = True

debug2 = True

data_file = 'data/16.txt'
data = []

energized = []


def read_file(file_path):
    file = open(file_path)

    lines = [line.strip() for line in file]
    return lines


def get_energized_value(original_value, direction):
    if original_value == '.':
        if direction in ['e', 'w']:
            return 'h'
        return 'v'
    elif original_value == 'h':
        if direction in ['e', 'w']:
            return 'h'
        return '2'
    elif original_value == 'v':
        if direction in ['e', 'w']:
            return '2'
        return 'v'
    elif original_value == '2':
        return '2'
    raise ValueError('Something wrong with energized value ' + str(original_value))


def find_energized_spaces(j, i, direction):
    if not 0 <= j <= len(data) or not 0 <= i <= len(data[0]):
        return 0
    else:
        old_value = energized[j][i]
        new_value = get_energized_value(old_value, direction)
        if new_value != old_value:
            if data[j][i] == '.':
                print(f'everyone loves you')


def get_answer_1():
    global data
    data = read_file(data_file)
    global energized
    energized = get_empty_energized(data)
    j, i = 0, 0

    find_energized_spaces(j, i, 'e')

    return sum([sum([1 for c in row if c != '.']) for row in energized])


def get_empty_energized(data):
    global energized
    energized = []
    for i in range(len(data)):
        energized.append(['.'] * len(data[0]))
    return energized


def get_answer_2():
    global data
    data = read_file(data_file)
    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_1_time = time.time()
    answer_2 = get_answer_2()
    answer_2_time = time.time()
    print(f"time taken for problem 1: {answer_1_time - start}")
    print(f"time taken for problem 2: {answer_2_time - answer_1_time}")
    print(f"The Answer to Advent of Code 2023, 16, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 16, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 16, 1 is
    # The Answer to Advent of Code 2023, 16, 2 is


if __name__ == "__main__":
    main()
