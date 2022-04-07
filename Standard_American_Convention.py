"""
На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в
соответствии со стандартным американским соглашением о запятых в больших числах.

*Формат входных данных
На вход программе подаётся натуральное число n, (0 < n < 10^100).

*Формат выходных данных
Программа должна вывести число с запятыми в соответствии с условием задачи.
"""

num = input()

num_rev = ''

for i in range(len(num)-1, -1, -1):
    num_rev = num_rev + num[i]

result = ''

while len(num_rev) != 0:
    if len(num_rev) > 3:
        result = result + num_rev[:3] + ','
    else:
        result = result + num_rev[:3]
    num_rev = num_rev[3:]

result_rev = ''

for i in range(len(result)-1, -1, -1):
    result_rev = result_rev + result[i]

print(result_rev)