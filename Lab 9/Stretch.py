file = open('hallfame.txt', 'r')
dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

line = file.readline()
while line !="":
    for i in ",.!?= ":
        s = line.replace(i, "").lower()
    for j in s:
        for k in dic.keys():
            if j == k:
                dic[k] += 1
    line = file.readline()
##print(max(dic, key=dic.get))
print(dic)
file.close()
