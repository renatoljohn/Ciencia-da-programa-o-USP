n = int(input("Digite um numero inteiro: "))
final = True
fatoracao = 1

while final:
    if n == 0:
        final = False
    else:
        fatoracao = fatoracao * n
        n = n -1
        if n == 1:
            final = False

print(fatoracao)