T = int(input())

for _ in range(T):
    N = int(input())
    if N < 4:
        print("0")
    else:
        max_area = 0
        half_perimeter = N // 2
    
        for a in range(1, half_perimeter):
            b = half_perimeter - a
            area = a * b
            max_area = max(max_area, area)
    
        print(max_area)
