import numpy as np

# 8. How to stack two arrays vertically?
# Q. Stack arrays a and b vertically

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

c = np.vstack((a,b))
c = np.concatenate([a, b], axis=0)
c = np.r_[a, b]

# 9. How to stack two arrays horizontally?
# Q. Stack the arrays a and b horizontally.


a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

c = np.hstack((a,b))
c = np.concatenate([a, b], axis=1)
c = np.c_[a, b]

# 10. How to generate custom sequences in numpy without hardcoding?
# Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
# Desired Output:
#> array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

a = np.array([1,2,3])

c = np.r_[np.repeat(a, 3), np.tile(a, 3)]

# 11. How to get the common items between two python numpy arrays?
# Q. Get the common items between a and b

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.intersect1d(a,b)

# 12. How to remove from one array those items that exist in another?
# Q. From array a remove all items present in array b

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

c = np.setdiff1d(a,b)

# 13. How to get the positions where elements of two arrays match?
# Q. Get the positions where elements of a and b match

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.where(a ==b)

# 14. How to extract all numbers between a given range from a numpy array?
# Q. Get all items between 5 and 10 from a.

a = np.array([2, 6, 1, 9, 10, 3, 27])

# Method 1
index = np.where((a >= 5) & (a <= 10))
c= a[index]

# Method 2:
index = np.where(np.logical_and(a>=5, a<=10))
c = a[index]

# Method 3: (thanks loganzk!)
c = a[(a >= 5) & (a <= 10)]

# 15. How to make a python function that handles scalars to work on numpy arrays?
# Q. Convert the function maxx that works on two scalars, to work on two arrays.

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

# Returns an object that acts like pyfunc, but takes arrays as input.
pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
#> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])
pair_max(a, b)

# 16. How to swap two columns in a 2d numpy array?
# Q. Swap columns 1 and 2 in the array arr.

arr = np.arange(9).reshape(3,3)
b = arr[:, [1,0,2]]

#> array([[1, 0, 2],
#>        [4, 3, 5],
#>        [7, 6, 8]])

# 17. How to swap two rows in a 2d numpy array?
# Q. Swap rows 1 and 2 in the array arr:

arr = np.arange(9).reshape(3,3)
b = arr[[1,0,2], :]

# 18. How to reverse the rows of a 2D array?
# Q. Reverse the rows of a 2D array

arr = np.arange(9).reshape(3,3)
b = arr[[2,1,0], :]
c = arr[::-1]
print(b)
