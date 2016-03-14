# Rounding floating-point values

floating = (float(input("Enter a floating-point value: ")))

if floating > 0:
    print(int(floating + 0.5))
elif floating < 0:
    print(int(floating - 0.5))
else:
    print("Wrong Input!")
