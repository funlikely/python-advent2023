"""
    --- Day 5: If You Give A Seed A Fertilizer ---

    What is the lowest location number that corresponds to any of the initial seed numbers?

"""
import time
import re
from typing import Dict, List

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
    seeds = [[some_seed_data[i * 2], some_seed_data[i * 2] + some_seed_data[i * 2 + 1] - 1] for i in range(int(len(some_seed_data) / 2))]
    return seeds


def map_interval(interval: List[int], mapum: List[List[int]]) -> List[List[int]]:
    interval_min = interval[0]
    interval_max = interval[1]
    translated_map = [[[item[1], item[1]+item[2]-1], item[0] - item[1]] for item in mapum]
    map_mins = [item[1] for item in mapum]
    map_maxs = [item[1]+item[2]-1 for item in mapum]
    map_shifts = [item[0] - item[1] for item in mapum]
    relevant_map_items = [item for item in translated_map
                          if interval_min <= item[0][0] <= interval_max or interval_min <= item[0][1] <= interval_max]
    out_left_map_items = [item for item in translated_map if item[0][0] < interval_min <= item[0][1]]
    out_right_map_items = [item for item in translated_map if item[0][0] <= interval_max < item[0][1]]
    inside_map_items = [item for item in translated_map
                        if interval_min <= item[0][0] <= interval_max and interval_min <= item[0][1] <= interval_max]
    if len(out_left_map_items) > 1 or len(out_right_map_items) > 1:
        print(f'error, out left map items: {out_left_map_items}, out right map items: {out_right_map_items}')
    new_intervals = []
    if not relevant_map_items:
        new_intervals.append([interval_min, interval_max])
    if out_left_map_items:
        out_left_map_item = out_left_map_items[0]
        new_intervals.append([interval_min + out_left_map_item[1], out_left_map_item[0][1] + out_left_map_item[1]])
    if out_right_map_items:
        out_right_map_item = out_right_map_items[0]
        new_intervals.append([out_right_map_item[0][0] + out_right_map_item[1], interval_max + out_right_map_item[1]])
    for map_item in inside_map_items:
        new_intervals.append([map_item[0][0] + map_item[1], map_item[0][1] + map_item[1]])

    return new_intervals


def process_seeds_and_maps_round_2(intervals, maps):
    if len(maps) == 0:
        return intervals
    mapum = maps[0]

    # process intervals through mapum
    new_intervals = []

    for interval in intervals:
        new_intervals += map_interval(interval, mapum)

    return process_seeds_and_maps_round_2(new_intervals, maps[1:])


def get_answer_2():
    data = read_file('data/05_test.txt')

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
