print("1.Addition\n2.subtraction\n3.Multiplication\n4.Division")
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number"))
c=int(input("enter your choice:"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
else:
    print(a/b)
