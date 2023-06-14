import numpy as np
# Zadanie 1.
# Stwórz numpy array z wartościami od 1 do 9, wyświetl, a następnie odwróć tę
# tablicę (pierwszy element zostaje ostatnim, itd.)

ar = np.arange(1,10)
print(ar)
af = ar[::-1]
print(af)

# or
af = np.flip(ar)
print(af)

# np.fliplr(zadanie) # dla wymiarów >= 2
# np.flipud(zadanie) # dla wymiarów >= 2
