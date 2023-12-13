"""
    --- Day 10: Pipe Maze ---

    Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting
    position to the point farthest from the starting position?"""
import math
import time

debug1 = False

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


directions = {'-': [{'y': 0,  'x': -1}, {'y': 0, 'x': 1}],
              '|': [{'y': -1, 'x': 0},  {'y': 1, 'x': 0}],
              'L': [{'y': -1,  'x': 0}, {'y': 0, 'x': 1}],
              'J': [{'y': 0,  'x': -1}, {'y': -1, 'x': 0}],
              'F': [{'y': 1, 'x': 0},   {'y': 0, 'x': 1}],
              '7': [{'y': 1, 'x': 0},   {'y': 0, 'x': -1}],
              'S': [{'y': 1, 'x': 0},   {'y': 0, 'x': 1}]}  # special for now, since it acts as an 'F'
              #'S': [{'y': -1,  'x': 0}, {'y': 0, 'x': 1}]}  # special for now, since it acts as an 'L'


data_file = 'data/10.txt'


def print_picture(data, path):
    picture = []
    for j in range(len(data)):
        line = ''.join([' ']*len(data[0]))
        line = list(line)
        picture.append(line)
    for node in path:
        picture[node[0]][node[1]] = data[node[0]][node[1]]
    for line in picture:
        if any([x for x in line if x != ' ']):
            print(''.join(line))


def get_answer_1():
    data = read_file(data_file)
    if data_file == 'data/10.txt':
        directions['S'] = directions['L']
    elif data_file == 'data/10_test.txt':
        directions['S'] = directions['F']
    elif data_file == 'data/10_test2.txt':
        directions['S'] = directions['F']

    y, x = [(j, i) for j in range(len(data)) for i in range(len(data[0])) if data[j][i] == 'S'][0]

    path = [(y, x)]
    print(f'loc: ({y},{x}), data(loc): {data[y][x]}')

    while len(path) < 10 or data[y][x] != 'S':
        choices = directions[data[y][x]]
        adjacencies = [(y + choice['y'], x + choice['x']) for choice in choices]
        next_nodes = [n for n in adjacencies if n not in path]
        if not next_nodes:
            break
        y, x = next_node = next_nodes[0]
        path.append(next_node)
        if len(path) % 6 == 0 and len(path) < 200:
            print(f'Path length so far: {len(path)}')
            print_picture(data, path)
        # print(f'path: {path}')
    print_picture(data, path)
    print(f'Total length of path: {len(path)}')
    path_node_set = set(path)
    print(f'Nodes in path are unique: {len(path) == len(path_node_set)}')
    return int(len(path) / 2)


def get_answer_2():
    data = read_file(data_file)
    if data_file == 'data/10.txt':
        directions['S'] = directions['L']
    elif data_file == 'data/10_test.txt':
        directions['S'] = directions['F']
    elif data_file == 'data/10_test2.txt':
        directions['S'] = directions['F']

    y, x = [(j, i) for j in range(len(data)) for i in range(len(data[0])) if data[j][i] == 'S'][0]

    path = [(y, x)]
    print(f'loc: ({y},{x}), data(loc): {data[y][x]}')

    while len(path) < 10 or data[y][x] != 'S':
        choices = directions[data[y][x]]
        adjacencies = [(y + choice['y'], x + choice['x']) for choice in choices]
        next_nodes = [n for n in adjacencies if n not in path]
        if not next_nodes:
            break
        y, x = next_node = next_nodes[0]
        path.append(next_node)
        if len(path) % 6 == 0 and len(path) < 200:
            print(f'Path length so far: {len(path)}')
            print_picture(data, path)
        # print(f'path: {path}')
    print_picture(data, path)
    print(f'Total length of path: {len(path)}')
    path_node_set = set(path)
    print(f'Nodes in path are unique: {len(path) == len(path_node_set)}')
    return int(len(path) / 2)


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 10, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 10, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 10, 1 is '6812'
    # The Answer to Advent of Code 2023, 10, 2 is


if __name__ == "__main__":
    main()
