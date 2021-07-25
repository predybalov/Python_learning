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