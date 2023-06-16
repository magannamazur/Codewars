import numpy as np

wektor = np.array([1,2,3])
print(wektor)
print(type(wektor))

lista1 = [4,5,6]
wektor = np.array(lista1)
print(wektor)

wektor_kolumnowy = np.array([[1], [2], [3]])
print(wektor_kolumnowy)

macierz = np.array([[1,2,3], [4,5,6]])
print(macierz)
# [[1 2 3]
#  [4 5 6]]

wektor_arange = np.arange(10)
print(wektor_arange)
# [0 1 2 3 4 5 6 7 8 9]

wektor_arange = np.arange(5,10)
print(wektor_arange)
# [5 6 7 8 9]

wektor_arange = np.arange(5,11,2)
print(wektor_arange)
# [5 7 9]

wektor_linspace = np.linspace(1,10,3)
print(wektor_linspace)
# [ 1.   5.5 10. ]
# tensor 1 wymiarowy, 1D

# tworzenie wektorów:
# np.array() - wiemy jaki wektor dokladnie
# np.arange() - wiemy od, do, i co ile
# np.linspace() - wiemy ile elementów

macierz = np.array([
    np.linspace(1,100,5),
    np.linspace(1,300,5)
])
print(macierz)
# [[  1.    25.75  50.5   75.25 100.  ]
#  [  1.    75.75 150.5  225.25 300.  ]]
# tensor 2 wymiarowy, 2D

print(macierz.shape)
# (2, 5)
# liczba wierszy, kolumn

print(macierz.size)
# 10
# iloczyn kolumn i wierszy

print(macierz.ndim)
# 2
# wymiar

skalar = [1]
# pojedyncza wartosc
# inaczej tensor 0 wymiarowy, 0D


# Dostep do macierzy - jednego elementu
macierz = np.array([
    np.linspace(1,100,5),
    np.linspace(1,300,5),
    np.linspace(1,200,5)
])
print(macierz)
# [[  1.    25.75  50.5   75.25 100.  ]
#  [  1.    75.75 150.5  225.25 300.  ]
#  [  1.    50.75 100.5  150.25 200.  ]]

print(macierz[1][1]) # numeracja od 0, typowa dla pythona [wiersz][kolumna]
# 75.75

print(macierz[1, 1]) # numeracja od 0, typowa dla pandasa
# 75.75


# dostep do wiersza all
print(macierz[0])
# [  1.    25.75  50.5   75.25 100.  ]
print(macierz[0,:])

# dostep do kolumny all
print(macierz[:,0])

# dostep do wybranych wierszy i kolumn
print(macierz[:,2:])

# dostep do x
# [o o x x x]
# [o o x x x]
# [o o x x x]

# generowanie losowych liczb
s = np.random.random(10) # zwraca 10 licz z przedzialu 0-1
print(s)

# losowa liczba z rozkladu normalnego
n = np.random.normal()
print(n)

# losowa liczba z rozkladu jednostajnego
u = np.random.uniform()
print(u)

# opcja dla liczb całkowitych, z powtórzeniami
r = np.random.randint(0, 100, size=10)
print(r)
# [82 14 44 54 62 40 82 52 59 75]

wektor = np.array([20, 17, 67, 456, 100, 6, 12.5])

# wskazanie miejsca szukanych wektorow
wektor_wieksze_od_99 = np.where(wektor > 99)
print(wektor_wieksze_od_99)
# (array([3, 4], dtype=int64),)

# szukane liczby
sz = wektor[wektor_wieksze_od_99]
print(sz)
# [456. 100.]

# dzialania na macierzach

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [10, 10, 10],
    [20, 20, 20],
    [30, 30, 30]
])

# dodawanie macierzy

add = np.add(matrix1, matrix2)
print(add)
# [[11 12 13]
#  [24 25 26]
#  [37 38 39]]

add1 = matrix1 + matrix2

# odejmnowanie macierzy

sub = np.subtract(matrix2,matrix1)
print(sub)
# [[ 9  8  7]
#  [16 15 14]
#  [23 22 21]]

sub1 = matrix2 + matrix1

#mnozenie macierzy

mno = matrix1 * matrix2

mno10 = matrix1 * 10

mnowektor = matrix1 * np.array([10,20,30])

print(mno)
print(mno10)
print(mnowektor)

# transpozycja maciezy

tra = matrix1.T
print(tra)

# macierz odwrotna***
C = np.array([[1,4],[2,5]])
od = np.linalg.inv(C)
print(od)

# zmiana ksztaltu macierzy
r = matrix1.reshape(1,9)
print(r)
# [[1 2 3 4 5 6 7 8 9]]

# wyxnaczanie glownej przekatnej
d = matrix1.diagonal()
print(d)
# [1 5 9]

# spłaszczanie macierzy
f = matrix1.flatten()
print(f)
# [1 2 3 4 5 6 7 8 9]

print(type(f))
print(type(r))
print(np.max(matrix1))
print(np.min(matrix1))
print(np.mean(matrix1))
print(np.var(matrix1)) # wariacja
print(np.std(matrix1)) # standardowe odchylenie

# jednostkowa macierz
iden = np.identity(3)
print(iden)