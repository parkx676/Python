def sum2d(n):
    answer = 0
    i = 0
    while i < len(n):
        for j in n[i]:
            answer += j
        i += 1
    return answer
