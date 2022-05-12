n = int(input("Digite um número inteiro: "))

tem = 0

while n > 0:
    ultimo = n % 10
    ad = (n // 10) % 10
    if ultimo == ad:
        tem = 1
    n = n//10

if tem == 1:
    print("sim")
else:
    print("não")

