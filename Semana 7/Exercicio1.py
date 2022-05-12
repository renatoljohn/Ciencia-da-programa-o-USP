largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))


while altura > 0:
    largura2 = largura
    while largura2 > 0:
        print("#", end="")
        largura2 = largura2 - 1
    print()
    altura = altura - 1
