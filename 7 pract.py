#----------1.1-------------
def pl(tip,a,b):
    if tip=='kr' and b==0 :
        return 3.14*a**2
    elif tip=='pr':
        return a*b
    elif tip=='tr':
        return 0.5*a*b
tip=input('Введите тип фигуры(kr-круг, pr-прямоугольник,tr- треугольник ) ')
a=int(input('Введите первую сторону фигуры '))
b=int(input('Введите вторую сторону фигуры(если выбран круг, то пишите 0) '))
res=pl(tip,a,b)
print(res)
#------------1.2--------------
def mas(massiv):
    return sum(massiv), sum(massiv)//len(massiv)
#a1=[1,3,6,1,6,9]
#a2=[2,6,26,37,436,72,6]
#a3=[2,7,5,3,8,9,6,3,5,6554,5]
n=int(input('Введите длинну массива(не превышающее 15): '))
a1=[]
a2=[]
a3=[]
for i in range(n):
    print('Введите ',i,' элемент для 1 массива    ')
    a1.append(int(input()))
    print('Введите ',i, ' элемент для 2 массива    ')
    a2.append(int(input()))
    print('Введите ',i, ' элемент для 3 массива    ')
    a3.append(int(input()))
print(mas(a1),mas(a2),mas(a3))
