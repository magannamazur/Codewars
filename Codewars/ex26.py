# Counting Duplicates

# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
# occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once

def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) >1])

import unittest
class testex26(unittest.TestCase):
    def test_ex26(self):
            self.assertEqual(duplicate_count(""), 0)
            self.assertEqual(duplicate_count("abcde"), 0)
            self.assertEqual(duplicate_count("abcdeaa"), 1)
            self.assertEqual(duplicate_count("abcdeaB"), 2)
            self.assertEqual(duplicate_count("Indivisibilities"), 2)