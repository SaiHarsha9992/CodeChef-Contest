# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    attA = list(map(int, input().split()))
    defA = list(map(int, input().split()))
    attP = list(map(int, input().split()))
    defP = list(map(int, input().split()))
    suma = sum(attA)
    sump = sum(attP)
    sumda = sum(defA)
    sumdp = sum(defP)
    if (suma > sump and sumda > sumdp):
        print("A")
    elif (suma < sump and sumda < sumdp):
        print("P")
    else:
        print("DRAW")