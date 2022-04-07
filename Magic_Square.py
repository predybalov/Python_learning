"""
Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная
из всех чисел 1, 2, 3,...n^2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей
равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

*Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

*Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
"""

n = int(input())

matrix = []

for i in range(n):
    temp = input().split()
    elem = []
    for e in temp:
        elem.append(int(e))
    matrix.append(elem)

num_set = set()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        num_set.add(matrix[i][j])
num_set = list(num_set)

sum_row = sum(matrix[0])
sum_column, sum_main, sum_side = 0, 0, 0

for i in range(len(matrix)):
    if sum_row != sum(matrix[i]):
        break
    else:
        sum_row = sum(matrix[i])
    for j in range(len(matrix[i])):
        if i == j:
            sum_main += matrix[i][j]
        if i == n - 1 - j:
            sum_side += matrix[i][j]

for i in range(len(matrix)):
    sum_column = 0
    for j in range(len(matrix[i])):
        sum_column += matrix[j][i]
    if sum_column != sum_row:
        break

if sum_row == sum_column == sum_main == sum_side and len(num_set) == n*n and num_set[0] == 1:
    print('YES')
else:
    print('NO')