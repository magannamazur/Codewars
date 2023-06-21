import numpy as np
A = np.array([[2,3,4],[5,6,7]])
B = [[2,3,4],[5,6,7]]
print(A.shape)
print(A)

# Indeksowanie
#[6]
A[1][1]
B[1][1]

# [3 6]
A[:, 1] # all wiersze, 2 kolumna


C = np.array([[2,3,4],[5,6,7],[8,9,10]])

# [[2 3]
#  [5 6]
#  [8 9]]
C[:,:2]

# [[ 6  7]
#  [ 9 10]]
C[1:,1:]


print(C[1:,1:])

# Reshape
R = A.reshape(-1) # skleja do jednej lini
print(R)
# [2 3 4 5 6 7]
print(R.shape)

r = A.reshape(6)
print(r)
print(r.shape)

#mean
m = A.mean(axis=0) # srednia z kolumn
M = A.mean(axis=1)  # srednia z wierszy
print(m, M)
# [3.5 4.5 5.5] [3. 6.]