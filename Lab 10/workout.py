keywords = {'def':0,'for':0,'if':0,'in':0,'return':0,'while':0,'False':0}

filename = input('Enter the filename: ')

ofile = open(filename, 'r')
line = ofile.readline()
while line != '':
    line = line.lstrip()
    for i in line:
        if i in "._-;=:":
            line = line.replace(i, ' ')
    line = line.split()
    for i in line:
        for j in keywords:
            if i == j:
                keywords[j] += 1
    line = ofile.readline()

for i in keywords.keys():
    if keywords[i] != 0:
        print(i+'         %d' %keywords[i])
