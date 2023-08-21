import numpy as np
# Zadanie 2.
# Stwórz następujący numpy array: [1, 23, 4, 31, 1, 1, 4, 23, 4, 1],
# a następnie wypisz wszystkie unikalne (nie powtarzające się) elementy

l = [1, 23, 4, 31, 1, 1, 4, 23, 4, 1]
ar = np.array(l)
print(ar)
uniq = np.unique(ar)
print(uniq)