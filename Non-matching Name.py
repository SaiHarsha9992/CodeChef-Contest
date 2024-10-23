def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        S_A = set(input().strip()) 
        S_B = set(input().strip())  
        
        for char in range(ord('a'), ord('z') + 1):
            if chr(char) not in S_A and chr(char) not in S_B:
                print("YES")
                break
        else:
            print("NO")

solve()
