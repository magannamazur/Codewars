# Description:
#
# Create a function with two arguments that will return an array of the first n multiples of x.
#
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
#
# Return the results as an array or list ( depending on language ).
# Examples
#
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]


def count_bybetter(x, n):
    return [i * x for i in range(1, n + 1)]


def count_bymy(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    lista = []
    for i in range(n):
        lista.append(x * (i + 1))
    return lista

import unittest

class testex2(unittest.TestCase):
    def test_ex2(self):
        self.assertEqual(count_bymy(1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(count_bymy(2, 5), [2, 4, 6, 8, 10])
        self.assertEqual(count_bymy(3, 5), [3, 6, 9, 12, 15])
        self.assertEqual(count_bymy(50, 5), [50, 100, 150, 200, 250])
        self.assertEqual(count_bymy(100, 5), [100, 200, 300, 400, 500])