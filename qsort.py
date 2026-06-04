def qsort(a, left, right):
    key = a[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while a[i] < key:
            i += 1
        while a[j] > key:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if left < j:
        a = qsort(a, left, j)
    if i < right:
        a = qsort(a, i, right)
    return a

print(qsort([5, 1, 2, 4, 3], 0, 4))