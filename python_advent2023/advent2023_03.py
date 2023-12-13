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
    allowed_chars = '0123456789.'
    v_range_min = 0 if i == 0 else i - 1
    v_range_max = len(data) if i == len(data) - 1 else i + 2
    h_range_min = 0 if j == 0 else j - 1
    h_range_max = len(data[i]) if j + len(number) == len(data[i]) else j + len(number) + 1
    for x in range(h_range_min, h_range_max):
        for y in range(v_range_min, v_range_max):
            if data[y][x] not in allowed_chars:
                return True
    return False


def get_answer_1():
    data = read_file('data/03.txt')

    skip_digits = 0

    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit() and (j == 0 or not data[i][j-1].isdigit()):
                number = get_number(data[i], j)
                is_part_number = determine_if_part_number(data, i, j, number)
                if is_part_number:
                    print(f'Found part number: {number}')
                    total += int(number)
                else:
                    print(f'Found non part number: {number}')
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

    # The Answer to Advent of Code 2023, 03, 1 is '549908'
    # The Answer to Advent of Code 2023, 03, 2 is


if __name__ == "__main__":
    main()
