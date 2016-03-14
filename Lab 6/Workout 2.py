# Newton's Root Finding Method

def rootN(x, n):
    i = int(1)
    while abs((i ** n) - x) >= 1e-1:
        i = (1 / n) * (((n - 1) * i) + (x / (i ** (n - 1))))
    print('the root is: ', i)


done = False
while not done:
    x, n = input('enter value and root: ').split(' ')
    x = float(x)
    n = int(n)
    rootN(x, n)
    con = input('continue? (y/n): ')
    if con == 'y':
        done = False
    elif con == 'n':
        done = True
        
    
       
        
