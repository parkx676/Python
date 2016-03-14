# Spare Change
# Juhwan Park (3917664)

# Input Values
dollars = eval(input("Enter dollars: "))
cents = eval(input("Enter cents: "))

# define values for each elements
quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01

# Total Input Values
total = dollars + (cents / 100)

# Result
print(int(total / quarters), "quarters")
print(int((total % quarters) / dimes), "dimes")
print(int(((total % quarters) % dimes) / nickels), "nickels")
print(round((((total % quarters) % dimes) % nickels) / pennies), "pennies")
