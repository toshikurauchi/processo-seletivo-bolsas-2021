from solution import subtracao_de_listas
import pytest

# Utilizando os exemplos agora com o pytest.mark

#verifica lista_numeros_impares

@pytest.mark.parametrize("lista_numeros, lista_pares, lista_impares", [([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9])])

def test_subtracao_de_listas(lista_numeros, lista_pares, lista_impares):
    assert subtracao_de_listas(lista_numeros, lista_pares) == lista_impares

#verifica lista_Maiuscula e lista_letras
                                                  
@pytest.mark.parametrize("lista_Maiuscula, lista_letras, lista_letras_final", [(['A', 'B', 'C', 'D', 'E'], ['A', 'b', 'c', 'D', 'E'], ['B', 'C'])])

def test_subtracao_de_lista(lista_Maiuscula, lista_letras, lista_letras_final):
    assert subtracao_de_listas(lista_Maiuscula, lista_letras) == lista_letras_final
                         
# #verifica lista_anime e lista_fã

@pytest.mark.parametrize("lista_anime, lista_fã, lista_anime_final", [(['Naruto', 'Dragon Ball', 'Bleach', 'Jujutsu Kaisen', 'Kimetsu no Aiba'], ['Naruto', 'Dragon Ball', 'Jujutsu Kaisen'], ['Bleach', 'Kimetsu no Aiba'])])

def test_subtracao_de_list(lista_anime, lista_fã, lista_anime_final):
    assert subtracao_de_listas(lista_anime, lista_fã) == lista_anime_final

# #verifica lista2_nome e lista_nome_maior

@pytest.mark.parametrize("lista2_nome, lista_nome_maior, lista_maior_final", [(['Quézia Moura', 'Kevin Shinohara', 'Cleilton Sousa'], ['Kevin Shinohara', 'Cleilton Sousa'], ['Quézia Moura'])])

def test_subtracao_de_lists(lista2_nome, lista_nome_maior, lista_maior_final):
    assert subtracao_de_listas(lista2_nome, lista_nome_maior) == lista_maior_final

# #verifica lista_name e lista_name_maior

@pytest.mark.parametrize("lista_name, lista_name_maior, lista_name_final", [(['QuéziaMoura', 'KevinShinohara', 'CleiltonSousa'], ['KevinShinohara', 'CleiltonSousa'], ['QuéziaMoura'])])                                                    

def test_subtracao_de_lis(lista_name, lista_name_maior, lista_name_final):
    assert subtracao_de_listas(lista_name, lista_name_maior) == lista_name_final

# #verifica lista_variaveis e lista_variaveis_variadas

@pytest.mark.parametrize("lista_variaveis, lista_variaveis_variadas, lista_variaveis_final", [(['2', '4'], ['1', 2, '3', 4], ['2', '4'])]) 

def test_subtracao_de_ls(lista_variaveis, lista_variaveis_variadas, lista_variaveis_final):
    assert subtracao_de_listas(lista_variaveis, lista_variaveis_variadas) == lista_variaveis_final
    
# #verifica lista_numeros_inteiros e lista_numeros_reais

@pytest.mark.parametrize("lista_numeros_inteiros, lista_numeros_reais, lista_reais_final", [([1.0, 2.0, 3.0, 4.0, 5], [1.0, 2.0, 3.0, 4.0], [5])]) 

def test_subtracao_de_s(lista_numeros_inteiros, lista_numeros_reais, lista_reais_final):
    assert subtracao_de_listas(lista_numeros_inteiros, lista_numeros_reais) == lista_reais_final
    

