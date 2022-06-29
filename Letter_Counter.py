"""
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему
добавляется количество повторений.
"""
import string

value = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'


def to_count(input_string):
    result = ''
    counter = 1

    for i in range(len(input_string) - 1):
        letter_cur = input_string[i]
        letter_next = input_string[i + 1]

        if letter_cur not in string.ascii_uppercase:
            return 1
        if letter_cur == letter_next:
            counter += 1
        if letter_cur != letter_next or i >= len(input_string) - 2:
            if counter > 1:
                result += letter_cur + str(counter)
            else:
                result += letter_cur
            counter = 1

    return result


print(to_count(value))
