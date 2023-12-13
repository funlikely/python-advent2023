"""
    --- Day 5: If You Give A Seed A Fertilizer ---

    What is the lowest location number that corresponds to any of the initial seed numbers?

"""
import time
import re
from typing import Dict

debug1 = True

debug2 = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_seeds(line):
    return [int(s) for s in line.split(' ')[1:]]


def get_maps(map_data):
    maps = [[]]
    for i in range(len(map_data)):
        if ':' in map_data[i]:
            continue
        if ' ' in map_data[i]:
            map_line = [int(s) for s in map_data[i].split(' ')]
            maps[-1].append(map_line)
        if map_data[i] == '':
            maps.append([])
    return maps


def run_value_through_map(val, mapum):
    for row in mapum:
        if row[1] <= val < row[1] + row[2]:
            return val - row[1] + row[0]
    return val


def get_locations_from_seed(seeds, maps):
    locations = {}
    for seed in seeds:
        destination = seed
        for mapum in maps:
            destination = run_value_through_map(destination, mapum)
        locations[seed] = destination
    return locations


def get_answer_1():
    data = read_file('data/05.txt')

    seeds = get_seeds(data[0])
    if debug1:
        print(f'seed values: {seeds}')

    maps = get_maps(data[2:])
    if debug1:
        for map_item in maps:
            print(f'map: {map_item}')

    locations = get_locations_from_seed(seeds, maps)

    min_location = min(locations.values())  # min(locations, key=locations.get)
    if debug1:
        print(f'locations: {locations}')
    return min_location


def get_answer_2():
    data = read_file('data/05.txt')

    total = 0

    return total


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 05, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 05, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 05, 1 is '462648396'
    # The Answer to Advent of Code 2023, 05, 2 is


if __name__ == "__main__":
    main()
