# cook your dish here
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    s = (1000-a-b)//21
    
    ss = 299-a
    
    res = min(s, ss)
    
    print(res)