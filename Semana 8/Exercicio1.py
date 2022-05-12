def remove_repetidos(a):
    lista = list(dict.fromkeys(a))
    lista.sort()
    return lista
