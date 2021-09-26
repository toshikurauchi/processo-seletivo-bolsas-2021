from solution import subtracao_de_listas


# Escreva seus testes neste arquivo. Para ajudar já importamos a função.

#verifica lista_1 e lista_2
lista_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = [0, 2, 4, 6, 8]
lista_3 = [1, 3, 5, 7, 9]

def test_subtracao_de_listas():
    assert lista_3 == subtracao_de_listas(lista_1, lista_2)

#verifica lista_Maiuscula e lista_letras
lista_Maiuscula = ['A', 'B', 'C', 'D', 'E']
lista_letras = ['A', 'b', 'c', 'D', 'E']
lista_letras_novas = ['B', 'C']

def test_subtracao_de_listas():
    assert lista_letras_novas == subtracao_de_listas(lista_Maiuscula, lista_letras)

#verifica lista_anime e lista_fa
lista_anime = ['Naruto', 'Dragon Ball', 'Bleach', 'Jujutsu Kaisen', 'Kimetsu no Aiba']
lista_fa = ['Naruto', 'Dragon Ball', 'Jujutsu Kaisen']
lista_anime_final = ['bleach', 'kimetsu no aiba']

def test_subtracao_de_listas():
    assert lista_anime_final == subtracao_de_listas(lista_anime, lista_fa)

#verifica lista_nome e lista_nome_maior

lista_nome = ['Quézia Moura', 'Kevin Shinohara', 'Cleilton Sousa']
lista_nome_maior = ['Kevin Shinohara', 'Cleilton Sousa']
lista_nome_final = ['Quezia Moura']

def test_subtracao_de_listas():
    assert lista_nome_final == subtracao_de_listas(lista_nome, lista_nome_maior)

#verifica lista_name e lista_name_maior

lista_name = ['Quézia Moura', 'Kevin Shinohara', 'Cleilton Sousa']
lista_name_bigger = ['Kevin Shinohara', 'Cleilton Sousa']
lista_name_final = ['QuéziaMoura']

def test_subtracao_de_listas():
    assert lista_name_final == subtracao_de_listas(lista_name, lista_name_bigger)

#verifica lista_variaveis e lista_variaveis_variadas
lista_variaveis = ['2', '4']
lista_variaveis_variadas = ['1', 2, '3', 4]
lista_variaveis_final = [2, 4]


def test_subtracao_de_listas():
    assert variaveis_final == subtracao_de_listas(lista_variaveis, lista_variaveis_variadas)
    
#verifica lista_numeros_inteiros e lista_numeros_reais
lista_numeros_inteiros = [1, 2, 3, 4, 5]
lista_numeros_reais = [1.0, 2.0, 3.0, 4.0]
lista_numeros_finais = [5]


def test_subtracao_de_listas():
    assert lista_numeros_finais == subtracao_de_listas(lista_numeros_inteiros, lista_numeros_reais)
    

