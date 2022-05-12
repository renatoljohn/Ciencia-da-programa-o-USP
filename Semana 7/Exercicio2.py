largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

altura2 = altura
while altura2 > 0:
    largura2 = largura
    if altura2 == altura or altura2 == 1:
        while largura2 > 0:
            print("#", end="")
            largura2 = largura2 - 1
    else:
        inicio = 0
        while largura2 > 0:
            if inicio == 0 or inicio == largura -1:
                print("#", end="")
                largura2 = largura2 - 1
                inicio += 1
            else:
                print(" ", end="")
                largura2 = largura2 - 1
                inicio += 1

    print()
    altura2 = altura2 - 1