a=[[0,1,2],[3,4,5],[6,7,8]]
b=[[0,1,2],[3,4,5],[6,7,8]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        res[i][j]=a[i][j]*b[i][j]
print (res)