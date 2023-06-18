# Syntax of enumerate():
#
# enumerate(iterable, start=0)

languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

print(enumerate_prime)

# convert enumerate object to list
print(list(enumerate_prime))