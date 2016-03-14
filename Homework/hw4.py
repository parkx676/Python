## Summary Statistics
## Juhwan Park (3917664)

## Constructing  list
scores = []
i = 0
done = False
while not done:
    score = int(input('Enter a score: '))
    if score < 0:
        done = True
    elif score > 100:
        print('Invalid score... re-enter')
    elif 0<= score <= 100:
        scores.append(score)
        i += score

## list sorting
m = 0
x = m + 1
while m != len(scores) - 1:
    while x < len(scores) and scores[m] < scores[x]:
        x += 1
    if x < len(scores):
        scores[m], scores[x] = scores[x], scores[m]
        x += 1
    else:
        m += 1
        x = m + 1

mean = int(i/len(scores))

## standard deviation
j = 0
sumup = 0
while j < len(scores):
    sumup += ((scores[j] - mean) ** 2)
    j += 1
result = (sumup / len(scores))

c = 1
while abs((c ** 2) - result) > 0.05:
    c += 0.01
c = round(c, 2)

print('----------------------')
print('Number of scores: %d' %len(scores))
print('Maximum score: %d' %scores[-1])
print('Minimum score: %d' %scores[0])
print('Average score: %f' %mean)
print('Standard dev.: %f' %c)
