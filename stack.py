def stack(a):
    order = []
    for i in range(0, len(a)):
        if a[i] == "+" :
            order.append(a[i+1])
        elif a[i] == "-":
            print(order.pop())

stack(["+", 1, "+", 10, "-", "+", 2, "+", 1234, "-"])