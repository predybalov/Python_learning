"""
Quick Sort
"""


def quick_sort(sequence):
    if len(sequence) < 2:
        return sequence
    else:
        pivot = sequence.pop()
        greater = []
        smaller = []
        for item in sequence:
            if item > pivot:
                greater.append(item)
            else:
                smaller.append(item)
        return quick_sort(smaller) + [pivot] + quick_sort(greater)


sample = [5, 9, 1, 4, 2, 8, 3, 7, 6]

print(quick_sort(sample))

