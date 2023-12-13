"""
    --- Day 9: Mirage Maintenance ---

    Analyze your OASIS report and extrapolate the next value for each history. What is the sum of these extrapolated values?

"""
import math
import time

debug1 = False

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer_1():
    data = read_file('data/09.txt')
    oasis = [[int(s) for s in line.split(' ')] for line in data]
    total = 0
    for line in oasis:
        inferer = [line]
        current_line = line
        while any([x for x in current_line if x != 0]):
            next_line = [current_line[i+1]-current_line[i] for i in range(len(current_line)-1)]
            inferer.append(next_line)
            current_line = next_line
        print(f'inferer: {inferer}')
        total += sum([x[-1] for x in inferer])
    return total


def get_answer_2():
    data = read_file('data/09_test.txt')
    oasis = [[int(s) for s in line.split(' ')] for line in data]
    total = 0
    for line in oasis:
        inferer = [line]
        current_line = line
        while any([x for x in current_line if x != 0]):
            next_line = [current_line[i+1]-current_line[i] for i in range(len(current_line)-1)]
            inferer.append(next_line)
            current_line = next_line
        print(f'inferer: {inferer}')
        total += sum([x[-1] for x in inferer])
    return total


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 09, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 09, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 09, 1 is '1861775706'
    # The Answer to Advent of Code 2023, 09, 2 is


if __name__ == "__main__":
    main()
