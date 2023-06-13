# Description:
#
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits
# in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
#
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321

def descending_ordermy(num):
    list = [int(x) for x in str(num)]
    list_sorted = sorted(list, reverse=False)
    sum = 0
    inta = 1
    for i in list_sorted:
        sum += i*inta
        inta *= 10
    return sum

# sorted, funkcja wbudowana, zwraca liste
# sort, funkcja dla list, zwraca None

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

import unittest

class testex6(unittest.TestCase):
    def test_ex6(self):
        self.assertEqual(descending_ordermy(0), 0)
        self.assertEqual(descending_ordermy(15), 51)
        self.assertEqual(descending_ordermy(123456789), 987654321)