# cook your dish here
t = int(input())


for _ in range(t):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n <= 3:
        print("0")
        continue
    
    arr.sort()
    print(min(arr[n-1] - arr[2], arr[n-2]-arr[1], arr[n-3]-arr[0]))