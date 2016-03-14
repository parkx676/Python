# Basal Metabolic Rate

weight = (eval(input("Enter your weight in pounds: ")))
height = (eval(input("Enter your height in inches: ")))
age = (eval(input("Enter your age in years: ")))
sex = (str(input("Enter your sex in the character 'M' for male or 'F' for female: ")))

F_BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
M_BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)

chocobar = 230

if sex == 'M':
    print("Number of chocolate bar:", round(M_BMR / chocobar))
else:
    print("Number of chocolate bar:", round(F_BMR / chocobar))
    
