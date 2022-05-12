import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    assinatura_1 = as_a
    assinatura_2 = as_b
    diferencas = 0
    diferenca_total = 0
    i = 0
    while i < len(assinatura_1):
        diferencas = abs(assinatura_1[i] - assinatura_2[i])
        diferenca_total = diferenca_total + diferencas
        i += 1
    similaridade = (diferenca_total / 6)
    return similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    total_palavras = []
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        novas_frases = separa_frases(sent)
        for fr in novas_frases:
            novas_palavras = separa_palavras(fr)
            total_palavras.extend(novas_palavras)
    lpt = 0
    for palavra in total_palavras:
        lp = len(palavra)
        lpt = lpt + lp
    len_palavras_total = lpt
    wal_texto = (len_palavras_total / len(total_palavras))
    lista_palavras = total_palavras
    sem_palavras_repetidas = n_palavras_diferentes(lista_palavras)
    ttr_texto = (sem_palavras_repetidas / len(total_palavras))
    sem_palavras_que_repetem = n_palavras_unicas(lista_palavras)
    hlr_texto = (sem_palavras_que_repetem / len(total_palavras))
    caracteres = 0
    for caracter in texto:
        if caracter != '.' and caracter != '?' and caracter != '!':
            caracteres = len(caracter) + caracteres
    numero_sentencas = separa_sentencas(texto)
    numero_sentencas = len(sentencas)
    sal_texto = (caracteres / numero_sentencas)
    frases = re.split(r'[,:;?.!]+', texto)
    if frases[-1] == '':
        del frases[-1]
    numero_frases = len(frases)
    sac_texto = (numero_frases / numero_sentencas)
    caracteres = 0
    for caracter in frases:
        caracteres = len(caracter) + caracteres
    pal_texto = (caracteres / numero_frases)
    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    numero_texto = 1
    similaridade_1 = 10 ** 5
    for texto in textos:
        as_b = ass_cp
        parametros = calcula_assinatura(texto)
        as_a = parametros
        similaridade_2 = compara_assinatura(as_a, as_b)
        if similaridade_2 < similaridade_1:
            similaridade_1 = similaridade_2
            texto_infectado = numero_texto
        numero_texto += 1
    return texto_infectado

valor_assinatura=le_assinatura()
conjunto_textos=le_textos()
avaliacao=avalia_textos(conjunto_textos, valor_assinatura)
print(f"O autor do texto {avaliacao} está infectado com COH-PIAH.")

