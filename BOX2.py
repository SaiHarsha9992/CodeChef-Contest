# cook your dish here
T = int(input())

for _ in range(T):
    X, Y, K = map(int, input().split())
    diff = abs(X - Y)
    if diff == K:
        print(0)
    elif (X + Y - K) % 2 != 0 or K > X + Y:
        print(-1)
    else:
        print(abs(diff - K) // 2)
