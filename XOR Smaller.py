# Number of test cases
t = int(input())

for _ in range(t):
    # Input for each test case
    n = int(input())
    arr = list(map(int, input().split()))

    cd = arr[0]
    for num in arr:
        cd &= num
    res = 0
    i = 1
    while i < (1 << 30):
        if cd & i:
            res += i
        i *= 2

    print(res)
