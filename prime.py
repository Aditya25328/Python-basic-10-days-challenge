n=int(input("enter a number:"))
if(n==1):
        print("neither prime not composite")
else:
    for i in range(2,n):

        if(n%i)==0:
            print("composite number")
            break
    else:
        print("prime number")