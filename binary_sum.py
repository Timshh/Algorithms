def binary_sum(a, b):
    c = []
    should_add = False
    for i in range(len(a) - 1, -1, -1):
        num = a[i] + b[i] + int(should_add)
        c.append(num%2)
        should_add = False
        if num > 1:
            should_add = True
    if should_add:
        c.append(1)
    c.reverse()
    return c

print (binary_sum([1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1]))