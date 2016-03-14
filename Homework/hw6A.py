## Digital Roots
## Juhwan Park (3917664)

def digitsum(n):
    if 0 > n:
        return digitsum(-n)
    elif n < 10:
        return n
    else:
        return (n % 10) + digitsum(n // 10)

    
def digitalroot(n):
    if n < 10:
        return digitsum(n)
    else:
        return digitalroot(digitsum(n))
