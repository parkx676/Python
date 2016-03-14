#Day of the Week

modi_m = (int(input("Enter the month: ")))
d = (int(input("Enter the day: ")))
year = (int(input("Enter the year: ")))


if modi_m == 1:
    m = 13
    y = year - 1
    congruence = (d + 5 + ((26 * (m + 1)) // 10) + ((5 * (y % 100)) // 4) + ((21 * (y // 100)) // 4)) % 7
    if congruence == 0:
        print(modi_m, '/', d, '/', y, 'is a Monday')
    elif congruence == 1:
        print(modi_m, '/', d, '/', y, 'is a Tuesday')
    elif congruence == 2:
        print(modi_m, '/', d, '/', y, 'is a Wednesday')
    elif congruence == 3:
        print(modi_m, '/', d, '/', y, 'is a Thursday')
    elif congruence == 4:
        print(modi_m, '/', d, '/', y, 'is a Friday')
    elif congruence == 5:
        print(modi_m, '/', d, '/', y, 'is a Saturday')
    elif congruence == 6:
        print(modi_m, '/', d, '/', y, 'is a Sunday')
elif modi_m == 2:
    m = 14
    y = year - 1
    congruence = (d + 5 + ((26 * (m + 1)) // 10) + ((5 * (y % 100)) // 4) + ((21 * (y // 100)) // 4)) % 7
    if congruence == 0:
        print(modi_m, '/', d, '/', y, 'is a Monday')
    elif congruence == 1:
        print(modi_m, '/', d, '/', y, 'is a Tuesday')
    elif congruence == 2:
        print(modi_m, '/', d, '/', y, 'is a Wednesday')
    elif congruence == 3:
        print(modi_m, '/', d, '/', y, 'is a Thursday')
    elif congruence == 4:
        print(modi_m, '/', d, '/', y, 'is a Friday')
    elif congruence == 5:
        print(modi_m, '/', d, '/', y, 'is a Saturday')
    elif congruence == 6:
        print(modi_m, '/', d, '/', y, 'is a Sunday')
elif 2 < modi_m < 13:
    m = modi_m
    y = year
    congruence = (d + 5 + ((26 * (m + 1)) // 10) + ((5 * (y % 100)) / 4) + ((21 * (y / 100)) / 4)) % 7
    if congruence == 0:
        print(modi_m, '/', d, '/', y, 'is a Monday')
    elif congruence == 1:
        print(modi_m, '/', d, '/', y, 'is a Tuesday')
    elif congruence == 2:
        print(modi_m, '/', d, '/', y, 'is a Wednesday')
    elif congruence == 3:
        print(modi_m, '/', d, '/', y, 'is a Thursday')
    elif congruence == 4:
        print(modi_m, '/', d, '/', y, 'is a Friday')
    elif congruence == 5:
        print(modi_m, '/', d, '/', y, 'is a Saturday')
    elif congruence == 6:
        print(modi_m, '/', d, '/', y, 'is a Sunday')
else:
    print('Wrong month input!')
