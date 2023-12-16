from unittest import TestCase
from advent2023_12 import *


class Test(TestCase):
    def test_get_combinations(self):
        self.fail()

    def test_fits_one_spring(self):
        actual = fits_one_spring('..###$$', 2, 3)
        self.assertEquals(actual, False)

