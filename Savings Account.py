import math

t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    total_income = x * y
    if total_income <= z:
        print(0)
    else:
        excess = total_income - z
        
        num_sources_to_reduce = math.ceil(excess / y)
        
        print(num_sources_to_reduce)
