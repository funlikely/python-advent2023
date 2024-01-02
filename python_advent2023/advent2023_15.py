"""
    --- Day 15: Lens Library ---

    Run the HASH algorithm on each step in the initialization sequence. What is the sum of the results? (The
    initialization sequence is one long line; be careful when copy-pasting it.)"""

import math
import time

debug1 = True

debug2 = True

data_file = 'data/15_test.txt'
data = []


def read_file(file_path):
    file = open(file_path)

    lines = [line.strip() for line in file]
    return lines


def run_hash_function2(step):
    acc = 0
    for c in step:
        acc += ord(c)
        acc *= 17
        acc %= 256
    if debug1 and False:
        print(f'hash({step} = {acc}')
    return acc


def run_hash_function(step):
    # using a fold to find the number of decrypted characters that are in the range of A-Z, a-z, and spaces
    def f(acc, x):
        return (acc + ord(x)) * 17 % 256

    accumulator = 0
    _ = [accumulator := f(accumulator, c) for c in step]

    if debug1 and False:
        print(f'hash({step}) = {accumulator}')
    return accumulator


def get_answer_1():
    data = read_file(data_file)
    steps = data[0].strip().split(',')
    return sum([run_hash_function(step) for step in steps])


def get_code(step):
    if '-' in step:
        return {'label': step[:-1], 'box': run_hash_function(step[:-1]), 'action': 'remove'}
    else:
        return {'label': step.split('=')[0], 'box': run_hash_function(step.split('=')[0]), 'action': 'add',
                'focal': step.split('=')[1]}


boxes = [[]] * 256


def add_lens(box, label, focal):
    for lens in box:
        if lens['label'] == label:
            lens['focal'] = focal
            return
    box.append({'label': label, 'focal': focal})


def remove_lens(box, label):
    return [lens for lens in box if lens['label'] != label]


def get_focusing_power_of_lens(i, lens):
    return i * lens['focal']


def get_focusing_power_of_box(i):
    return (i + 1) * sum([get_focusing_power_of_lens(j + 1, boxes[i][j]) for j in range(len(boxes[i]))])


def get_answer_2():
    data = read_file(data_file)
    steps = data[0].strip().split(',')
    codes = [get_code(step) for step in steps]
    for step in steps:
        print(f'step: {step}, code: {get_code(step)}')

    global boxes

    for code in codes:
        if code['action'] == 'add':
            add_lens(code['box'], code['label'], code['focal'])
        else:
            remove_lens(code['box'], code['label'])
    return sum([get_focusing_power_of_box(i) for i in range(len(boxes))])


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
