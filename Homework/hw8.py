## Flight Data Filter
## Juhwan Park(3917664)
import os

print("Airport Routing Filter")

validentry = False
in_filename = input("Enter the source file name: ")
i = 0
while not validentry:
    try:
        infile = open(in_filename, 'r')
        validentry = True
    except FileNotFoundError:
        in_filename = input("File not found. Reenter: ")
        i += 1
        if i == 2:
            os._exit(0)

done = False
while not done:
    out_filename = input("Enter the output file name: ")
    if os.path.isfile(out_filename) == True:
        overwrite = input("Would you like to overwrite the existing file?(y/n): ").lower()
        if overwrite == 'y':
            outfile = open(out_filename, 'w')
            done = True

file = infile.readline()
symbol = input("Enter airport symbol: ").upper()
while file !="":
    file_lst = file.strip().split(',')
    if file_lst[2] == symbol or file_lst[4] == symbol:
        outfile.write(file)
    file = infile.readline()
outfile.close()
infile.close()
print("Finished")

