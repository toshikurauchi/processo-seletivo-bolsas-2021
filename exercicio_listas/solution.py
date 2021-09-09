def subtracao_de_listas(lista1, lista2):
    resposta = []

    for elemento in lista1:
        if elemento not in lista2:
            resposta.append(elemento)

    return resposta
