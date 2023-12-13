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


def get_answer_1():
    data = read_file(data_file)
    new_data = []
    for j in range(len(data)):
        new_data.append(list(data[j]))
        if all([x == '.' for x in data[j]]):
            new_data.append(list(data[j]))
    for i in range(len(new_data[0])):
        if all([new_data[b][i] == '.' for b in range(len(new_data))]):
            for j in range(len(new_data)):
                new_data[j] = new_data[j][:i] + ['.'] + new_data[j][i:]
    print_stars(new_data)

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
