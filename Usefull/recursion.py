def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def factorial(n):
    return 1 if n <= 0 else n * factorial(n-1)

# dla 5:
# n * factorial(n-1) =
# 5 * f(4)
# 5 * 4 * f(3)
# 5 * 4 * 3 * f(2)
# 5 * 4 * 3 * 2 * f(1)
# 5 * 4 * 3 * 2 * 1


