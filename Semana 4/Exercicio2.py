n = int(input("Digite o valor de n: "))
numero = 1
while n > 0:
    if numero % 2 == 0:
        numero += 1
    else:
        print(numero)
        n = n -1
        numero += 1
