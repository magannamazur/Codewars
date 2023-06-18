# Task
#
# Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next
# [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, the result would be [20,37,21].

def delete_nth(order,max_e):
    list = []
    for e in order:
        count = order.count(e)
        if count > max_e:
            counti = list.count(e)
            if counti < max_e:
                list.append(e)
        elif count <= max_e:
            list.append(e)
    return list


def delete_nthsz(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

def delete_nthbest(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ]

# i = index  0,1,2,3..
# o = element



import unittest

class testex10(unittest.TestCase):
    def test_ex10(self):
        self.assertEqual(delete_nth([20,37,20,21], 1), [20,37,21])
        self.assertEqual(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])