def exp(x, n):
    if n == 0:
        return 0
    else:
        return x + exp(x, n-1)

