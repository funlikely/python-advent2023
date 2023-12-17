"""
    --- Day 12: Hot Springs ---

    For each row, count all of the different arrangements of operational and broken springs that meet the given
    criteria. What is the sum of those counts?"""
import math
import time

debug1 = True

debug2 = True

data_file = 'data/12.txt'


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
            if g == len(slots):
                return 1  # just right
            if g < len(slots):
                if all([x == '?' for x in slots]):
                    return len(slots) - g + 1  # the whole slot is wildcards
                damaged_spots = [i for i, e in enumerate(slots) if e == '#']
                required_damaged_span = max(damaged_spots) - min(damaged_spots) + 1
                if required_damaged_span > g:
                    raise ValueError(f'error in get_combinations({slots}, {damaged}')
                elif required_damaged_span == g:
                    return 1
                elif slots[0] == '#':
                    return 1
                else:  # ??#??#??? g 5  ds 2 5  rds 4
                    return len([(a, b) for a in range(len(slots)) for b in range(len(slots))
                                if min(damaged_spots) <= a < b <= max(damaged_spots) and b - a + 1 == g])
        return sum([get_combinations([slot], damaged) for slot in slots])
    d0 = damaged[0]
    s0 = slots[0]
    if d0 > len(s0):
        return get_combinations(slots, damaged[1:])
    elif d0 == len(s0):
        return get_combinations(slots[1:], damaged[1:]) + get_combinations(slots[1:], damaged)
    else:
        return 0

    return 0


def fits_one_spring(line, a, b):
    if a < 0 or b < 0 or a > len(line) or b > len(line) or b < a:
        raise ValueError(f'Bad values for a={a} or b={b} for line of length {len(line)}')
    if any([line[x] == '#' for x in range(len(line)) if x < a or x > b]):
        return False
    if any([line[x] == '.' for x in range(len(line)) if a <= x <= b]):
        return False
    return True


def get_combinations_simple(line, damaged):
    if len(damaged) == 0:
        return 0
    elif len(damaged) == 1:
        return len(
            [(a, a + damaged[0] - 1) for a in range(len(line) - damaged[0] + 1) if
             fits_one_spring(line, a, a + damaged[0] - 1)])
    else:
        required_size = sum(damaged) + len(damaged) - 1
        if len(line) < required_size:
            return 0
        else:
            if fits_one_spring(line[:(damaged[0])], 0, damaged[0] - 1) and line[damaged[0]] == '#' and line[0] == '#':
                """ this is the case of '##.#', [1,1], which should have 0 solutions """
                # spring_to_go_to = min([i for i, e in enumerate(line) if e != '#' and i > damaged[0]])
                # return get_combinations_simple(line[(spring_to_go_to + 1):], damaged)
                return 0
            if fits_one_spring(line[:(damaged[0])], 0, damaged[0] - 1) and line[damaged[0]] != '#' and line[0] == '#':
                return get_combinations_simple(line[(damaged[0] + 1):], damaged[1:])
            if fits_one_spring(line[:(damaged[0])], 0, damaged[0] - 1) and line[damaged[0]] != '#':
                return get_combinations_simple(line[(damaged[0] + 1):], damaged[1:]) + get_combinations_simple(line[1:],
                                                                                                               damaged)
            else:
                return get_combinations_simple(line[1:], damaged)


def get_combinations_simple_proxy(param, param1):
    result = get_combinations_simple(param, param1)
    if debug2:
        print(f'get_combinations_simple({param}, {param1}) = {result}')
    return result


def get_answer_1():
    data = read_file(data_file)
    slots_collection = get_slots(data)
    damaged_collection = get_damaged_groups(data)
    if debug1:
        print(f'slots: {slots_collection}, damaged groups: {damaged_collection}')

    # combos = [get_combinations(slots_collection[i], damaged_collection[i]) for i in range(len(slots_collection))]
    combos = [get_combinations_simple_proxy(data[i].split(" ")[0], damaged_collection[i]) for i in
              range(len(data))]
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
    #                                             not 7676, too high
    #                                             not 7638, too high
    # The Answer to Advent of Code 2023, 12, 2 is


if __name__ == "__main__":
    main()
