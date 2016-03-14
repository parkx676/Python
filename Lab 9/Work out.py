## Work out

openfile = open("2.5_day.csv", 'r')
file = openfile.readline()
categ0 = "0"
while file != "":
    file = file.strip().split(',')
    categ0 += ' '
    categ0 += file[0]
    file = openfile.readline()
print(categ0 + '\n')
openfile.close()

openfile = open("2.5_day.csv", 'r')
file = openfile.readline()
categ1 = "1"
while file != "":
    file = file.strip().split(',')
    categ1 += ' '
    categ1 += file[1]
    file = openfile.readline()
print(categ1+ '\n')
openfile.close()

openfile = open("2.5_day.csv", 'r')
file = openfile.readline()
categ2 = "2"
while file != "":
    file = file.strip().split(',')
    categ2 += ' '
    categ2 += file[2]
    file = openfile.readline()
print(categ2+ '\n')
openfile.close()
