# Selection Sort

import random

n = int(input('Enter the number of elements you want: '))
lst = list(range(n))
random.shuffle(lst)

print(lst)

m = 0
x = m + 1

while m != len(lst) - 1:
    while x < len(lst) and lst[m] < lst[x]:
        x += 1
    if x < len(lst):
        lst[m], lst[x] = lst[x], lst[m]
        x += 1
    else:
        m += 1
        x = m + 1
print(lst)


