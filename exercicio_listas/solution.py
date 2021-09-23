def subtracao_de_listas(lista1, lista2):
    resposta = []

    for elemento in lista1:
        if elemento not in lista2:
            resposta.append(elemento)

    return resposta
#verifica lista_1 e lista_2
lista_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = [0, 2, 4, 6, 8]
lista_3 = [1, 3, 5, 7, 9]

def test_subtracao_de_listas():
    assert lista_3 == subtracao_de_listas(lista_1, lista_2)
#verifica lis
lista_Maiusculo = ['A', 'B', 'C', 'D', 'E']
lista_letras = ['A', 'b', 'c', 'D', 'E']
lista_letras_novas = ['b', 'c']
