## Roman Numerals
## Juhwan Park (3917664)

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000


table = [['M',1000], ['D',500], ['C',100], ['L',50], ['X',10], ['V',5], ['I',1]]


def int2rom(roman):
    result = 0
    lst = []
    for i in roman:
        for letter, value in table:
            if i == letter:
                lst.append(value)
        
    for j in range(len(lst)):
        if j != len(lst)-1 and lst[j] < lst[j+1]:
            result -= lst[j]
        else:
            result += lst[j]
    print('Decimal value: %d' %result)
    

done = False   
while not done:
    roman = str(input('Enter a Roman Numeral: '))
    if len(roman) > 3:
        x = 0
        test = False
        while not test and x != len(roman)-3:
            if roman[x] == roman[x+1] == roman[x+2] == roman[x+3] == 'I' or roman[x] == roman[x+1] == roman[x+2] == roman[x+3] == 'X' or roman[x] == roman[x+1] == roman[x+2] == roman[x+3] == 'C' or roman[x] == roman[x+1] == roman[x+2] == roman[x+3] == 'M':
                print('I,X,C, and M cannot be repeated more than 3 times in succession!')
                test = True
            else:
                x += 1
        if not test:
            int2rom(roman)
    else:
        if roman == '':
            done = True
        else:
            int2rom(roman)
    


