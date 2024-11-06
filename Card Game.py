
T = int(input())

results = []

for _ in range(T):
    N, X = map(int, input().split())
    
    if N % 2 == 0:
        odd_count = N // 2
        even_count = N // 2
    else:
        odd_count = (N + 1) // 2
        even_count = (N - 1) // 2
    
    if X % 2 == 0:
        ways = even_count - 1
    else:
        ways = odd_count - 1
    
    results.append(ways)

for result in results:
    print(result)
