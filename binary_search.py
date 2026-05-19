def binary_search(a, low, high, b):
    if high < low:
        return low - 1
    mid = low + (high - low)//2
    if b == a[mid]:
        return mid
    elif b < a[mid]:
        return binary_search(a, low, mid - 1, b)
    else:
        return binary_search(a, mid + 1, high, b)

print (binary_search([1, 2, 3, 5, 7, 9, 12, 60, 240, 1606], 1, 10, 60))