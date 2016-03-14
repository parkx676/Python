## Binomial Coefficient

def choose(n, k):
    if k == n or k == 0:
        return 1
    else:
        return choose(n-1, k-1) + choose(n-1, k)
