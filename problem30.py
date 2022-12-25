ec=0
oc=0
s=0
v=0
t=0
m=0
for i in range(1,11):
    a=int(input("input a no.:"))
    if a%2==0:
        ec=ec+1
        s=s+a
    else:
        oc=oc+1
        v=v+a
if s==0:
    t=0
else:
    t=s/ec
if v==0:
    m=0
else:
    m=v/oc
print("No. of even nos.=", ec)
print("No. of odd nos.=", oc)
print("Summation of even nos.=", s)
print("Summation of odd nos.=", v)
print("Average of even nos.=", t)
print("Average of odd nos.=", m)
