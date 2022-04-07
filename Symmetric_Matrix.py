"""
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

*Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы
матрицы построчно через пробел.

*Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
"""

n = int(input())

matrix = []

for i in range(n):
    elem = input().split()
    matrix.append(elem)

is_symmetric = True

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False


if is_symmetric is True:
    print('YES')
else:
    print('NO')