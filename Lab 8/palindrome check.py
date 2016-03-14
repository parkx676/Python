## Palindrome Check
def reverse(istr):
    return istr[::-1]


def ispalindrome(istr):
    for i in ",.!? ":
        s = istr.replace(i, "")
    s = s.lower()
    s = s.replace("'", "")
    if s == reverse(s):
        return True
    else:
        return False
    

done = False
while not done:
    istr = str(input("Enter a string: "))
    if ispalindrome(istr) == True:
        print('%s is a palindrome' %istr)
    elif ispalindrome(istr) == False:
        print('%s is not a palindrome' %istr)
    con = str(input('Constinue? (y/n): ')).lower()
    if con == 'n':
        done = True
    elif con == 'y':
        done = False
