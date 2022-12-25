a=int(input("input a no.:"))
b=int(input("input a no.:"))
c=int(input("input a no.:"))
if a>b and a<c or a<b and a>c:
    print(a)
elif b>a and b<c or b<a and b>c:
    print(b)
elif c>a and c<b or c<a and c>b:
    print(c)
