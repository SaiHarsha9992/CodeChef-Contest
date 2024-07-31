# cook your dish here
a, b, c, x = map(int, input().split())

r = a * b * c

s = pow(x, 3)

if s < r:
    print("Cuboid")
elif s > r:
    print("Cube")
else:
    print("Equal")