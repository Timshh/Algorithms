def BubbleSort(Array):
    for i in range(0, len(Array)):
        for j in range(len(Array) - 1, i + 1, -1):
            if Array[j] < Array[j-1]:
                buffer = Array[j]
                Array[j] = Array[j-1]
                Array[j-1] = buffer
    return Array

print (BubbleSort([1, 2, 3, 7, 3, 6, 7, 2, 9, 4, 7, 8, 2, 65, 8, 23, 6, 37, 31, 7, 34, 1, 7, 9, 3, 5, 2, 2]))