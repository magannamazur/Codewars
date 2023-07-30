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

# [[3 4 5]
#  [0 1 2]
#  [6 7 8]]

# 18. How to reverse the rows of a 2D array?
# Q. Reverse the rows of a 2D array

arr = np.arange(9).reshape(3,3)
b = arr[[2,1,0], :]
c = arr[::-1]

# 19. How to reverse the columns of a 2D array?
# Q. Reverse the columns of a 2D array arr.

arr = np.arange(9).reshape(3,3)
b = arr[:, ::-1]

# 20. How to create a 2D array containing random floats between 5 and 10?
# Q. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10
arr = np.random.randint(5, 11, size=15).reshape(5,3)

# 25. How to import a dataset with numbers and texts keeping the text intact in python numpy?
# Q. Import the iris dataset keeping the text intact.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris[:3])

# 26. How to extract a particular column from 1D array of tuples?
# Q. Extract the text column species from the 1D iris imported in previous question.

species = np.array([row[4] for row in iris])
# print(species[:5])
# print(iris[:,4])

# 27. How to convert a 1d array of tuples to a 2d numpy array?
# Q. Convert the 1D iris to 2D array iris_2d by omitting the species text field.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype='object')
# Method 1: Convert each row to a list and get the first 4 items
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
print(iris_2d[:4])
print(iris[:,:4])

# Alt Method 2: Import only the first 4 columns from source url
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(iris_2d[:4])

# 28. How to compute the mean, median, standard deviation of a numpy array?
# Q. Find the mean, median, standard deviation of iris's sepallength (1st column)

sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mu, med, sd)

# 29. How to normalize an array so the values range exactly between 0 and 1?
# Q. Create a normalized form of iris's sepallength whose values range exactly between 0 and 1 so that
# the minimum has value 0 and maximum has value 1.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin)/(Smax - Smin)

# 32. How to insert values at random positions in an array?
# Q. Insert np.nan values at 20 random positions in iris_2d dataset

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

# Method 1
i, j = np.where(iris_2d)

# i, j contain the row numbers and column numbers of 600 elements of iris_x
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan

# Method 2
np.random.seed(100)
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

# Print first 10 rows
print(iris_2d[:10])

# 33. How to find the position of missing values in numpy array?
# Q. Find the number and position of missing values in iris_2d's sepallength (1st column)

# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float')
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

print("Number of missing values: \n", np.isnan(iris_2d[:, 0]).sum())
print("Position of missing values: \n", np.where(np.isnan(iris_2d[:, 0])))