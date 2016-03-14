## Warm-up 2

filename = input("Enter a filename you want to open: ").lower()
file = open(filename, 'r')
maximum = -2001
for i in file:
    i = i.strip().split(',')
    j = float(i[1])
    if j > maximum:
        maximum = j
print(maximum)
file.close()

file = open(filename, 'r')
minimum = 2001
for k in file:
    k = k.strip().split(',')
    l = float(k[1])
    if l < minimum:
        minimum = l
print(minimum)
file.close()
