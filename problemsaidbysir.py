a=2
b=0
z=0
c=int(input("input a no.:"))
while z<c:
    for i in range(1,(a+1)):
        if a%i==0:
            b=b+1
    if b==2:
        z=z+1
        print(a)
    a=a+1
    b=0
        
    
            
