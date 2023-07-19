word = "mississippi"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print(counter)
# {'m': 1, 'i': 4, 's': 4, 'p': 2}

# MOST_COMMON

# If you need to list a group of objects according to their frequency,
# or the number of times they appear, then you can use .most_common().
# This method returns a list of (object, count) sorted by the objects’ current count.
# Objects with equal counts come in the order they first appear.

from collections import Counter
sales = Counter(banana=15, tomato=4, apple=39, orange=30)

# The most common object
print(sales.most_common(1))
# [('apple', 39)]

# The most common key
print(sales.most_common()[0][0])
# apple

# The most common value
print(sales.most_common()[0][1])
# 39

# All objects sorted by count
print(sales.most_common())
# [('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]

# All objects in reverse order
print(sales.most_common()[::-1])
# [('tomato', 4), ('banana', 15), ('orange', 30), ('apple', 39)]
