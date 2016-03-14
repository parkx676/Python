morse ={'A':'._','B':'_...','C':'_._.'}

phrase = input('Enter a phrase: ').upper()

for i in phrase:
    print(morse[i])
