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