# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    c = 0
    for j in range(n):
        if arr[j-1] == 2:
            c += 1
    if c%8 == 0:
        print("YES")
    else:
        print("NO")