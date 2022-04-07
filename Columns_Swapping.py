"""
Напишите программу, которая меняет местами столбцы в матрице.

*Формат входных данных
На вход программе на разных строках подаются два натуральных числа n и m — количество строк
и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов,
подлежащих обмену.

*Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.
"""

n, m = int(input()), int(input())

matrix = []

for i in range(n):
    elem = input().split()
    matrix.append(elem)

c, r = input().split()
c, r = int(c), int(r)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == c:
            print(matrix[i][r], end=' ')
        elif j == r:
            print(matrix[i][c], end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()