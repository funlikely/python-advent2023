"""
    --- Day 14: Parabolic Reflector Dish ---

    Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?
"""

import math
import time

debug1 = True

debug2 = True

data_file = 'data/14.txt'


def read_file(file_path):
    file = open(file_path)

    lines = [line.strip() for line in file]
    return lines


def find_rock_to_shift(shifted_column, a):
    i = a
    while i < len(shifted_column):
        if shifted_column[i] == 'O':
            return i
        elif shifted_column[i] == '#':
            return None
        i += 1
    return None


def shift_column_north(column):
    shifted_column = [x for x in column]

    for a in range(len(shifted_column)):
        if shifted_column[a] == '.':
            b = find_rock_to_shift(shifted_column, a)
            if b:
                shifted_column[a] = 'O'
                shifted_column[b] = '.'
    shifted_column = ''.join(shifted_column)
    return shifted_column


def load_of_column(column):
    shifted_column = shift_column_north(column)
    load = [(len(shifted_column) - k) for k in range(len(shifted_column)) if shifted_column[k] == 'O']
    return sum(load)


def get_answer_1():
    data = read_file(data_file)
    result = 0

    for i in range(len(data[0])):
        column_i = ''.join([data[j][i] for j in range(len(data))])
        result += load_of_column(column_i)
    return result


def get_answer_2():
    data = read_file(data_file)

    result = 0
    return result


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 14, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 14, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 14, 1 is '113525'
    # The Answer to Advent of Code 2023, 14, 2 is


if __name__ == "__main__":
    main()
