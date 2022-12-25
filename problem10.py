a=int(input("input amount:"))
b=a//1000
print("1000 X",b)
c=a-(1000*b)
d=c//500
print("500 X",d)
e=c-500*d
f=e//100
print("100 X",f)
g=a-((1000*b)+(500*d)+(100*f))
h=g//50
print("50 X",h)
i=g-(50*h)
j=i//20
print("20 X",j)
k=i-(20*j)
l= k//10
print("10 X",l)
m=k-(10*l)
n=m//5
print("5 x",n)
o=m-(5*n)
p=o//2
print("2 X",p)
q=o-(2*p)
r=q//1
print("1 X",r)

