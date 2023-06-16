# Zadanie 3.
# Stwórz macierz 3x3 (używając reshape) z wartościami od 2 do 10

import numpy as np
s = np.arange(2,11)
print(s)
r = s.reshape(3,3)
print(r)