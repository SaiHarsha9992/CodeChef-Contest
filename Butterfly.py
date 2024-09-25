# cook your dish here
t = int(input())
for _ in range(t):
    R, G, B = map(int, input().split())
    ms = max(R, G, B)

    if ms <= (R + G + B) - ms:
        print("YES")
    else:
        print("NO")