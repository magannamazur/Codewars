def small_enough(array, limit):
    return all(a <= limit for a in array)

# The all() function returns True if all items in an iterable are true, otherwise it returns False.
#
# If the iterable object is empty, the all() function also returns True.