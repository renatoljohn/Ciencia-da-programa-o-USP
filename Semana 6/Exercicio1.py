
def computador_escolhe_jogada(n, m):
    if n > m:
        r = n % (m + 1)
        print(f"\nO computador tirou {r} peça(s)")
    else:
        r = m
        print(f"\nO computador tirou {r} peça(s)")
    return r

def usuario_escolhe_jogada(n, m):
    while True:
        try:
            r = int(input("Quantas peças você vai tirar? "))
        except:
            print(f"Digite um número inteiro maior que 0 e menor ou igual a {m}")
            continue
        if r > 0 and r <= m:
            break
        else:
            print(f"Digite um número inteiro maior que 0 e menor ou igual a {m}")
            continue
    print(f"\nVocê tirou {r} peça(s)")
    return r

def partida():
    enterMsg1 = "Quantas peças? "
    enterMsg2 = "Limite de peças por jogada? "
    while True:
        try:
            n = int(input(enterMsg1))
            m = int(input(enterMsg2))
            if n > 0 and m > 0 and n > m:
                break
            else:
                print("\nAtenção: 'n' e 'm' devem ser inteiros maiores que 0 e 'n' dever ser maior que 'm'")
                continue
        except:
            print("\nPor favor insira somente números inteiros maiores que 0!\nAtenção: 'n' dever ser maior que 'm'")

    if n % (m + 1) == 0:
        print("\nVocê começa")
        whoPlays = "user"
    else:
        print("\nComputador começa")
        whoPlays = "computer"

    while True:
        if whoPlays == "user":
            n -= usuario_escolhe_jogada(n, m)
            whoPlays = "computer"
        else:
            n -= computador_escolhe_jogada(n, m)
            whoPlays = "user"

        print(f"Agora resta(m) {n} peça(s) no tabuleiro.")
        if n == 0:
            if whoPlays == "user":
                winner = "computador"
                print("\nFim do jogo! O %s ganhou!" % winner)
                return winner
            else:
                winner = "VOCÊ"
                print("\nFim do jogo! %s ganhou!" % winner)
                return winner
        elif n < m:
            m = n


def campeonato():
    match = 1
    u = 0
    c = 0
    while match <= 3:
        print("\n**** Rodada %s ****" % match)
        winner = partida()
        match += 1
        if winner == "computador":
            c += 1
        else:
            u += 1
    print("\nPlacar: Você %s X %s Computador" % (u, c))


def main():
    print(5 * "+", " BEM VINDO AO JOGO DO NIM ", 5 * "+")
    print(3 * "-", " Tente ganhar do computador ", 3 * "-")
    choseTypeMsg1 = "Escolha '1' para uma única partida e '2' para campeonato com 3 partidas.\nQualquer outro valor para sair: "
    c = 0;
    while c == 0:
        c = input(choseTypeMsg1)
        try:
            c = int(c)
        except:
            print("\nPor favor, insira um número inteiro")

    if c == 1:
        print("\nVocê escolheu partida simples")
        partida()
    elif c == 2:
        print("\nVocê escolheu campeonato")
        campeonato()
    else:
        print("\nVocê escolheu sair do jogo. Espero ter ver de volta logo!")

main()