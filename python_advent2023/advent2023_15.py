"""
    --- Day 15: Lens Library ---

    Run the HASH algorithm on each step in the initialization sequence. What is the sum of the results? (The
    initialization sequence is one long line; be careful when copy-pasting it.)"""

import math
import time

debug1 = True

debug2 = True

data_file = 'data/15.txt'
data = []


def read_file(file_path):
    file = open(file_path)

    lines = [line.strip() for line in file]
    return lines


def run_hash_function(step):
    acc = 0
    for c in step:
        acc += ord(c)
        acc *= 17
        acc %= 256
    return acc


def get_answer_1():
    data = read_file(data_file)
    steps = data[0].strip().split(',')
    return sum([run_hash_function(step) for step in steps])


def get_answer_2():
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
    print(f"The Answer to Advent of Code 2023, 15, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 15, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 15, 1 is is '511416'
    # The Answer to Advent of Code 2023, 15, 2 is


if __name__ == "__main__":
    main()
