# Largest of Three Values

x = (float(input("Enter 1st floating-point value: ")))
y = (float(input("Enter 2nd floating-point value: ")))
z = (float(input("Enter 3rd floating-point value: ")))

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)
