## Reverse Phone Spelling Program
## Juhwan Park (3917664)
dictionary = {'a': '2', 'b': '2', 'c': '2',\
                 'd': '3', 'e': '3', 'f': '3',\
                 'g': '4', 'h': '4', 'i': '4',\
                 'j': '5', 'k': '5', 'l': '5',\
                 'm': '6', 'n': '6', 'o': '6',\
                 'p': '7', 'q': '7', 'r': '7', 's': '7',\
                 't':'8', 'u': '8', 'w': '9', 'v': '8',\
                 'w': '9', 'x': '9', 'y': '9', 'z': '9'}


done = False
while not done:
    number = input("Enter a telephone number: ").lower()
    for i in number:
        if i in " .,)(#$%^&*-_+<>'"'"'"{}[]=?/\!@;:":
            number = number.replace(i,"")
    if number == '':
        done = True
    else:
        if len(number) != 7 and len(number) != 10:
            print("Invalid Number!")
        else:
            trans = ''
            if len(number) == 7:
                for i in number:
                    if i not in dictionary.keys():
                        trans += i
                        if len(trans) == 3:
                            trans += '-'
                    else:
                        trans += dictionary[i]
                        if len(trans) == 3:
                            trans += '-'
            elif len(number) == 10:
                for i in number:
                    if i not in dictionary.keys():
                        trans += i
                        if len(trans) == 3:
                            trans += '-'
                        elif len(trans) == 7:
                            trans += '-'
                    else:
                        trans += dictionary[i]
                        if len(trans) == 3:
                            trans += '-'
                        elif len(trans) == 7:
                            trans += '-'
            print("Numeric telephone number is: %s" %trans)
