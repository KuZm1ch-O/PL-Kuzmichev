file = open('VVOD.txt')

matrix = []

for i in file.readlines():
    i = i.split()
    for j in range(len(i)):
        i[j] = int(i[j])
    matrix.append(i)

n = len(matrix)
count = 0
total = 0
for i in range(n):
    for j in range(i + 1, n):
        element = matrix[i][j]
        if element > 0:
            count += 1
        total += element

file1 = open("VIVOD.txt", "w")
file1.write(f'Sum: {total}\n')
file1.write(f'Count: {count}\n')