scores = []
done = False
while not done:
    score = int(input("Enter a score: "))
    if score < 0:
        done = True
    elif score > 100:
        print("Invalid score... re-enter")
    else:
        scores.append(score)
print("---------------------------------")
print("Number of scores: %d" %len(scores))

scores = sorted(scores, reverse=True)
print("Maximum score: %s" %scores[0])
print("Minimum score: %s" %scores[-1])

i = 0
x = 0
while x < len(scores) and len(scores) != 0:
    i += scores[x]
    x += 1

print("Average score: %d" %float((i / len(scores))))

