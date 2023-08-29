# Python print 2 decimal places
float = 2.154327
format_float = "{:.2f}".format(float)
print(format_float)

## declaring variables
name = "Datacamp"
type_of_company = "Educational"

## enclose your variable within the {} to display it's value in the output
print(f"{name} is an {type_of_company} company.")

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])