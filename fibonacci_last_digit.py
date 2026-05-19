def fibonacci_last_digit(current):
    a = []
    a.append(0)
    a.append(1)
    a.append(1)
    for i in range(3, b + 1):
        a.append((a[i-1] + a[i-2]) % 10)
    return a[b]

print(fibonacci_last_digit(327305))