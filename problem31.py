a=0
b=0
for i in range(1,11):
    c=int(input("input a no.:"))
    if i==1:
        a=c
        b=c
    if c>a:
        a=c
    if c<b:
        b=c
print("Greatest no. =", a)
print("Smallest no. =", b)
