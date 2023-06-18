numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)

print(result)

numbersSquare = set(result)
print(numbersSquare)

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))