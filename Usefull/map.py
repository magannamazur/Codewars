def calculateSquare(n):
     return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)

print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# ***Syntax
# map(function, iterables)
