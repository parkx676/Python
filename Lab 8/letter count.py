## Letter Count

def ltrcount(istr):
    count = 0
    for i in istr:
        if i.isalpha():
            count += 1
    return count
