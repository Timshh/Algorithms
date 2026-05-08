def DoubleSum(A, B):
    C = []
    shouldAdd = False
    for i in range(len(A) - 1, -1, -1):
        num = A[i] + B[i] + int(shouldAdd)
        C.append(num%2)
        shouldAdd = False
        if num > 1:
            shouldAdd = True
    if shouldAdd:
        C.append(1)
    C.reverse()
    return C

print (DoubleSum([1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1]))