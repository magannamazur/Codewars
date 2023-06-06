# Description:
#
# You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met
# yesterday evening?
#
# Write a simple function to check if the string contains the word hallo in different languages.
#
# These are the languages of the possible people you met the night before:
#
#     hello - english
#     ciao - italian
#     salut - french
#     hallo - german
#     hola - spanish
#     ahoj - czech republic
#     czesc - polish
#
# Notes
#
#     you can assume the input is a string.
#     to keep this a beginner exercise you don't need to check if the greeting is a subset of word
#     (Hallowen can pass the test)
#     function should be case insensitive to pass the tests



def validate_hello(greetings):
    hi = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in hi:
        if i in greetings.lower():
            return True
    return False

#fast check
ans= validate_hello('hombre! Hola!')
print(ans)

import unittest

class testex1(unittest.TestCase):
    def test_ex1(self):
            for inp, exp in [('hello',True), ('ciao bella!',True), ('salut',True),
                             ('hallo, salut',True), ('hombre! Hola!',True),
                             ('Hallo, wie geht\'s dir?',True), ('AHOJ!',True),
                             ('czesc',True), ('meh',False), ('Ahoj',True), ]:
                self.assertEqual(validate_hello(inp),exp)
