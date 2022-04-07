"""
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
последовательности одинаковых символов заданной строки в подсписки.

*Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

*Формат выходных данных
Программа должна вывести указанный вложенный список.
"""

sample = input()

sample = sample.replace(' ', '')

result = []
elem = [sample[0]]

for i in range(1, len(sample)):
    if elem[0] != sample[i]:
        result.append(elem)

    if sample[i] == elem[-1]:
        elem.append(sample[i])
    else:
        elem = [sample[i]]

    if i == len(sample) - 1:
        result.append(elem)

print(result)