# B. Lexicographic Ordering
# Juhwan Park (3917664)

first = str(input('Enter first string: '))
second = str(input('Enter second string: '))
third = str(input('Enter third string: '))

if first < second < third:
    print(first)
    print(second)
    print(third)
elif first < third < second:
    print(first)
    print(third)
    print(second)
elif second < first < third:
    print(second)
    print(first)
    print(third)
elif second < third < first:
    print(second)
    print(third)
    print(first)
elif third < first < second:
    print(third)
    print(first)
    print(second)
elif third < second < first:
    print(third)
    print(second)
    print(first)
        
        
