# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The multiply of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))


# A list like [1, 2, 3, 1, 2, 3, 4] can be thought of as [1, 1, 2, 2, 3, 3, 4].
# 1 xor 1 = 0
# 0 xor 2 = 2
# 2 xor 2 = 0
import operator
from functools import reduce

def find_itgenius(xs):
     return reduce(operator.xor, xs)
print(find_itgenius([1,1,2,2,3,3,4]))
