"""
    --- Day 10: Pipe Maze ---

    Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting
    position to the point farthest from the starting position?"""
import math
import time

debug1 = False

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer_1():
    data = read_file('data/10.txt')
    total = 0
    return total


def get_answer_2():
    data = read_file('data/10.txt')
    total = 0
    return total


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 10, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 10, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 10, 1 is
    # The Answer to Advent of Code 2023, 10, 2 is


if __name__ == "__main__":
    main()
