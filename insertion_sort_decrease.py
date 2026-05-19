def swap(a, first_id, second_id):
    buffer = a[first_id]
    a[first_id] = a[second_id]
    a[second_id] = buffer

def insertion_sort_decrease(a):
    for i in range(1, len(a)):
        num = a[i]
        j = i-1
        while j >= 0 and num > a[j]:
            swap(a, j, j+1)
            j -= 1
    return a

print (insertion_sort_decrease([1, 8, 4, 2, 3, 7, 5, 6, 9, 0]))