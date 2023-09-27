# cook your dish here
import math
t = int(input())
for i in range(t):
    l, v1, v2 = map(int, input().split())
    to = math.ceil(l/v1)
    h = math.ceil(l/v2)
    if to == h:
        print(-1)
    else:
        c = to-h-1
        print(c)
        
