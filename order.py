def order(a):
    order = []
    for i in range(0, len(a)):
        if a[i] == "+":
            order.append(a[i+1])
        elif a[i] == "-":
            print(order.pop(0))

order(["+", 1, "+", 10, "-", "-"])