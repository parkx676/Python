# Decimal to Binary Conversion
# Juhwan Park (3917664) Lab sec 5


num = int(input('Enter an integer value: '))
binary_backward = ''

while num < 0:
    print('Input must be greater or equal to zero!')
    num = int(input('Enter an integer value: '))
if num == 0:
    print('Base-2 equivalent: 0')
else:
    while num > 0:
        binary = str(num % 2)
        num = num // 2
        binary_backward = binary + binary_backward
    print('Base-2 equivalent: %s' %binary_backward)
