# 1..................................................

def reverse_wordsshortest(text):
    return ' '.join([ word[::-1] for word in text.split(' ')])

import unittest

class tescik(unittest.TestCase):
    def tescik(self):
        self.assertEqual(reverse_wordsshortest('The quick brown fox jumps over the lazy dog.'),
                         'ehT kciuq nworb xof spmuj revo eht yzal .god')


# 2.........................................................

def solution(text, ending):
    return text.endswith(ending)

import unittest


fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

class testt(unittest.TestCase):
    def testt(self):
        def test_case():
            for text, ending in fixed_tests_True:
                self.assertEqual(solution(text, ending), True)

        def test_case():
            for text, ending in fixed_tests_False:
                self.assertEqual(solution(text, ending), False)