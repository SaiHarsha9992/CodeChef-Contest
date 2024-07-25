# cook your dish here
a, b = map(int , input().split())
if a == b:
    print("SAME")
elif a > b:
    print("DECREASED")
else:
    print("INCREASED")