# The int() function converts a number or a string to its equivalent integer

# int() Syntax:
#
# int(value, base [optional])
#
#     value - any numeric-string, bytes-like object or a number
#     base [optional] - the number system that the value is currently in
#     by default = decimal system

# converting a string (that is in binary format) to integer
print("For 0b101, int is:", int("0b101", 2))

# converting a string (that is in octal format) to integer
print("For 0o16, int is:", int("0o16", 8))

# converting a string (that is in hexadecimal format) to integer
print("For 0xA, int is:", int("0xA", 16))