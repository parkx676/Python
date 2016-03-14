#Metric Conversions

number = (eval(input("Enter value: ")))
units = (str(input("Enter units: ")))

if units == 'pounds' or units == 'ounces' or units == 'miles' or units == 'inches':
    if units == 'pounds':
        print(number * 0.45359, 'kilos')
    elif units == 'ounces':
        print(number * 28.3495, 'grams')
    elif units == 'miles':
        print(number * 1.609, 'kilometers')
    else:
        print(number * 2.54, 'centimeters')
else:
    print(units, '?')
