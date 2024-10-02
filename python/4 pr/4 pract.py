a=int(input('Введите число 1 '))
b=int(input('Введите число 2 '))
while a<=b:
	print(a)
	a+=1
print('------')
#--------2--------
a = int(input('Введите число 1 '))
b = int(input('Введите число 2 '))

if a<b:
		while a<=b:
			print(a)
			a+=1
else:
	while a>=b:
		print(a)
		a-=1


#-----------9-------------
n=int(input('Введите кол-во чисел Фибоначчи '))
a,b=0,1
summa=0
for i in range (n):
	summa+=a
	a=b
	b=a+b
print('Сумма чисел Фибоначчи равна ', summa)


