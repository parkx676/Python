# Loan Payments

loan = eval(input("Enter a loan amount: "))
annual = eval(input(
    "Enter an annual interest rate: "))
n = eval(input("Enter a loan duration: "))
r = annual / 12
print("Payment = ", (r * loan)/(1 - ((1 + r) ** -n)))
