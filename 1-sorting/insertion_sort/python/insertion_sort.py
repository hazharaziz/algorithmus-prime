

def insertion_sort(numbers):

    for j in range(1, len(numbers)):
        key = numbers[j]
        i = j - 1
        while (i > -1) and (numbers[i] > key):
            numbers[i + 1] = numbers[i]
            i -= 1
        numbers[i + 1] = key

