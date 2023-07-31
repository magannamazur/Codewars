# Definition and Usage
#
# The sorted() function returns a sorted list of the specified iterable object.

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

b = ("hello world")
x = sorted(b)
print(x)

# sorted() method sorts the given sequence as well as set and dictionary(which is not a sequence) either in ascending
# order or in descending order(does unicode comparison for string char by char) and always returns the a sorted list.
# This method doesn’t effect the original sequence
# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))
print(x)

# sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original
# sequence. Moreover, sort() is a method of list class and can only be used with lists.
# List of Integers
numbers = [1, 3, 4, 2]

# Sorting list of Integers
numbers.sort()

print(numbers)

def order(sentence):
  return " ".join(sorted(sentence.split(), key=min))

# key (Optional) - A function that serves as a key for the sort comparison. Defaults to None