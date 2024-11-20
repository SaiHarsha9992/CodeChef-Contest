# cook your dish here
t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sad_count = 0
    for b in B:
        if A[b - 1] > 0:
            A[b - 1] -= 1  # Fulfill the request
        else:
            sad_count += 1  # Customer becomes sad
        
    print(sad_count)