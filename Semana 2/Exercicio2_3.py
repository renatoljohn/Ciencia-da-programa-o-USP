numero = input("Digite um número inteiro:")

total = len(numero)
if total < 2:
    print("O dígito das dezenas é 0")
else:
    print(f"O dígito das dezenas é {numero[-2]}")