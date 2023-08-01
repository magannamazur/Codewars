# The index() method returns the index of the specified element in the list.

animals = ['cat', 'dog', 'rabbit', 'horse']

# get the index of 'dog'
index = animals.index('dog')


print(index)

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'