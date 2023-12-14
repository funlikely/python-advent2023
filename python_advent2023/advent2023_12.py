"""
    --- Day 12: Hot Springs ---

    For each row, count all of the different arrangements of operational and broken springs that meet the given
    criteria. What is the sum of those counts?"""
import math
import time

debug1 = True

debug2 = True

data_file = 'data/12_test.txt'


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_slots(data):
    springs = [[slot for slot in x.split(' ')[0].split('.') if len(slot) > 0] for x in data]
    return springs


def get_damaged_groups(data):
    damaged = [[int(g) for g in x.split(' ')[1].split(',')] for x in data]
    return damaged


def get_combinations(slots, damaged):
    if len(damaged) == 0:
        return 0
    if len(damaged) == 1:
        g = damaged[0]
        if len(slots) == 1:
            if g > len(slots):
                return 0  # damaged group too big for available slot
    return 0


def get_answer_1():
    data = read_file(data_file)
    slots_collection = get_slots(data)
    damaged_collection = get_damaged_groups(data)
    if debug1:
        print(f'slots: {slots_collection}, damaged groups: {damaged_collection}')

    combos = [get_combinations(slots_collection[i], damaged_collection[i]) for i in range(len(slots_collection))]

    return sum(combos)


def get_answer_2():
    data = read_file(data_file)

    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 12, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 12, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 12, 1 is
    # The Answer to Advent of Code 2023, 12, 2 is


if __name__ == "__main__":
    main()
