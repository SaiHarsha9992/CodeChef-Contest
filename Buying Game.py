def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        tsum = 0
        res = 0
        
        
        a = []
        
        
        xv = list(map(int, input().split()))
        
        yv = list(map(int, input().split()))
        for i in range(n):
            x = xv[i] - yv[i]
            y = yv[i]
            tsum += y
            a.append((x, y))
        
        a.sort()
        
        
        res = tsum
        tsum += a[0][0]
        
        for i in range(1, n):
            tsum += a[i][0]
            res = min(res, tsum)
        
        print(res)

if __name__ == "__main__":
    main()
