# Zadanie 7.
# Stwórz dowolną tablicę wartości, a następnie oblicz średnią i medianę

import numpy as np

matrix = np.array([
    [1, 15, 4, 13],
    [8, 21, 3, 12],
    [11, 13, 11, 5],
    [32, 13, 0, 2],
])

# średnia
print(np.mean(matrix))

# mediana
print(np.median(matrix))