def factnum(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factnum(n-1)
n=int(input("enter any number:"))
a=factnum(n)
print(a)