"""
    --- Day 11: Cosmic Expansion ---

    Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""
import math
import time

debug1 = False

debug2 = True

data_file = 'data/11_test.txt'


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def print_stars(stars):
    for line in stars:
        print(f'{"".join(line)}')


def get_horiz_expand_indices(data):
    return [j for j in range(len(data)) if all([x == '.' for x in data[j]])]


def get_vert_expand_indices(data):
    return [i for i in range(len(data[0])) if all([data[j][i] == '.' for j in range(len(data))])]


def expand_stars(data):
    horiz_expand_indices = get_horiz_expand_indices(data)
    vert_expand_indices = get_vert_expand_indices(data)
    print(f'horiz expand indices: {horiz_expand_indices}, vert expand indices: {vert_expand_indices}')

    new_stars= []
    for j in range(len(data)):
        new_line = []
        if j in horiz_expand_indices:
            for i in range(len(data[0]) + len(vert_expand_indices)):
                new_line.append('.')
            new_stars.append(new_line)
            new_line = []
            for i in range(len(data[0]) + len(vert_expand_indices)):
                new_line.append('.')
            new_stars.append(new_line)
        else:
            for i in range(len(data[0])):
                if i in vert_expand_indices:
                    new_line.append('.')
                    new_line.append('.')
                else:
                    new_line.append(data[j][i])
            new_stars.append(new_line)
    return new_stars


def get_star_coords(stars):
    return [(y, x) for y in range(len(stars)) for x in range(len(stars[0])) if stars[y][x] == '#']


def get_dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def get_answer_1():
    data = read_file(data_file)

    stars = expand_stars(data)

    print_stars(stars)

    star_coords = get_star_coords(stars)

    distances = []
    for coord1 in star_coords:
        for coord2 in [s for s in star_coords if is_ordered_stars(coord1, s)]:
            distances.append(get_dist(coord1, coord2))
            print(f'Distance between {coord1} and {coord2} = {get_dist(coord1, coord2)}')

    return int(sum(distances) / 2)


def get_dist2(coord1, coord2, horiz_expand_indices, vert_expand_indices):
    dist = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

    scale = 100

    y1 = min(coord1[1], coord2[1])
    y2 = max(coord1[1], coord2[1])
    dist += len([h for h in horiz_expand_indices if y1 < h < y2]) * scale

    x1 = min(coord1[0], coord2[0])
    x2 = max(coord1[0], coord2[0])
    dist += len([v for v in vert_expand_indices if x1 < v < x2]) * scale

    return dist


def is_ordered_stars(a, b):
    return (a[0] - b[0]) * 10 ** 10 + (a[1] - b[1])


def get_answer_2():
    data = read_file(data_file)

    stars = data
    horiz_expand_indices = get_horiz_expand_indices(stars)
    vert_expand_indices = get_vert_expand_indices(stars)

    # print_stars(stars)

    star_coords = get_star_coords(stars)

    distances = []
    for coord1 in star_coords:
        for coord2 in [s for s in star_coords if is_ordered_stars(coord1, s)]:
            distances.append(get_dist2(coord1, coord2, horiz_expand_indices, vert_expand_indices))
            if debug2:
                print(f'Distance between {coord1} and {coord2} = {get_dist2(coord1, coord2, horiz_expand_indices, vert_expand_indices)}')

    return sum(distances)


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 11, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 11, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 11, 1 is '9521550'
    # The Answer to Advent of Code 2023, 11, 2 is


if __name__ == "__main__":
    main()
