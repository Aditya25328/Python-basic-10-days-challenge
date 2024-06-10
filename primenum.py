n=int(input("enter starting number:"))
n1=int(input("enter end range:"))
a=[]
for i in range(n,n1):
    if(i>1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            a.append(i)
print(a)