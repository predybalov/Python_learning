"""
Bubble Sort
"""


def bubble_sort(sequence):
    length = len(sequence)
    if length < 2:
        return sequence
    else:
        for i in range(length-1):
            for j in range(length-1-i):
                if sequence[j+1] < sequence[j]:
                    sequence[j+1], sequence[j] = sequence[j], sequence[j+1]
        return sequence


sample = [5, 9, 1, 4, 2, 8, 3, 7, 6]

print(bubble_sort(sample))