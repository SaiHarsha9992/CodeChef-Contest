# cook your dish here

t = int(input())

for _ in range(t):
    
    a, b, c, m = map(int, input().split())
    
    arr = sorted([a, b, c])
    
    
    if (m >= abs(a-b)) or (m >= abs(b-c)) or (m >= abs(c-a)):
        print("YES")
    else:
        print("NO")