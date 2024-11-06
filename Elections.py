# cook your dish here
T = int(input())

results = []

for _ in range(T):
    N, X = map(int, input().split())
    va = list(map(int, input().split()))
    vb = list(map(int, input().split()))
    
    iw = 0
    g = []
    
    for i in range(N):
        if va[i] > vb[i]:
            iw += 1
        else:
            gap = vb[i] - va[i] + 1
            g.append(gap)
    
    rw = (N // 2) + 1
    if iw >= rw:
        results.append("YES")
        continue
    
    d = rw - iw
    
    g.sort()
    
    vu = 0
    cw = False
    
    for i in range(d):
        if vu + g[i] <= X:
            vu += g[i]
        else:
            cw = False
            break
    else:
        cw = True
    
    results.append("YES" if cw else "NO")

# Print all results for each test case
for result in results:
    print(result)
