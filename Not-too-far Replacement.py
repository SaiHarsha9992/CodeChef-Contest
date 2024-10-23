def solve():
    T = int(input())  
    for _ in range(T):
        N = int(input()) 
        A = list(map(int, input().split())) 
        
        last_element = A[N]  
        first_N_elements = sorted(A[:N])  
        for i in range(N):
            if ((first_N_elements[i] <= 2 * last_element) and (first_N_elements[i]>last_element)):
                first_N_elements[i], last_element = last_element, first_N_elements[i]
        
        result = sum(first_N_elements)
        print(result)

solve()
