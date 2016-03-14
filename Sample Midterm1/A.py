row = 1
while row <= 10:
    col = 1
    outstring = ' '
    while col <= 10:
        outstring += format(row * col, '5d')
        col += 1
    print(outstring)
    row += 1
