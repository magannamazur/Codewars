# Task
#
# Given an integral number, determine if it's a square number:
#
#     In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
#
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.
# Examples
#
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

import math
def is_square(n):
    if n < 0:
        return False
    else:
        r = math.sqrt(n)
        if n == 0:
            return True
        elif n % r == 0:
            return True
        else:
            return False


import math
def is_squarefast(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

import unittest

class testex8(unittest.TestCase):
    def test_ex8(self):
        self.assertEqual(is_square(-1), False)
        self.assertEqual(is_square( 0), True)
        self.assertEqual(is_square(25), True)