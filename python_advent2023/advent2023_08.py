"""
    --- Day 8: Haunted Wasteland ---

    Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

"""
import time

debug1 = True

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer_1():
    data = read_file('data/07.txt')
    return 0


def get_answer_2():
    data = read_file('data/07.txt')
    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 08, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 08, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 08, 1 is
    # The Answer to Advent of Code 2023, 08, 2 is


if __name__ == "__main__":
    main()
