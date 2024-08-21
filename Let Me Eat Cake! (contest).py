# cook your dish here

t = int(input())

for _ in range(t):
    
    a, b = map(int, input().split())
    ans = 0
    while ( a != b ):
        
        if(a > b):
            
            x = (a+1)//2
            
            ans += x
            
            a -= x  
        else:
            
            x = (b+1)//2
            
            ans += x
            
            b -= x
    print(ans)