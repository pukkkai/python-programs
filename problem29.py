m=1
a=int(input("input a no.:"))
for i in range(1,(a+1)):
    if i<a:
        print(i, " x ", end="")
    m=m*i
print(a, "=", m)
