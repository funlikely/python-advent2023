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


def get_seeds_round_2(row):
    some_seed_data = [int(s) for s in row.split(' ')[1:]]
    seeds = [[some_seed_data[i * 2], some_seed_data[i * 2 + 1]] for i in range(int(len(some_seed_data) / 2))]
    return seeds


def run_through_map(destinations, mapum):
    """
    Possibilities
        destinations = [a, b]
        map_item_interval = [c, d]

        if a < c, d < b
            we get three intervals (map(a, c-1), map(c,d), map(d+1, b))
        if c <= a, d < b
            we get two intervals (map(a, d), map(d+1, b))
        if a < c, b <= d
            we get two intervals (map(a, c-1), map(c, b))
        if c <= a, b <=d
            we get one interval (map(a,b))
        if d < c or a > d
            we get one interval ((a,b))

        Oh we'll want to process these maps so they don't have holes in them.

        Data structure brainstorm.


        soil-to-fertilizer map:
        0 15 37  [[15, 51], [0, 36]]
        37 52 2  [[52, 53], [37, 38]]
        39 0 15  [[0, 14], [39, 43]]

        [[[0, 14], [39, 43]], [[15, 51], [0, 36]], [[52, 53], [37, 38]], [[54, 1000], [54, 1000]]]


    :param destinations:
    :param mapum:
    :return:
    """
    results = []
    for interval in destinations:
        for map_item in mapum:
            source_range_min = map_item[1]
            source_range_max = map_item[1] + map_item[2] - 1
            if interval[0] >= source_range_min and interval[1] <= source_range_max:
                results.append(
                    [interval[0] - source_range_min + map_item[0], interval[1] - source_range_min + map_item[0]])
            elif interval[0] <= source_range_min and source_range_min <= interval[1] <= source_range_max:
                print('')
    return results


def process_seeds_and_maps_round_2(seeds, maps):
    destinations = seeds
    for mapum in maps:
        destinations = run_through_map(destinations, mapum)
    return destinations


def get_answer_2():
    data = read_file('data/05.txt')

    seeds = get_seeds_round_2(data[0])
    if debug2:
        print(f'seed values: {seeds}')

    maps = get_maps(data[2:])
    if debug2:
        for map_item in maps:
            print(f'map: {map_item}')

    locations = process_seeds_and_maps_round_2(seeds, maps)

    min_location = min(locations)

    return min_location


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
