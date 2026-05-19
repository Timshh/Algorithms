def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range(len(a) - 1, i + 1, -1):
            if a[j] < a[j-1]:
                buffer = a[j]
                a[j] = a[j-1]
                a[j-1] = buffer
    return a

print (bubble_sort([1, 2, 3, 7, 3, 6, 7, 2, 9, 4, 7, 8, 2, 65, 8, 23, 6, 37, 31, 7, 34, 1, 7, 9, 3, 5, 2, 2]))