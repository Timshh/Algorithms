def Swap(Array, firstID, secondID):
    buffer = Array[firstID]
    Array[firstID] = Array[secondID]
    Array[secondID] = buffer

def InsertionSortDecrease(Array):
    for i in range(1, len(Array)):
        num = Array[i]
        j = i-1
        while j >= 0 and num > Array[j]:
            Swap(Array, j, j+1)
            j -= 1
    return Array

print (InsertionSortDecrease([1, 8, 4, 2, 3, 7, 5, 6, 9, 0]))