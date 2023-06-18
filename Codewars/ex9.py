#
# Convert number to reversed array of digits
#
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example(Input => Output):
#
# 35231 => [1,3,2,5,3]
# 0 => [0]



def digitize(n):
    n = str(n)
    l = []
    for e in n[::-1]:
        l.append(int(e))
    return l

def digitizefast(n):
    return [int(e) for e in str(n)[::-1]]

import unittest

class testex8(unittest.TestCase):
    def test_ex8(self):
        self.assertEqual(digitize(35231),[1,3,2,5,3])
        self.assertEqual(digitize(23582357),[7,5,3,2,8,5,3,2])
        self.assertEqual(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])