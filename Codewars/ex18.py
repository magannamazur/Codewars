# Find the unique number
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
#
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    l = set(arr)
    u = list(l)
    for e in u:
        x = arr.count(e)
        if x == 1:
            return e

def find_uniqfast(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

def find_uniqintrested(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]

from collections import Counter

def find_uniqcounter(a):
    return Counter(a).most_common()[-1][0]

import unittest
class testex16(unittest.TestCase):
    def test_ex16(self):
            self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
            self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
            self.assertEqual(find_uniq([ 3, 10, 3, 3, 3 ]), 10)