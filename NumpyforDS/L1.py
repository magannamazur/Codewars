# 1. Import numpy as np and see the version
import numpy as np
print(np.__version__)

# 2. How to create a 1D array?
# Q. Create a 1D array of numbers from 0 to 9
arr = np.arange(0,10)

arr = np.arange(10)

# 3. How to create a boolean array?
# Q. Create a 3×3 numpy array of all True’s

arr = np.full((3,3),True)

np.ones((3,3), dtype=bool)

# 4. How to extract items that satisfy a given condition from 1D array?
# Q. Extract all odd numbers from arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr = arr[np.where(arr % 2 ==1)]

arr = arr[arr % 2 == 1]

# 5. How to replace items that satisfy a condition with another value in numpy array?
# Q. Replace all odd numbers in arr with -1

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[arr % 2 == 1] = -1

# 6. How to replace items that satisfy a condition without affecting the original array?
# Q. Replace all odd numbers in arr with -1 without changing arr

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
c = arr.copy()
c[c % 2 == 1] = -1

out = np.where(arr % 2 == 1, -1, arr)

# 7. How to reshape an array?
# Q. Convert a 1D array to a 2D array with 2 rows

arr = np.arange(10)

arr = arr.reshape(2,5)

arr = arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols

# 21. How to print only 3 decimal places in python numpy array?
# Q. Print or show only 3 decimal places of the numpy array

rand_arr = np.random.random((5,3))
# rand_arr = np.random.random([5,3])
b = np.around(rand_arr, 3)
# np.set_printoptions(precision=3)

# 22. How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
# Q. Pretty print

np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
# np.set_printoptions(suppress=True, precision=6)


# 23. How to limit the number of items printed in output of numpy array?
# Q. Limit the number of items printed in python numpy array a to a maximum of 6 elements.

a = np.arange(15)
np.set_printoptions(threshold = 6)
print(a)

# 24. How to print the full numpy array without truncating
# Q. Print the full numpy array a without truncating.
import sys
np.set_printoptions(threshold=sys.maxsize)
print(a)