# cook your dish here
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = 0
    
    isSwaped = False
    for i in arr:
        
        if i <= d:
            if isSwaped == True:
                res += 1
                isSwaped = False
        else:
            if isSwaped == False:
                res += 1
                isSwaped = True
    print(res)