# cook your dish here
import math

def finddivs(n):
    d = set() 
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d

def coed(n):
    d = finddivs(n)
    oc = sum(1 for di in d if di % 2 != 0)
    ec = len(d) - oc
    return oc, ec

t = int(input())

for _ in range(t):
    
    n = int(input())
    oc, ec = coed(n)
    
    if ec > oc:
        print(1)
    elif ec == oc:
        print(0)
    else:
        print(-1)

    
    