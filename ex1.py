def validate_hello(greetings):
    hi = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
#     hi = "hello ciao salut hallo hola ahoj czesc"
    greetings = greetings.lower()
    sign = ['!', ',', ':', '.', '?', ';']
    for s in sign:
        if s in greetings:
            greetings = greetings.replace(s, '')
    g = greetings.split(" ")
    lens =len(g)
    while lens > 0:
        for something in g:
            if something in hi:
                return True
            else:
                lens -= 1
    return False


ans= validate_hello('hombre! Hola!')
print(ans)