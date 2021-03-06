"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

*---*
**-**
*****
**-**
*---*

*Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы (целые числа) построчно через пробел.

*Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

*Примечание
Элементы диагоналей также учитываются.
"""

n = int(input())
matrix = [[]*n for _ in range(n)]

for r in range(n):
    row = input().split()
    for elem in row:
        elem = int(elem)
        matrix[r].append(elem)

max_num = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (j <= i <= n-1-j) or (j >= i >= n-1-j):
            if matrix[i][j] > max_num:
                max_num = matrix[i][j]

print(max_num)