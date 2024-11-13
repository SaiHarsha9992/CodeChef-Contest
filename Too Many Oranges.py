# cook your dish here
t = int(input())

for _ in range(t):
    
    N, K = map(int, input().split())
    
    min_slices = 10 * N
    max_slices = 12 * N
    
    if min_slices <= K <= max_slices:
        print("YES")
    else:
        print("NO")