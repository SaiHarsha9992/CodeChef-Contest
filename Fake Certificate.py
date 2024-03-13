# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    c = 0
    max_count = 0
    for i in range(n):
        if s[i]=='1':
            c += 1
            count = 0
        else:
            count += 1
            max_count = max(max_count, count)
    c += max_count
    print(c)