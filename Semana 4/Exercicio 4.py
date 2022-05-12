n = int(input("Digite um número inteiro: "))

i = 2
primo = 0

while i < n and i > 1:
    if n % i == 0:
        primo = 1
    i = i - 1

if primo == 0:
    print("primo")
else:
    print("não primo")
