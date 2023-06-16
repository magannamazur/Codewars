# Zadanie 8.
# Stwórz dowolną tablicę wartości, a następnie je znormalizuj - tj. od każdego
# elementu tablicy odejmij średnią i podziel przez odchylenie standardowe

import numpy as np

arr = np.random.randint(1, 100, 30).reshape(6, 5)
print(arr)

# średnia
meanvalue= np.mean(arr)

# wariacja
varvalue = np.var(arr)

# odchylenie standardowe - pierwiastek z wariacji
stdvalue = np.std(arr)

arr_nom = (arr - meanvalue) / stdvalue
print(arr_nom)
