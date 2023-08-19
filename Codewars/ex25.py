# Write Number in Expanded Form
#
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
    n = str(num)
    l = len(n)
    r = ''
    for e in n:
        if e == '0':
            l-=1
            continue
        else:
            r+=str(e)+str(0)*(l-1)+' + '
            l-=1
    return r[:-3]

def expanded_formshort(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

import unittest
class testex25(unittest.TestCase):
    def test_ex25(self):
            self.assertEqual(expanded_form(12), '10 + 2')
            self.assertEqual(expanded_form(42), '40 + 2')
            self.assertEqual(expanded_form(70304), '70000 + 300 + 4')