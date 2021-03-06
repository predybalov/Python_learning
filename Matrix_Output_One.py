"""
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк
и столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут
элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

*Формат входных данных
На вход программе подаются два числа nn и mm — количество строк и столбцов в матрице, далее идут n×m слов,
каждое на отдельной строке.

*Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
"""

n, m = int(input()), int(input())
words = []

for i in range(n*m):
    word = input()
    words.append(word)

matrix = [[0]*m for _ in range(n)]

counter = 0

for r in range(n):
    for c in range(m):
        matrix[r][c] = words[counter]
        counter += 1

for line in matrix:
    print(*line)