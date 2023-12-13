"""
    --- Day 11: Cosmic Expansion ---

    Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""
import math
import time

debug1 = False

debug2 = True

data_file = 'data/11_test.txt'


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def print_stars(stars):
    for line in stars:
        print(f'{"".join(line)}')


def get_horiz_expand_indices(data):
    return [j for j in range(len(data)) if all([x == '.' for x in data[j]])]


def get_vert_expand_indices(data):
    return [i for i in range(len(data[0])) if all([data[j][i] == '.' for j in range(len(data))])]


def expand_stars(data):
    horiz_expand_indices = get_horiz_expand_indices(data)
    vert_expand_indices = get_vert_expand_indices(data)
    print(f'horiz expand indices: {horiz_expand_indices}, vert expand indices: {vert_expand_indices}')

    new_stars= []
    for j in range(data):
        for i in range(data[0]):
            print('hi there')
    return new_stars

def get_answer_1():
    data = read_file(data_file)

    stars = expand_stars(data)

    print_stars(stars)

    return 0


def get_answer_2():
    data = read_file(data_file)
    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 11, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 11, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 11, 1 is
    # The Answer to Advent of Code 2023, 11, 2 is


if __name__ == "__main__":
    main()
