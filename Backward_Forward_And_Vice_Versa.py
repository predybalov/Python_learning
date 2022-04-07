"""
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
Если в списке нечетное количество элементов, то последний остается на своем месте.

*Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

*Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним пробелом.
"""

nums = input()

nums_list = nums.split(' ')


def change_list(txt):
    new_list = []
    for i in range(0, len(txt), 2):
        new_list.append(txt[i + 1])
        new_list.append(txt[i])
    new_string = ' '.join(new_list)

    return new_string


if len(nums_list) % 2 != 0:
    end_of_list = nums_list[-1]
    nums_list = nums_list[:-1]
    print(change_list(nums_list), end_of_list)
else:
    print(change_list(nums_list))