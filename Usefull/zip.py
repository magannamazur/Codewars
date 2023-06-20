# Syntax
# zip(iterator1, iterator2, iterator3 ...)
# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)

print(result)
print(list(result))