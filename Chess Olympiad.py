# cook your dish here

w, d, l = map(int, input().split())

at = w + (d*0.5)

bt = l + (d*0.5)

tot = w + d + l

at = at + (4 - tot)

if at > bt:
    print("YES")
else:
    print("NO")