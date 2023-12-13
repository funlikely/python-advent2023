"""
    --- Day 9: Mirage Maintenance ---

    Analyze your OASIS report and extrapolate the next value for each history. What is the sum of these extrapolated values?

"""
import math
import time
from typing import List

debug1 = True

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer_1():
    data = read_file('data/09.txt')
    return 0


def get_answer_2():
    data = read_file('data/09.txt')
    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 09, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 09, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 09, 1 is
    # The Answer to Advent of Code 2023, 09, 2 is


if __name__ == "__main__":
    main()
