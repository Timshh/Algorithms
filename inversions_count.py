def inversions_count(a):
    count = 0
    for i in range(0, len(a) - 1):
         if a[i] > a[i + 1]:
            count += 1
    return count

print (inversions_count([1, 2, 3, 4, 5, 6 ,7, 8, 7, 8, 10, 1, 24, 2]))