# Definition and Usage
#
# The translate() method returns a string where some specified characters are replaced with the
# character described in a dictionary, or in a mapping table.
#
# Use the maketrans() method to create a mapping table.
#
# If a character is not specified in the dictionary/table, the character will not be replaced.
#
# If you use a dictionary, you must use ascii codes instead of characters.

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))