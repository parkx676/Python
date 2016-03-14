# multiplication table

def multi(num):
    for j in range(1, 10):
        print(num, '*', j, '=', int(num) * j)
        
while (True):
    num = input('Which number of multiplication table you want? ')
    if 1 < int(num) < 10:
        multi(num)
    
    else:
        print('Wrong Input!')
