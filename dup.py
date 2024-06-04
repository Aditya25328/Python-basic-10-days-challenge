a=[1,2,1,3,43,5,6,7,8,2,4]
b=[]
for i in a:
    if a.count(i)>1:
        if b.count(i)==0:
             b.append(i)
print(b)