# Shortest Distance
import math

lst = [[45, -99], [24, 83], [-48, -68], [-97, 99], \
[-8, -77], [-2, 50], [44, 41], [-48, -58], \
[-1, 53], [14, 86], [31, 94], [12, -91], \
[33, 50], [82, 72], [83, -90], [10, 78], \
[7, -22], [90, -88], [-21, 5], [6, 23]]

def shortestDist():
    i = -1
    x = -2
    result = 100000000
    while abs(i) <= len(lst):
        while abs(x) <= len(lst):
            sqr1 = (lst[i][0] - lst[x][0]) ** 2
            sqr2 = (lst[i][1] - lst[x][1]) ** 2
            if math.sqrt(sqr1 + sqr2) < result:
                result = round(math.sqrt(sqr1 + sqr2), 4)
                x -= 1
            else:
                x -= 1
        i -= 1
        x = i - 1
    return result
