n=int(input("enter starting number:"))
n1=int(input("enter end range:"))
for n in range(n,n1):
    sum=0
    temp=n
    o=len(str(n))
    while(temp>0):
        d=temp%10
        sum+=d**o
        temp//=10
    if n==sum:
       print(f"{n} is armstrong number")