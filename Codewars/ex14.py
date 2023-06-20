# Multiple of index
#
# Return a new array consisting of elements which are multiple of their own index in input array (length > 1).
# Some cases:
#
# [22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]
#
# [68, -1, 1, -7, 10, 10] => [-1, 10]

def multiple_of_index(arr):
    index = 0
    l = []
    for e in arr:
        if e == 0:
            index += 1
            l.append(e)
        elif index == 0:
            index += 1
        elif e% index == 0:
            index += 1
            l.append(e)
        else:
            index += 1
    return l

import unittest
class testex14(unittest.TestCase):
    def test_ex14(self):
            self.assertEqual(multiple_of_index([22, -6, 32, 82, 9, 25]), [-6, 32, 25])
            self.assertEqual(multiple_of_index([68, -1, 1, -7, 10, 10]), [-1, 10])
            self.assertEqual(multiple_of_index([11, -11]), [-11])
            self.assertEqual(multiple_of_index([-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68]), [-85, 72, 0, 68])
            self.assertEqual(multiple_of_index([28,38,-44,-99,-13,-54,77,-51]), [38, -44, -99])
            self.assertEqual(multiple_of_index([-1,-49,-1,67,8,-60,39,35]), [-49, 8, -60, 35])
            self.assertEqual(multiple_of_index([0, 2, 3, 6, 9]), [0, 2, 6])