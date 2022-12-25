a=int(input("input a no.:"))
b=0
c=0
while (a):
    b=b+(10**c)*(a%2)
    a=a//2
    c=c+1
print(b)
