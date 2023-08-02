def countdict(string):
    return {i: string.count(i) for i in string}

print(countdict('aba'))


d = countdict('aba')
print(d)
#We can also use .keys() and .values() methods to access Counter class object
for i in d.keys():
      print(i, ":", d[i])