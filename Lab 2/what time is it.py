# What Time is it?

import time

total_minuite = time.time() / 60
total_hour = total_minuite / 60
total_day = total_hour / 24
total_year = total_day // 365
leapmonth_day =  (total_year / 4) - 1
i = (total_day - (total_year * 365 + leapmonth_day))
j = ((i % 1) * 24)
k = ((j % 1) * 60)

def month(i):
    if i <= 31:
        print('January')
    elif 31 < i <= 59:
        print('Feburary')
    elif 59 < i <= 90:
        print('March')
    elif 90 < i <= 120:
        print('April')
    elif 120 < i <= 151:
        print('May')
    elif 151 < i <= 181:
        print('June')
    elif 181 < i <= 212:
        print('July')
    elif 212 < i <= 243:
        print('August')
    elif 243 < i <= 273:
        print('September')
    elif 273 < i <= 304:
        print('October')
    elif 304 < i <= 334:
        print('November')
    else:
        print('December')

       
print(int(j), ':', int(k)), month(i), print(',', int(i), int(1970 + total_year))
