## Warm-Up
import random

filename = input("Enter a filename: ")
file = open(filename, 'w')
i = 1
while i < 1001:
    j = str(i)
    file.write(j +','+str(random.randint(-1000, 1000)) + '\n')
    i += 1
file.close()
    
