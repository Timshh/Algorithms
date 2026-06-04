def hirsch_id(a):
    maximum = 0
    h_id = 0
    for i in a:
        maximum = max(i, maximum)
    for i in range(maximum, 0, -1):
        count = 0
        for j in a:
            if j >= i: count += 1
        if count >= i:
            h_id = i
            break
    return h_id

print(hirsch_id([3, 0, 6, 1, 5, 100, 50, 20, 10, 7, 8, 17, 197, 76, 31]))