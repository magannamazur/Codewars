# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.
#
# For example (Input --> Output):
#
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)
#

def persistence(n):
    iloraz = n
    count = 0
    while iloraz >= 10:
        ilorazz = 1
        count += 1
        for e in str(iloraz):
            ilorazz *= int(e)
        iloraz = ilorazz
    return count

import unittest

class testex11(unittest.TestCase):
    def test_ex11(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(999), 4)