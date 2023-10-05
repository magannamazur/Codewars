# strptime()
#
# The strptime() method creates a datetime object from the given string.
#
# Note: You cannot create datetime object from every string. The string needs to be in a certain format.

from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

# Here,
#
#     %d - Represents the day of the month. Example: 01, 02, ..., 31
#     %B - Month's name in full. Example: January, February etc.
#     %Y - Year in four digits. Example: 2018, 2019 etc.
