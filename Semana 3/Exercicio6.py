import math

cord1x = int(input("Digite o 1 eixo x: "))
cord1y = int(input("Digite o 1 eixo y: "))
cord2x = int(input("Digite o 2 eixo x: "))
cord2y = int(input("Digite o 2 eixo y: "))

distancia = int(math.sqrt(((cord1x-cord2x)**2)+((cord1y-cord2y)**2)))

if distancia >= 10:
    print("longe")
elif distancia < 10:
    print("perto")