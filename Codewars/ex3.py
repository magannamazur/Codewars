# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
#
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
#

def reverse_wordsmy(text):
    list = text.split(" ")
    rew_list =""
    for i in list:
        rew_word =""
        length = len(i)
        for e in range(length-1, -1, -1):
            rew_word +=i[e]
        rew_list +=rew_word + " "
        rew_word =""
    l= len(rew_list)
    rew_list =rew_list[:l-1]
    return rew_list

def reverse_wordsmymidle(text):
    rew_list = []
    for i in text.split(" "):
        rew_word = i[::-1]
        rew_list.append(rew_word)
    return " ".join(rew_list)

def reverse_wordsshortest(text):
  return ' '.join([ word[::-1] for word in text.split(' ')])

a = reverse_wordsmymidle("hi yo")
print(a)

import unittest

class testex3(unittest.TestCase):
    def test_ex3(self):
        self.assertEqual(reverse_wordsmy('The quick brown fox jumps over the lazy dog.'),
                         'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEqual(reverse_wordsmy('apple'), 'elppa')
        self.assertEqual(reverse_wordsmy('a b c d'), 'a b c d')
        self.assertEqual(reverse_wordsmy('double  spaced  words'), 'elbuod  decaps  sdrow')