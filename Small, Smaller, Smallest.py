t = int(input())

for _ in range(t):
    n = int(input())
    st = input()
    
    cz = st.count('0') 
    co = n - cz

    if co == 0:
        ans = cz  
    elif co % 2 != 0:
        ans = 1  
    else:
        ans = 0  
    
    print(ans)
