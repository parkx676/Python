def choose(n,k):
    if (n == n and k == 0) or (n == n and k == n):
        return 1
    else:
        return choose(n - 1, k - 1) + choose(n - 1, k)
