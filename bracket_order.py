def bracket_order(order):
    inside = ""
    if order == "":
        return True
    orient = ""
    if order[0] == "(":
        orient = ")"
    elif order[0] == "[":
        orient = "]"
    else:
        return False
    order = order[1:]
    while order != "":
        curr = order[0]
        order = order[1:]
        if curr == orient:
            return bracket_order(inside) and bracket_order(order)
        inside += curr
    return False

print(bracket_order("()[]()[()]"))