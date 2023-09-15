# heapq.heapreplace(heap, item)
# Pop and return the smallest item from the heap, and also push the new item.
# The heap size doesn’t change. If the heap is empty, IndexError is raised.

import heapq

def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)

# works the same as:
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)