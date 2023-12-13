"""
    --- Day 8: Haunted Wasteland ---

    Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

"""
import math
import time
from typing import List

debug1 = True

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_graph(graph_data):
    graph = {line[0:3]: ({'L': line[7:10], 'R': line[12:15]}) for line in graph_data}
    return graph


def get_answer_1():
    data = read_file('data/08.txt')

    instructions = data[0]
    graph = get_graph(data[2:])
    if debug1:
        print(f'instructions: {instructions}')
        print(f'graph: {graph}')

    steps = 0
    current = 'AAA'
    while current != 'ZZZ':
        direction = instructions[steps % len(instructions)]
        if debug1:
            print(f'at {current}, moving {direction} on {graph[current]}')
        current = graph[current][direction]
        steps += 1
    return steps


def get_lcm(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return get_lcm([math.lcm(nums[0], nums[1])] + nums[2:])


def get_answer_2():
    data = read_file('data/08.txt')

    instructions = data[0]
    graph = get_graph(data[2:])
    if debug1:
        print(f'instructions: {instructions}')
        print(f'graph: {graph}')

    a_starts = [k for k in graph.keys() if k[-1] == 'A']
    steps_list = [0] * len(a_starts)
    for i in range(len(a_starts)):
        steps = 0
        current = a_starts[i]
        while current[-1] != 'Z':
            direction = instructions[steps % len(instructions)]
            if debug1:
                print(f'at {current}, moving {direction} on {graph[current]}')
            current = graph[current][direction]
            steps += 1
        steps_list[i] = steps

    return get_lcm(steps_list)


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 08, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 08, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 08, 1 is '22411'
    # The Answer to Advent of Code 2023, 08, 2 is '11188774513823'


if __name__ == "__main__":
    main()
