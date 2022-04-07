"""
Given a list of integers find the closest to zero.
If there is a tie, choose the positive value.
"""

lst = [2, 74, 56, -8, 12, -40, -2, 70, -4, -66, -4]

lst_negative = []
lst_positive = []

for i in range(len(lst)):
    element = lst[i]
    if element < 0:
        lst_negative.append(element)
    else:
        lst_positive.append(element)

lst_negative.sort()
lst_negative.reverse()
lst_positive.sort()

if abs(lst_negative[0]) < lst_positive[0]:
    print(lst_negative[0])
elif abs(lst_negative[0]) > lst_positive[0]:
    print(lst_positive[0])
else:
    print(lst_positive[0])
