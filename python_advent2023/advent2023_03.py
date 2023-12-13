"""
    --- Day 3: Gear Ratios ---

    Here is an example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right)
    and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

    Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine
    schematic?

"""
import time
import re

debug = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_number(row, j):
    return re.findall(r'\b\d+\b', row[j:])[0]


def determine_if_part_number(data, i, j, number):
    pass


def get_answer_1():
    data = read_file('data/03.txt')

    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                number = get_number(data[i], j)
                is_part_number = determine_if_part_number(data, i, j, number)
                if is_part_number:
                    total += number
    return total


def get_answer_2():
    data = read_file('data/03.txt')
    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 03, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 03, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 03, 1 is
    # The Answer to Advent of Code 2023, 03, 2 is


if __name__ == "__main__":
    main()
