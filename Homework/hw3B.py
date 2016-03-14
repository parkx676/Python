# Perfect Numbers
# Juhwan Park (3917664) Lab sec 5

initial = 1
factors = 0
perfect = ''

upper = int(input('Enter the upper bound: '))
initial_upper = upper

if upper < 1:
    print('Invalid upper bound!')
else:
    upper = upper

    while upper != 0:
        while upper != initial:
            if upper % initial == 0:
                factors = factors + initial
                initial += 1
            else:
                initial += 1
        while factors == upper:
                perfect = perfect + str(factors) + ' '
                upper -= 1
                initial = 1
                factors = 0
        upper -= 1
        initial = 1
        factors = 0
    print('Perfect numbers in the interval [0,%d]: %s' %(initial_upper, perfect))
