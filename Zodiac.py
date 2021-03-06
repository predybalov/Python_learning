"""
Китайский гороскоп назначает животным годы в 1212-летнем цикле. Один 1212-летний цикл показан в таблице ниже.
Таким образом, 2012 год будет очередным годом дракона.
Напишите программу, которая считывает год и отображает название связанного с ним животного. Ваша программа должна
корректно работать с любым годом, не только теми, что перечислены в таблице.

*Формат входных данных
На вход программе подается одно целое число – год.

*Формат выходных данных
Программа должна вывести текст – название животного.
"""

year = int(input()) % 12

horoscope = {0: 'Обезьяна', 1: 'Петух', 2: 'Собака', 3: 'Свинья', 4: 'Крыса', 5: 'Бык', 6: 'Тигр',
             7: 'Заяц', 8: 'Дракон', 9: 'Змея', 10: 'Лошадь', 11: 'Овца'}

print(horoscope[year])