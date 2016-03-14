# Take-Away Game

import random

while True:
    start_choice = str(input('Would you like to go first (y/n)? '))
    pile = 21
    if start_choice == 'y':
        while pile >= 4:
            choice = int(input('%d objects remain, choose 1,2 or 3: ' %pile))
            while choice > 3 or choice < 1:
                print('oops, you must choose 1,2 or 3...')
                choice = int(input('%d objects remain, choose 1,2 or 3: ' %pile))
            pile = pile - choice
            if pile == 4:
                opp_choice = random.randint(1,3)
                print("%d objects remian, I'll take" %pile, opp_choice)
                pile = 0
                print('You Win!')
            elif pile == 3:
                opp_choice = 3
                print("%d objects remian, I'll take" %pile, opp_choice)
                pile = 0
                print('I win. Thanks for playing.')
            elif pile == 2:
                opp_choice = 2
                print("%d objects remian, I'll take" %pile, opp_choice)
                pile = 0
                print('I win. Thanks for playing.')
            elif pile == 1:
                opp_choice = 1
                print("%d objects remian, I'll take" %pile, opp_choice)
                pile = 0
                print('I win. Thanks for playing.')
            else:
                opp_choice = random.randint(1,3)
                print("%d objects remian, I'll take" %pile, opp_choice)
                pile = pile - opp_choice
            
    elif start_choice == 'n':
        while pile >= 4:
            opp_choice = random.randint(1,3)
            print("%d objects remian, I'll take" %pile, opp_choice)
            pile = pile - opp_choice
            if pile == 4:
                choice = int(input('%d objects remain, choose 1,2 or 3: ' %pile))    
                while choice > 3 or choice < 1:
                    print('oops, you must choose 1,2 or 3...')
                    choice = int(input('%d objects remain, choose 1,2 or 3: ' %pile))
                pile = pile - choice
                opp_choice = pile
                print("%d objects remian, I'll take" %pile, opp_choice)
                pile = 0
                print('I win. Thanks for playing.')
            elif pile == 3:
                print('You win!')
            elif pile == 2:
                print('You win!')
            elif pile == 1:
                print('You win!')
            else:
                choice = int(input('%d objects remain, choose 1,2 or 3: ' %pile))    
                while choice > 3 or choice < 1:
                    print('oops, you must choose 1,2 or 3...')
                    choice = int(input('%d objects remain, choose 1,2 or 3: ' %pile))
                pile = pile - choice

    else:
        print('Wrong Input!!')
