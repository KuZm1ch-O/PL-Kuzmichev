#------1.1------
a=int(input())
b=int(input())
c=int(input())
d=[1,2,3]
if a in d:
	print(a)
if b in d:
	print(b)
if c in d:
	print(c)
#------1.2------
a=input()
if a[0]==a[1]:
	print('ДА')
else:
	print('НЕТ')
#--------2.1-----------
a=int(input())
b=int(input())
if a>b: x=a-b
if a<b: x=a+b
if a==b: x=11
print(x)

#--------2.2------------
f=int(input())
k=int(input())
if f<5 and k>2:
	R=f+k-1
if k<2: R=k^2
if k==2: R=1
print(R)
#--------3.1-------
a=int(input())
b=int(input())
if a>b:
	print(a)
else: print(b)
#---------3.2---------
a=int(input())
if a%2==0:
	print('Число четное')
else: print('Число нечетное')