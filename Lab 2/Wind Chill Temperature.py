#Wind Chill Temperature

temp = eval(input("Enter a temperture in Fahrenheit: "))
veloc = eval(input("Enter a velocity in miles/hour: "))
print(35.74 + (0.6215 * temp) - (35.75 * (veloc ** 0.16)) + (0.4275 * temp * (veloc ** 0.16)))
