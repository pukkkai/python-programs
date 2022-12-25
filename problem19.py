a=input("input o for odd and e for even:")
if a=="o" or a=="e":
    b=int(input("input a no.:"))
    if a=="o":
        c=1
    else:
        c=2
    for i in range(c,(b+1),2):
        print(i)
else:
    print("wrong input")
    
