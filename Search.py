def search(a, num):
    count = 0
    for i in range(0, len(a)):
        if a[i] == num:
            count += 1
    return count

print (search([1, 2, 3, 7, 3, 6, 7, 2, 9, 4, 7, 8, 2, 65, 8, 23, 6, 37, 31, 7, 34, 1, 7, 9, 3, 5, 2, 2], 3))