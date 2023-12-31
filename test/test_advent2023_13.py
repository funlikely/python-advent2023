from unittest import TestCase
from advent2023_13 import *

from python_advent2023.advent2023_13 import *


class Test(TestCase):

    def test_get_combinations_simple_examples(self):
        image= ['.#.###.###..###.#', '..#...##########.', '..######.#..#.###', '..##.#.#......#..',
                '..#.##....##....#', '.##..#.##.##.##.#', '#.....####..####.', '#.....####..####.', '.##..#.##.##.##.#']
        self.assertFalse(image_is_reflecting_i_lines_above_mirror(image, 1))
