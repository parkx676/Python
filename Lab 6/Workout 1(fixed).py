lst = [[45, -99], [24, 83], [-48, -68], [-97, 99], \
[-8, -77], [-2, 50], [44, 41], [-48, -58], \
[-1, 53], [14, 86], [31, 94], [12, -91], \
[33, 50], [82, 72], [83, -90], [10, 78], \
[7, -22], [90, -88], [-21, 5], [6, 23]]
import math

def shortestDist(lst):
    i = 0
    j = 0
    shortest = 1000000000000000000
    while i != len(lst)-1:
        while j != len(lst)-1:
            if i == j:
                j += 1
            else:
                initial = math.sqrt((lst[j][0]-lst[i][0])**2 + (lst[j][1]-lst[i][1])**2)
                if j+1 == i:
                    j += 1
                compare = math.sqrt((lst[j+1][0]-lst[i][0])**2 + (lst[j+1][1]-lst[i][1])**2)
                if initial > compare:
                    if shortest > compare:
                        shortest = compare
                        j += 1
                    else:
                        j += 1
                elif initial < compare:
                    if shortest > initial:
                        shortest = first
                        j += 1
                    else:
                        j += 1
        i += 1
        j = 0
    return shortest

                    
