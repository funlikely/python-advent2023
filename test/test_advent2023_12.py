from unittest import TestCase
from advent2023_12 import *

from python_advent2023.advent2023_12 import *


class Test(TestCase):

    def test_get_combinations_simple_examples(self):
        self.assertEquals(get_combinations_simple('.??.', [1]), 2)

    def test_get_combinations_simple_from_problem_itself(self):
        self.assertEquals(get_combinations_simple('???.###', [1, 1, 3]), 1)
        self.assertEquals(get_combinations_simple('.??..??...?##.', [1, 1, 3]), 4)
        self.assertEquals(get_combinations_simple('?#?#?#?#?#?#?#?', [1, 3, 1, 6]), 1)
        self.assertEquals(get_combinations_simple('????.#...#...', [4, 1, 1]), 1)
        self.assertEquals(get_combinations_simple('????.######..#####.', [1, 6, 5]), 4)
        self.assertEquals(get_combinations_simple('?###????????', [3, 2, 1]), 10)

    def test_fits_one_spring_fails_on_dot_locations(self):
        self.assertEquals(fits_one_spring('..###??', 1, 2), False)
        self.assertEquals(fits_one_spring('..###??', 1, 3), False)
        self.assertEquals(fits_one_spring('..###??', 1, 4), False)
        self.assertEquals(fits_one_spring('..###??', 1, 5), False)

    def test_fits_one_spring_true_for_good_spring_location(self):
        self.assertEquals(fits_one_spring('..###??', 2, 3), False)
        self.assertEquals(fits_one_spring('..###??', 2, 4), True)
        self.assertEquals(fits_one_spring('..###??', 2, 5), True)
        self.assertEquals(fits_one_spring('..###??', 2, 6), True)

    def test_fits_one_spring_false_when_missing_spring_locations(self):
        self.assertEquals(fits_one_spring('..###??', 3, 5), False)
        self.assertEquals(fits_one_spring('..###??', 3, 5), False)
        self.assertEquals(fits_one_spring('..###??', 3, 5), False)

    def test_fits_one_spring_raises_error_on_bad_a(self):
        try:
            fits_one_spring('..###??', -1, 2)
        except ValueError as e:
            self.assertEquals(str(e), 'Bad values for a=-1 or b=2 for line of length 7')

    def test_fits_one_spring_raises_error_on_bad_b(self):
        try:
            fits_one_spring('..###??', 1, 9)
        except ValueError as e:
            self.assertEquals(str(e), 'Bad values for a=1 or b=9 for line of length 7')
