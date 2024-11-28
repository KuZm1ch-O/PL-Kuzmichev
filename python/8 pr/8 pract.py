matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrix)
count = 0
total = 0
for i in range(n):
    for j in range(i + 1, n):
        #элемент матрицы
        element = matrix[i][j]
        if element > 0:
            count += 1
        total += element

print("Сумма:", total)
print("Количество положительных элементов:", count)


#-----------------------
martix = [
    [9, 8, 6, 54, 1, 67, 2],
    [10, 818, 1, 2, 8],
    [45, 1, 5, 63, 8]
]

new_matrix = []


for i in martix:
    max_ind = 0
    min_ind = 0
    max_num = -100
    min_num = 100
    for j in range(len(i)):
        n = i[j]
        if n < min_num:
            min_num = n
            min_ind = j
        elif n > max_num:
            max_num = n
            max_ind = j
    first = i[0]
    last = i[-1]
    i[0] = min_num
    i[-1] = max_num
    i[min_ind] = first
    i[max_ind] = last
    new_matrix.append(i)

print(new_matrix)

