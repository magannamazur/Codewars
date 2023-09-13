# Syntax of enumerate():
#
# enumerate(iterable, start=0)

languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

print(enumerate_prime)

# convert enumerate object to list
print(list(enumerate_prime))

def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

# % is the old style Python string formatting operator. On the left side is a string template and on the right side
# is either a single value or a tuple that supplies the values to fill in the template.
#
# In this case, the enumerate function gives us a list of tuples [(1, line1), (2, line2), ...]
#
# Then the list comprehension invokes the string formatter on each tuple, so we get ["1: line1", "2: line2"...]
