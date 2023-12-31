"""
    --- Day 13: Point of Incidence ---

    To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to
    that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above
    example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has
    4 rows above it, a total of 405.

    Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all
    of your notes?"""

import math
import time

debug1 = True

debug2 = True

data_file = 'data/13.txt'


def read_file(file_path):
    file = open(file_path)

    lines = [line.strip() for line in file]
    return lines


def get_images(data):
    blank_lines = [-1] + [k for k in range(len(data)) if data[k] == ''] + [len(data) + 1]
    images = [data[(blank_lines[i] + 1):blank_lines[i + 1]] for i in range(len(blank_lines) - 1)]
    return images


def image_is_reflecting_i_lines_above_mirror(image, i):
    if i < 1 or i > len(image) - 1:
        raise ValueError(f"there can't be {i} rows reflected in an image with {len(image)} rows")
    j = 0
    while i - j > 0 and i + j < len(image):
        if image[i - j - 1] != image[i + j]:
            return False
        j += 1
    return True


def transpose_image(image):
    transposed_image = [''.join([image[k][i] for k in range(len(image))]) for i in range(len(image[0]))]
    return transposed_image


def get_image_note_value(image):
    for i in range(1, len(image)):
        if image_is_reflecting_i_lines_above_mirror(image, i):
            return i * 100
    else:
        transposed_image = transpose_image(image)
    for i in range(1, len(transposed_image)):
        if image_is_reflecting_i_lines_above_mirror(transposed_image, i):
            return i
    raise ValueError(f'Didn\'t find reflection in {image}')


def get_answer_1():
    data = read_file(data_file)

    images = get_images(data)
    if debug1:
        for image in images:
            print(f'image: {image}')

    result = 0
    for image in images:
        if len(image) < 3 or len(image[0]) < 3:
            raise ValueError("You have a too narrow image that you didn't expect!!")
        result += get_image_note_value(image)

    return result


def get_answer_2():
    data = read_file(data_file)

    return 0


def main():
    start = time.time()
    answer_1 = get_answer_1()
    answer_2 = get_answer_2()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Advent of Code 2023, 13, 1 is '{answer_1}'")
    print(f"The Answer to Advent of Code 2023, 13, 2 is '{answer_2}'")

    # The Answer to Advent of Code 2023, 12, 1 is '37381'
    # The Answer to Advent of Code 2023, 12, 2 is


if __name__ == "__main__":
    main()
