def InsertionSort(Array):
    for i in range(1, len(Array)):
        num = Array[i]
        j = i - 1
        while j >= 0 and num < Array[j]:
            Array[j + 1] = Array[j]
            j -= 1
        Array[j + 1] = num
    return Array
print (InsertionSort([31, 41, 59, 26, 41, 58]))