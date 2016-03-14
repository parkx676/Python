def p(n):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if n == 0:
        return ['']
    elif n == 1:
        ans = []
        for i in alpha:
            ans += i
        return ans
    else:
        ans1 = []
        for j in p(n-2):
            for i in alpha:
                ans1 += [i+j+i]
        return ans1
