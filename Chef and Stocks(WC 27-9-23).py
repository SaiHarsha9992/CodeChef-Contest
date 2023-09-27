# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr)-min(arr))