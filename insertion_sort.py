def insertion_sort(a):
    for i in range(1, len(a)):
        num = a[i]
        j = i - 1
        while j >= 0 and num < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = num
    return a

def insertion_sort_id(a):
    acopy = [1]
    for i in range(1, len(a)):
        num = a[i]
        j = i - 1
        while j >= 0 and num < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = num
        acopy.append(j + 2)
    return acopy

print (insertion_sort_id([1, 8, 4, 2, 3, 7, 5, 6, 9, 0, 31, 41, 59, 26, 41, 58]))
print (insertion_sort([1, 8, 4, 2, 3, 7, 5, 6, 9, 0, 31, 41, 59, 26, 41, 58]))