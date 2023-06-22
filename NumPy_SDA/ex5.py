# Zadanie 5.
# Spośród tablicy wartości: [23, 45, 112, 150, 43, 254, 95, 8] wyfiltruj te,
# które są większe od 100

import numpy as np
l = [23, 45, 112, 150, 43, 254, 95, 8]
f = np.array(l)
print(f)
where = np.where(f>100)
print(where)
done = f[where]
print(done)

# szybkie
fast = f[np.where(f>100)]
print(fast)

# szybsze
q = np.array([3,4,5,100,123,1234])
print(q>100)
print(q[q>100])