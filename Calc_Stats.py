#Your task is to process a sequence of integer numbers to determine the following statistics:
#
#    o) minimum value
#    o) maximum value
#    o) number of elements in the sequence
#    o) average value
#
#For example: [6, 9, 15, -2, 92, 11]
#
#    o) minimum value = -2
#    o) maximum value = 92
#    o) number of elements in the sequence = 6
#    o) average value = 21.833333

lst = [6, 9, 15, -2, 592, 11]

value = lst[0]
elements_sum = 0

for i in range(len(lst)):
    element = lst[i]
    if element < value:
        value = element
print("Minimum value = " + str(value))

for i in range(len(lst)):
    element = lst[i]
    if element > value:
        value = element
print("Maximum value = " + str(value))

print("Number of elements in the sequence = " + str(len(lst)))

for i in range(len(lst)):
    elements_sum = elements_sum + lst[i]
print("Average value = " + str(round(elements_sum/len(lst), 6)))
