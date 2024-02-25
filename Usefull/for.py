def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1
