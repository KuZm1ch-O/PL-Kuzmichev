#-----------1----------
n=int(input('Введите длинну массива: '))
a=[]
for i in range(n):
    print('Введите ',i,' элемент')
    a.append(int(input()))

print('Исходный массив а: ',a)
a.reverse()
print('Массив в обратном порядке:',a)
#--------2-----------
n=int(input('Введите длинну массива: '))
a=[]
for i in range(n):
    print('Введите ',i,' элемент')
    a.append(int(input()))
o=0
b=len(a)
s=sum(a)
c=s//b
for i in range(len(a)):
    if a[i] == 0:
        a[i] = c
print(a)
