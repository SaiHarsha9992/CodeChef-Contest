# cook your dish here
def ordered_distances(n, x, y):
    for i in range(n):
        
        p = x[i]
        
        ds = []
        for j in range(n):
            
            d = abs(x[j]-p)
            
            ds.append((d, x[j])) 
            
        ds.sort()
        
        sorted_y = [pair[1] for pair in ds]
        
        if sorted_y == y:
            return i+1
            
    return -1
            
            
            

t = int(input())

for _ in range(t):
    
    n = int(input())
    
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    
    print(ordered_distances(n, x, y))
    
            