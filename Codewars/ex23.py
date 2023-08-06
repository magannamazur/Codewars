# Count characters in your string
# Description:
#
# The main idea is to count all the occurring characters in a string. If you have a string like aba,
# then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    d={}
    for i in s:
        if i not in d:
            d[i]= s.count(i)
    return d


def countdict(string):
    return {i: string.count(i) for i in string}

import unittest
class testex23(unittest.TestCase):
    def test_ex23(self):
            self.assertEqual(count('aba'), {'a': 2, 'b': 1})
            self.assertEqual(count(''), {})
            self.assertEqual(count('aa'), {'a' : 2})