"""
    --- Day 2: Cube Conundrum ---

    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes,
    and 14 blue cubes. What is the sum of the IDs of those games?

"""
import time
import re

debug = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer_1():
    data = read_file('data/02.txt')
    total = 0
    for line in data:
        numbers = re.findall(r'\b\d+\b', line)
        game_num = int(numbers[0])

        game_fail = False
        split_line = line.split(' ')[2:]
        for j in range(0, len(split_line), 2):
            if split_line[j + 1].startswith('red') and int(split_line[j]) > 12:
                game_fail = True
            if split_line[j + 1].startswith('green') and int(split_line[j]) > 13:
                game_fail = True
            if split_line[j + 1].startswith('blue') and int(split_line[j]) > 14:
                game_fail = True
        if not game_fail:
            total += game_num

    return total


def get_answer_2():
    data = read_file('data/02.txt')
    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 02, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 02, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 02, 1 is
    # The Answer to Advent of Code 2023, 02, 2 is


if __name__ == "__main__":
    main()
