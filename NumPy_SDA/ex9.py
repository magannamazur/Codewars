# Zadanie 9.
# Stwórz funkcję, która przyjmuje dwa wektory (oba o tym samym wymiarze) w
# postaci numpy tablicy, a zwróci odległość euklidesową między nimi

import numpy as np
def euklides_diff(arr1,arr2) -> float:
    return np.sqrt(sum((arr1 - arr2) ** 2))

u_1 = np.array([1, 3, 5, 2, 0])
u_2 = np.array([6, 3, 1, -1, 2])

print(euklides_diff(u_1, u_2))