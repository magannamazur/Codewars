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
print(c)
