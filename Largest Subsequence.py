t = int(input())

for _ in range(t):
    
    n = int(input())
    
    s = input()
    res = 0
    for i in range(n):
        if(s[i] == s[0]):
            res = max(res, i+1)
        if(s[i] == s[n-1]):
            res = max(res, n-i)
    
    print(res)