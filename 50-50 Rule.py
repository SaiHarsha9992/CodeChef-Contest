# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if x < 50:
        print("Z")
    elif x >= 50 and y < 50:
        print("F")
    else:
        print("A")