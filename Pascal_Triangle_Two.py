"""
На вход программе подается натуральное число nn. Напишите программу, которая выводит
первые n строк треугольника Паскаля.

*Формат входных данных
На вход программе подается число n (n >= 1).

*Формат выходных данных
Программа должна вывести первые n строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

1
1 1
1 2 1
1 3 3 1
........
"""

n = int(input())

line = []
triangle = []
result = []

for i in range(1, n + 1):
    triangle = [0] * i
    for j in range(len(triangle)):
        if j == 0:
            triangle[j] = 1
        elif j == len(triangle) - 1:
            triangle[j] = 1
        else:
            triangle[j] = line[j-1] + line[j]
    line = triangle.copy()

    result.append(triangle)


for row in result:
    print(*row)