def mid_subarray(a, low, mid, high):
    leftsum = float('-inf')
    sum = 0
    maxleft = 0
    for i in range(mid, low - 1, -1):
        sum += a[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = float('-inf')
    sum = 0
    maxright = 0
    for i in range(mid + 1, high + 1):
        sum += a[i]
        if sum > rightsum:
            rightsum = sum
            maxright = i
    return (maxleft, maxright, leftsum + rightsum)


def max_subarray(a, low, high):
    if high == low:
        return (low, high, a[low])
    else:
        mid = (low + high)//2
        leftlow, lefthigh, leftsum = max_subarray(a, low, mid)
        rightlow, righthigh,rightsum = max_subarray(a, mid + 1, high)
        midlow, midhigh, midsum = mid_subarray(a, low, mid, high)
        if leftsum >= rightsum and leftsum >= midsum:
            return (leftlow, lefthigh, leftsum)
        elif rightsum >= leftsum and rightsum >= midsum:
            return (rightlow, righthigh, rightsum)
        else:
            return (midlow, midhigh, midsum)


print (max_subarray([1, 2, 3, 5, 7, 9, 12, -100, 240, 1606, -20, 10], 0, 10))