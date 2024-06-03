n = int(input("enter a number :"))
num1=0
num2=1
nxtn=num2
count=1
while count <= n:
	print(nxtn)
	count += 1
	num1, num2 = num2, nxtn
	nxtn = num1 + num2

