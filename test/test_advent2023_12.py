from unittest import TestCase
from advent2023_12 import *


class Test(TestCase):

    def test_get_combinations(self):
        """
        todo: implement
        :return:
        """
        self.assertEquals(1, 1)

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
