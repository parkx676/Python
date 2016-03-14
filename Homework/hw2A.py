# A. Revolving Credit
# Juhwan Park (3917664)

balance = float(input('Enter current account balance: '))

if balance < 0:
    print('Invalid account balance')
else:
    if balance > 1000:
        interest = ((balance % 1000) * .01) + (1000 * .015)
        amount_due = balance + interest
        minimum_payment = (amount_due * 0.1)
    else:
        interest = balance * 0.015
        amount_due = balance + interest
        if amount_due < 10:
            minimum_payment = amount_due
        else:
            if (amount_due * 0.1) < 10:
                minimum_payment = 10
            else:
                minimum_payment = amount_due * 0.1
        
    print('Interest:', round(interest, 2))
    print('Amount Due:', round(amount_due, 2))
    print('Minimum Payment:', round(minimum_payment, 2))
