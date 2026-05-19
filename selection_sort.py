def selection_sort(a):
    for i in range(0, len(a)):
        min = a[i]
        min_id = i
        for j in range(i, len(a)):
            if a[j] < min:
                min = a[j]
                min_id = j
        buffer = a[min_id]
        a[min_id] = a[i]
        a[i] = buffer
    return a

print (selection_sort([1, 2, 3, 7, 3, 6, 7, 2, 9, 4, 7, 8, 2, 65, 8, 23, 6, 37, 31, 7, 34, 1, 7, 9, 3, 5, 2, 2]))