t=0
avg=0
a=int(input("input marks.:"))
b=int(input("input marks.:"))
c=int(input("input marks.:"))
d=int(input("input marks.:"))
e=int(input("input marks.:"))
f=int(input("input marks.:"))
if a>=30 and b>=30 and c>=30 and d>=30 and e>=30:
    if f>34:
        f=f-34
    else:
        f=0
    t=a+b+c+d+e+f
    avg=t/5
    if avg>=60:
        print("1st")
    elif avg>=45:
        print("2nd")
    elif avg>=34:
        print("3rd")
    else:
        print("fail")
else:
    print("back")
    t=a+b+c+d+e
    avg=t/5
print("Total marks =", t, "Average marks =", avg)


