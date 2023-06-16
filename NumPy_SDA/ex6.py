# Zadanie 6.
# Stwórz poniższą macierz 4x4, a następnie:
# (a) wyświetl element z drugiego wiersza i trzeciej kolumny,
# (b) oblicz jej ślad (sumę elementów na głównej przekątnej),
# (c) znajdź element największy i najmniejszy.

import numpy as np

matrix = np.array([
    [1, 15, 4, 13],
    [8, 21, 3, 12],
    [11, 13, 11, 5],
    [32, 13, 0, 2]
])
#a
print(matrix[1][2])
print(matrix[1,2])

#b
# wyxnaczanie glownej przekatnej
przekatna = matrix.diagonal()
print(przekatna)
suma = przekatna.sum()
print(suma)

fast_suma = matrix.diagonal().sum()
print(fast_suma)

#c
print(np.max(matrix))
print(np.min(matrix))