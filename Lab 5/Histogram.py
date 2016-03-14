# Histogram

import random

histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = 0

while n <= 10000:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    x = dice1 + dice2
    n += 1
    if x == 2:
        histogram[0] += 1
    elif x== 3:
        histogram[1] += 1
    elif x== 4:
        histogram[2] += 1
    elif x== 5:
        histogram[3] += 1
    elif x== 6:
        histogram[4] += 1
    elif x== 7:
        histogram[5] += 1
    elif x== 8:
        histogram[6] += 1
    elif x== 9:
        histogram[7] += 1
    elif x== 10:
        histogram[8] += 1
    elif x== 11:
        histogram[9] += 1
    elif x== 12:
        histogram[10] += 1
print(histogram)

        
