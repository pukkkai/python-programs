a=int(input("input a no.:"))
b=0
for i in range(1,(a+1)):
    if a%i==0:
        b=b+1
if b==2:
    print(a, "is a prime no.")
else:
    print(a, "is a composite no.")

               
               
