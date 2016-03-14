x = float(input('Enter a number: '))

if x <= 0.0:
    y = 0.0
    print(y)
elif 0.0 < x <= 1.0:
    y = x ** 2
    print(y)
elif 1.0< x <= 10.0:
    y = 1.0
    print(y)
elif 10.0 < x:
    y = 0.0
    print(y)
