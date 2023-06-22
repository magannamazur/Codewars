# Break camelCase
#
# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
#
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""



import string
def solution(s):
    alphabet = list(string.ascii_uppercase)
    str =""
    for e in s:
        if e in alphabet:
            str += " "
        str += e
    return str

def solutionfast(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

def solutionmaplambda(s):
    return ''.join(map(lambda x: x if x.islower() else " "+ x, s))

import unittest
class testex15(unittest.TestCase):
    def test_ex15(self):
            self.assertEqual(solution("helloWorld"), "hello World")
            self.assertEqual(solution("camelCase"), "camel Case")
            self.assertEqual(solution("breakCamelCase"), "break Camel Case")