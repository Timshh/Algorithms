def InsertionSort(Array):
    for i in range(1, len(Array)):
        num = Array[i]
        j = i - 1
        while j >= 0 and num < Array[j]:
            Array[j + 1] = Array[j]
            j -= 1
        Array[j + 1] = num
    return Array

def InsertionSortID(Array):
    arraycopy = [1]
    for i in range(1, len(Array)):
        num = Array[i]
        j = i - 1
        while j >= 0 and num < Array[j]:
            Array[j + 1] = Array[j]
            j -= 1
        Array[j + 1] = num
        arraycopy.append(j + 2)
    return arraycopy

print (InsertionSortID([1, 8, 4, 2, 3, 7, 5, 6, 9, 0]))
print (InsertionSort([1, 8, 4, 2, 3, 7, 5, 6, 9, 0]))