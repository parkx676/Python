## Reversing Number

def reverseNum(n):
    if len(n) < 2:
        return n
    else:
        return n[-1] + reverseNum(n[:-1])
