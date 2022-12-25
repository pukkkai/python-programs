a=int(input("input a no.:"))
b=0
for c in range(2,(a+1)):
    for d in range(1,(c+1)):
        if c%d==0:
            b=b+1
    if b==2:
        print(c)
    b=0



