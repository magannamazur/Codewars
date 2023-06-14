# Description:
#
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done
# before, or after the addition.
#
# The binary number returned should be a string.
#
# Examples:(Input1, Input2 --> Output (explanation)))
#
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def decimalToBinary(n):
    return bin(n).replace("0b", "")

number = 14
print('The binary equivalent of 15 is', bin(number))

def ninjaMethod(n):
    return (bin(4785)[2:])

import unittest

class testex7(unittest.TestCase):
    def test_ex7(self):
        self.assertEqual(decimalToBinary(2),"10")
        self.assertEqual(decimalToBinary(63),"111111")