n=int(input("enter number:"))
sum=0
temp=n
while(temp>0):
    d=temp%10
    sum+=d**3
    temp//=10
if n==sum:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")