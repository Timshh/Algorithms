b = 201
def CalcFibb(curr):
    if (curr <= 1):
        return curr
    return CalcFibb(curr - 1) + CalcFibb(curr - 2)

print(CalcFibb(b))