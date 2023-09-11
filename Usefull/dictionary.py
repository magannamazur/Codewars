def countdict(string):
    return {i: string.count(i) for i in string}

print(countdict('aba'))


d = countdict('aba')
print(d)
#We can also use .keys() and .values() methods to access Counter class object
for i in d.keys():
      print(i, ":", d[i])

dic = {}
print(type(dic))

# klucz : wartość

powitanie= {1:"hej", 2: "siema"}
print(powitanie)

# Użycie klucza do pobrania wartości
print(powitanie[1])

sl = {1:30, 2:45, 3:10}
key_of_min_value = min(sl, key=sl.get)
min_value = min(sl.values())
print(key_of_min_value, min_value)

def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]