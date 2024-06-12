a=int(input("enter number:"))
t=a
r=0
while t>0:
    r+=t%10
    t//=10
if(a%r==0):
    print(f'{a} is harshad number')