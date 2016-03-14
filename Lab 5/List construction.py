# List Construction


words_list = []

words = input('Enter a words: ')

while words != '':
    if words[0] in words[1:]:
        words_list.append(words)
    words = input('Enter a words: ')      
print(words_list)
