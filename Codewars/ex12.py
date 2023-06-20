# Description:
#
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.
#
# Note: input will never be an empty string

def fake_bin(x):
    l = []
    new = []
    for i in x:
        l.append(int(i))
    for e in l:
        if e < 5:
            new.append(0)
        else:
            new.append(1)
    return "".join(str(e) for e in new)

def fake_binfast(x):
    return ''.join('0' if c < '5' else '1' for c in x)

import unittest

class testex12(unittest.TestCase):
    def test_ex12(self):
        tests = [
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]

        for exp, inp in tests:
            self.assertEqual(fake_bin(inp), exp)