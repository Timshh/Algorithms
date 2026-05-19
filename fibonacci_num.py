def fibonacci_num(current):
    if (current <= 1):
        return current
    return fibonacci_num(current - 1) + fibonacci_num(current - 2)

print(fibonacci_num(201))