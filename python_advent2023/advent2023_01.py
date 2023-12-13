"""
    --- Day 1: Trebuchet?! ---

    The newly-improved calibration document consists of lines of text; each line originally contained a specific
    calibration value that the Elves now need to recover. On each line, the calibration value can be found by
    combining the first digit and the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together
    produces 142.

    Consider your entire calibration document. What is the sum of all of the calibration values?

"""
import time

debug = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer_1():
    data = read_file('data/01.txt')
    total = 0
    for row in data:
        row = ''.join([a for a in row if a.isdigit()])
        total += int(row[0]) * 10
        total += int(row[-1])

    return total


def replace_substring(string: str, a: str, b: str) -> str:
    if len(a) > len(string):
        return string
    for i in range(len(string) - len(a) + 1):
        if ''.join(string[i:(i + len(a))]) == a:
            return string[:i] + b + string[(i + len(a)):]
    return string


def process_row_for_numbers(r):
    replacements = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                    'eight': '8', 'nine': '9'}
    for i in range(len(r)):
        for k in replacements:
            if r[i:].startswith(k):
                r = r[:i] + replacements[k] + r[(i + len(k)):]
    return r


def get_answer_2():
    data = read_file('data/01.txt')
    total = 0
    for row in data:
        row = process_row_for_numbers(row)
        row = ''.join([a for a in row if a.isdigit()])
        num_to_add = int(row[0]) * 10 + int(row[-1])
        print(f'Number to add: {num_to_add}')
        total += num_to_add

    return total


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 01, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 01, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 01, 1 is '54630'
    # The Answer to Advent of Code 2023, 01, 2 is

if __name__ == "__main__":
    main()
