n = int(input("Digite um número inteiro: "))

final = 0

while (n>0):

    dig = n%10
    final = final+dig
    n = n//10

print(final)

