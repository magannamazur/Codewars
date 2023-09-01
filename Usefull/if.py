def hoopCount(n):
    return "Keep at it until you get it" if n<10 else "Great, now move on to tricks"

print(hoopCount(10))

def get_real_floor(n):
    return n - 2 if n > 13 else n - 1 if n > 0 else n

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

def update_light(current):
    return 'yellow' if current =='green' else  'red' if current =='yellow'  else 'green'

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)