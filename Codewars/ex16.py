# Isograms
#
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
#
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false



def is_isogram(string):
    double = 0
    for s in string.lower():
        double = string.lower().count(s)
        if double > 1:
            break
    if double > 1:
        return False
    else:
        return True

def is_isogramfast(string):
    return len(string) == len(set(string.lower()))

import unittest
class testex16(unittest.TestCase):
    def test_ex16(self):
            self.assertEqual(is_isogram("Dermatoglyphics"), True )
            self.assertEqual(is_isogram("isogram"), True )
            self.assertEqual(is_isogram("aba"), False, "same chars may not be adjacent")
            self.assertEqual(is_isogram("moOse"), False, "same chars may not be same case")
            self.assertEqual(is_isogram("isIsogram"), False)
            self.assertEqual(is_isogram(""), True, "an empty string is a valid isogram")