

def find_uniq(arr):
    l = set(arr)
    u = list(l)
    for e in u:
        x = arr.count(e)
        if x == 1:
            return e

import unittest
class testex16(unittest.TestCase):
    def test_ex16(self):
            self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
            self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
            self.assertEqual(find_uniq([ 3, 10, 3, 3, 3 ]), 10)