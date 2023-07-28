# Build Tower
#
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block
# is represented with "*" character.
#
# For example, a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]

def tower_builder(n_floors):
    lvl = ' '
    s = "*"
    leaves = lvl*(n_floors-1) + s + lvl*(n_floors-1)
    tree = [leaves]
    if n_floors > 1:
        for e in range(1,n_floors):
            leaves = lvl*(n_floors - e-1) + s* (2*e +1) + lvl*(n_floors - e-1)
            tree.append(leaves)
    return tree

def tower_builderfast(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

import unittest
class testex20(unittest.TestCase):
    def test_ex20(self):
            self.assertEqual(tower_builder(1), ['*', ])
            self.assertEqual(tower_builder(2), [' * ', '***'])
            self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])