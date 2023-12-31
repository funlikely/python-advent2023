from unittest import TestCase
from advent2023_13 import *

from python_advent2023.advent2023_13 import *


class Test(TestCase):

    def test_image_is_reflecting_i_lines_above_mirror_1(self):
        image = ['.#.###.###..###.#', '..#...##########.', '..######.#..#.###', '..##.#.#......#..',
                 '..#.##....##....#', '.##..#.##.##.##.#', '#.....####..####.', '#.....####..####.',
                 '.##..#.##.##.##.#']
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 1))
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 6))
        self.assertTrue(image_is_reflecting_i_lines_above_mirror(image, 7))
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 8))

    def test_image_is_reflecting_i_lines_above_mirror_2(self):
        image = ['.##..#.##', '.##.####.', '####.....', '.##...##.', '.##.#.###', '#####..##', '.##.#.##.',
                 '....#.###', '####.####', '#..###..#', '.#..#####', '#..#.#...', '.....##..', '#####.###', '#####.###']

        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 1))
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 13))
        self.assertTrue(image_is_reflecting_i_lines_above_mirror(image, 14))

    def test_image_is_reflecting_i_lines_above_mirror_raises_values_exception(self):
        image = ['.##..#.##', '.##.####.', '####.....', '.##...##.', '.##.#.###', '#####..##', '.##.#.##.',
                 '....#.###', '####.####', '#..###..#', '.#..#####', '#..#.#...', '.....##..', '#####.###', '#####.###']

        with self.assertRaises(ValueError):
            image_is_reflecting_i_lines_above_mirror(image, 0)
        with self.assertRaises(ValueError):
            image_is_reflecting_i_lines_above_mirror(image, 15)

    def test_image_is_reflecting_i_lines_above_mirror_3(self):
        image = ['...##...#...##.##', '...##...#...##.##', '..#..#..#..##..#.', '..#..#...##.#####', '..#..#..###...###', '##.##.##..##...##', '#..##..##.#....##', '#.....###.#.##..#', '...............##', '########.#......#']

        self.assertTrue(image_is_reflecting_i_lines_above_mirror(image, 1))
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 2))
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 3))

    def test_image_is_reflecting_i_lines_above_mirror_4(self):
        image = ['...##...#...##.##', '...##...#...##.##', '..#..#..#..##..#.',
                 '..#..#...##.#####', '..#..#..###...###', '##.##.##..##...##', '#..##..##.#....##',
                 '#.....###.#.##..#', '...............##', '########.#......#']

        self.assertTrue(image_is_reflecting_i_lines_above_mirror(image, 1))
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 2))
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 3))

    def test_transpose_image(self):
        image = ['abcdef', '123456', 'xxxxxx']
        self.assertEquals(transpose_image(image), ['a1x', 'b2x', 'c3x', 'd4x', 'e5x', 'f6x'])

