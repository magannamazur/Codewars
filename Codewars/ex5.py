# Description:
#
# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from
# Jaden Smith, but they are not capitalized in the same way he originally typed them.
#
# Example:
#
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    return " ".join(e.capitalize() for e in string.split(" "))

import unittest

class testex5(unittest.TestCase):
    def test_ex5(self):
        quote = "How can mirrors be real if our eyes aren't real"
        self.assertEqual(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
