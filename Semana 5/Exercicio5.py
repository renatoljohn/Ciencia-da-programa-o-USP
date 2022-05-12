def maximo(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    elif y > z:
        return y
    else:
        return z


