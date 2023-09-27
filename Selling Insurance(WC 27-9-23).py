# cook your dish here
import math
t = int(input())
for i in range(t):
    n = int(input())
    if 500%n == 0:
        print(500//n)
    else:
        print((500//n)+1)
    