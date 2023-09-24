# The Supermarket Queue
# Description:
#
# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total
# time required for all the customers to check out!
#
#     customers: an array of positive integers representing the queue. Each integer represents a customer, and its
#     value is the amount of time they require to check out.
#     n: a positive integer, the number of checkout tills.
#
# Example
# queue_time([10,2,3,3], 2) should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the queue finish before the 1st person has finished.

def queue_time(customers, n):
    sl = {}
    if len(customers) == 0:
        return 0
    elif len(customers) <=n:
        return max(customers)
    else:
        for i in range(1,n+1):
                sl[i]=customers[i-1]
    for c in customers[n:]:
        a = min(sl, key=sl.get)
        sl[a] =sl[a]+c
    return max(sl.values())

def queue_timefast(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

import unittest
class testex29(unittest.TestCase):
    def test_ex29(self):
            self.assertEqual(queue_time([], 1), 0, "wrong answer for case with an empty queue")
            self.assertEqual(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
            self.assertEqual(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
            self.assertEqual(queue_time([1, 2, 3, 4, 5], 1), 15, "wrong answer for a single till")
            self.assertEqual(queue_time([1, 2, 3, 4, 5], 100), 5,
                               "wrong answer for a case with a large number of tills")
            self.assertEqual(queue_time([2, 2, 3, 3, 4, 4], 2), 9, "wrong answer for a case with two tills")
