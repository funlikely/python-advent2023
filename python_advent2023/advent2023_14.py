"""
    --- Day 14: Parabolic Reflector Dish ---

    Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?
"""

import math
import time

debug1 = True

debug2 = True

data_file = 'data/14.txt'
data = []


def width():
    return len(data[0])


def height():
    return len(data)


def read_file(file_path):
    file = open(file_path)

    lines = [line.strip() for line in file]
    return lines


def find_rock_to_shift(shifted_column, a):
    i = a
    while i < len(shifted_column):
        if shifted_column[i] == 'O':
            return i
        elif shifted_column[i] == '#':
            return None
        i += 1
    return None


def shift_column_north(column):
    shifted_column = [x for x in column]

    for a in range(len(shifted_column)):
        if shifted_column[a] == '.':
            b = find_rock_to_shift(shifted_column, a)
            if b is not None:
                shifted_column[a] = 'O'
                shifted_column[b] = '.'
    shifted_column = ''.join(shifted_column)
    return shifted_column


def load_of_column(column):
    shifted_column = shift_column_north(column)
    load = [(len(shifted_column) - k) for k in range(len(shifted_column)) if shifted_column[k] == 'O']
    return sum(load)


def get_answer_1():
    global data

    data = read_file(data_file)
    result = 0

    for i in range(width()):
        column_i = ''.join([data[j][i] for j in range(height())])
        result += load_of_column(column_i)
    return result


def find_rock_to_shift_north(col_i, row_a):
    row_y = row_a
    while row_y < height():
        if data[row_y][col_i] == 'O':
            return row_y
        elif data[row_y][col_i] == '#':
            return None
        row_y += 1
    return None


def shift_rocks_north():
    for i in range(width()):
        for a in range(height()):
            if data[a][i] == '.':
                b = find_rock_to_shift_north(i, a)
                if b is not None:
                    data[a][i] = 'O'
                    data[b][i] = '.'


def find_rock_to_shift_east(row_j, col_b):
    col_x = col_b
    while col_x > -1:
        if data[row_j][col_x] == 'O':
            return col_x
        elif data[row_j][col_x] == '#':
            return None
        col_x -= 1
    return None


def shift_rocks_east():
    for j in range(height()):
        for b in range(width() - 1, -1, -1):
            if data[j][b] == '.':
                a = find_rock_to_shift_east(j, b)
                if a is not None:
                    data[j][b] = 'O'
                    data[j][a] = '.'


def find_rock_to_shift_west(row_j, col_b):
    col_x = col_b
    while col_x < width():
        if data[row_j][col_x] == 'O':
            return col_x
        elif data[row_j][col_x] == '#':
            return None
        col_x += 1
    return None


def shift_rocks_west():
    for j in range(height()):
        for b in range(width()):
            if data[j][b] == '.':
                a = find_rock_to_shift_west(j, b)
                if a is not None:
                    data[j][b] = 'O'
                    data[j][a] = '.'


def find_rock_to_shift_south(col_i, row_a):
    row_y = row_a
    while row_y > -1:
        if data[row_y][col_i] == 'O':
            return row_y
        elif data[row_y][col_i] == '#':
            return None
        row_y -= 1
    return None


def shift_rocks_south():
    for i in range(width()):
        for a in range(height() - 1, -1, -1):
            if data[a][i] == '.':
                b = find_rock_to_shift_south(i, a)
                if b is not None:
                    data[a][i] = 'O'
                    data[b][i] = '.'


def print_data():
    for j in range(height()):
        print(''.join(data[j]))
    print()


def get_state():
    state = ''
    for j in range(height()):
        row = ''.join([char for char in data[j]])
        state += row
    return state


def get_load():
    return 0


def get_answer_2():
    global data
    data = read_file(data_file)
    for j in range(height()):
        data[j] = [char for char in data[j]]

    result = 0

    print(f'Original state:')
    print_data()
    previous_state = get_state()
    i = 1
    states = {}
    while True:
        shift_rocks_north()
        shift_rocks_west()
        shift_rocks_south()
        shift_rocks_east()
        if debug1 and False:
            print(f'Shift N/W/W/E:')
            print_data()
        current_state = get_state()
        if current_state in states.values():
            for key, value in states.items():
                if current_state == value:
                    print(f'found an equilibrium at iteration {i}, it is a repeat of iteration {key}')
            break
        states[i] = current_state
        if i % 10 == 0:
            print(f'iteration: {i}')
        i += 1
    return get_load()


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_1_time = time.time()
    answer_2 = get_answer_2()
    answer_2_time = time.time()
    print(f"time taken for problem 1: {answer_1_time - start}")
    print(f"time taken for problem 2: {answer_2_time - answer_1_time}")
    print(f"The Answer to Advent of Code 2023, 14, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 14, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 14, 1 is '113525'
    # The Answer to Advent of Code 2023, 14, 2 is


if __name__ == "__main__":
    main()
