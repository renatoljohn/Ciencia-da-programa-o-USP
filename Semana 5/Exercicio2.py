def ePrimo(y):
    total = 0

    for n in range(1, y+1):
        if y % n ==0:
            total += 1
    if total == 2:
        return 1
    else:
        return 0

def maior_primo(x):
    resultado = 0
    for n in range(2, x+1):
        primo = ePrimo(n)
        if primo == 1:
            resultado = n
    return resultado








