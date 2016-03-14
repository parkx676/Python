# Celsius/Fahrenheit Crossover

cel = int(100)
fah = int(((9 * cel) / 5) + 32)
while cel != fah:
    cel -= 1
    fah = int(((9 * cel) / 5) + 32)
print(fah)
    
