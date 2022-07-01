"""
Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку,
сворачивая соседние по числовому ряду числа в диапазоны.
Примеры:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4"
"""

value = [1, 4, 5, 2, 3, 9, 8, 11, 22, 40, 41, 42, 100, 43, 53, 80, 81, 90, 102, 0, 6]

counter = 1
value.sort()
positions = []

for i in range(len(value)-1):
    cur = value[i]
    nex = value[i+1]

    if nex - cur == 1:
        counter += 1
    else:
        counter = 1

    if nex - cur > 1:
        positions.append(i)

positions.append(len(value)-1)

begin = 0
for p in positions:
    if p > begin:
        if p == positions[-1]:
            print(value[begin], '-', value[p], sep='')
        else:
            print(value[begin], '-', value[p], sep='', end=',')
    else:
        if p == positions[-1]:
            print(value[p])
        else:
            print(value[p], end=',')
    begin = p + 1