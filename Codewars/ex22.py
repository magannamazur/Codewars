# Your order, please
#
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the
# position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid
# consecutive numbers.
# Examples
#
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(s):
    g = s.split(' ')
    n=""
    for i in range(1,len(s.split(' '))+1):
        for e in s.split(' '):
            if str(i) in e:
                n += " "
                n += e
    return n[1:len(n)]

def orderfast(sentence):
  return " ".join(sorted(sentence.split(), key=min))

def orderlambda(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

import unittest
class testex22(unittest.TestCase):
    def test_ex22(self):
            self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
            self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
            self.assertEqual(order(""), "")