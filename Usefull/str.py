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

## format example
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
a = '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(a)

# %d operator is used as a placeholder to specify integer values, decimals, or numbers
# %s specifically is used to perform concatenation of strings together
# %f formatter is specifically used for formatting float values (numbers with decimals).

def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def say_hello(name, city, state):
    return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)

def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])

def reverse_letter(string):
    return ''.join(x for x in string if x.isalpha())[::-1]


def spin_words(sentence):
    return ' '.join(e[::-1] if len(e) >= 5 else e for e in sentence.split(' '))
