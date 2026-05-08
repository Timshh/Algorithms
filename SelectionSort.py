def SelectionSort(Array):
    for i in range(0, len(Array)):
        min = Array[i]
        minID = i
        for j in range(i, len(Array)):
            if Array[j] < min:
                min = Array[j]
                minID = j
        buffer = Array[minID]
        Array[minID] = Array[i]
        Array[i] = buffer
    return Array

print (SelectionSort([1, 2, 3, 7, 3, 6, 7, 2, 9, 4, 7, 8, 2, 65, 8, 23, 6, 37, 31, 7, 34, 1, 7, 9, 3, 5, 2, 2]))