"""
    --- Day 13: Point of Incidence ---

    To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to
    that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above
    example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has
    4 rows above it, a total of 405.

    Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all
    of your notes?"""

import math
import time

debug1 = True

debug2 = True

data_file = 'data/13.txt'


def read_file(file_path):
    file = open(file_path)

    lines = [line.strip() for line in file]
    return lines


def get_images(data):
    images = []
    blank_lines = [0] + [k for k in range(len(data)) if data[k] == ''] + [len(data) + 1]
    images = [data[blank_lines[i]:blank_lines[i + 1]] for i in range(len(blank_lines) - 1)]
    return images


def get_answer_1():
    data = read_file(data_file)

    images = get_images(data)
    if debug1:
        for image in images:
            print(f'image: {image}')

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
    print(f"The Answer to Advent of Code 2023, 13, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 13, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 12, 1 13
    # The Answer to Advent of Code 2023, 12, 2 13


if __name__ == "__main__":
    main()
