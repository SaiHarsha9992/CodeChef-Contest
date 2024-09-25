# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())

    c = y-x
    d = z-y

    if(c == d):
        print(0)
    else:
        print(1)