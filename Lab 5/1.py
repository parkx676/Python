words = 'did'

words_list = []

for x in range(1, len(words) - 1):
    while str(words[0]) == str(words[x]):
        words_list.append(words)
