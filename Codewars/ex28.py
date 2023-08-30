#Shortest Word

# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    return min(len(x) for x in s.split())

def find_shortt(s):
    return len(min(s.split(' '), key=len))

# The min() function in python works using ASCII, how letters are represent in binary. So instead of giving you the
# shortest word it return the one that would come first if it the words where organized alphabetically.
# That is why we need to set the key to len.

import unittest
class testex28(unittest.TestCase):
    def test_ex28(self):
            self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
            self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)
            self.assertEqual(find_short("lets talk about javascript the best language"), 3)
            self.assertEqual(find_short("i want to travel the world writing code one day"), 1)