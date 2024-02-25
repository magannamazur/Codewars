# filter() Syntax
#
# The syntax of filter() is:
#
# filter(function, iterable)
#
#
#     function - a function
#     iterable - an iterable like sets, lists, tuples etc.


# returns True if the argument passed is even

def check_even(number):
    if number % 2 == 0:
          return True

    return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)


# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Output: [2, 4, 6, 8, 10]


numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))