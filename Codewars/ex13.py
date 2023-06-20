# Triple Trouble
#
# Create a function that will return a string that combines all of the letters of the three inputed strings in groups.
# Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter.
#
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
#
# Note: You can expect all of the inputs to be the same length.



def triple_trouble(one, two, three):
    new = ""
    for i in range(len(one)):
        new += one[i] +two[i] + three[i]
    return new


def triple_troublezip(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))

def triple_troublez(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))

import unittest

class testex13(unittest.TestCase):
    def test_ex13(self):
            self.assertEqual(triple_trouble("aaa","bbb","ccc"), "abcabcabc")
            self.assertEqual(triple_trouble("aaaaaa", "bbbbbb", "cccccc"), "abcabcabcabcabcabc")
            self.assertEqual(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
            self.assertEqual(triple_trouble("Bm", "aa", "tn"), "Batman")
            self.assertEqual(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")