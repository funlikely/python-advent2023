"""
    --- Day 5: If You Give A Seed A Fertilizer ---

    What is the lowest location number that corresponds to any of the initial seed numbers?

"""
import time
import re

debug1 = False

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer_1():
    data = read_file('data/05.txt')

    total = 0
    return total


def get_answer_2():
    data = read_file('data/05.txt')

    total = 0

    return total


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 05, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 05, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 05, 1 is
    # The Answer to Advent of Code 2023, 05, 2 is


if __name__ == "__main__":
    main()
