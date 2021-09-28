from solution import subtracao_de_listas
import pytest

# Utilizando os exemplos agora com o pytest.mark

#verifica lista_numeros_impares

@pytest.mark.parametrize("test_input, expected", [([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6, 8]), ([1, 3, 5, 7, 9])])

def test_subtracao_de_listas(test_input, expected):
    assert subtracao_de_listas(test_input) == expected

#verifica lista_Maiuscula e lista_letras
                                                  
@pytest.mark.parametrize("test_input, expected", [(['A', 'B', 'C', 'D', 'E'], ['A', 'b', 'c', 'D', 'E']), (['B', 'C'])])

def test_subtracao_de_listas(test_input, expected):
    assert subtracao_de_listas(test_input) == expected
                         
#verifica lista_anime e lista_fã

@pytest.mark.parametrize("test_input, expected", [([''Naruto', 'Dragon Ball', 'Bleach', 'Jujutsu Kaisen', 'Kimetsu no Aiba'], ['Naruto', 'Dragon Ball', 'Jujutsu Kaisen']), (['bleach', 'kimetsu no aiba'])])

def test_subtracao_de_listas(test_input, expected):
    assert subtracao_de_listas(test_input) == expected

#verifica lista_nome e lista_nome_maior

@pytest.mark.parametrize("test_input, expected", [(['Quézia Moura', 'Kevin Shinohara', 'Cleilton Sousa'], ['Kevin Shinohara', 'Cleilton Sousa']), (['Quezia Moura'])])

def test_subtracao_de_listas(test_input, expected):
    assert subtracao_de_listas(test_input) == expected

#verifica lista_name e lista_name_maior

@pytest.mark.parametrize("test_input, expected", [(['Quézia Moura', 'Kevin Shinohara', 'Cleilton Sousa'], ['Kevin Shinohara', 'Cleilton Sousa']), (['QuéziaMoura'])])                                                    

def test_subtracao_de_listas(test_input, expected):
    assert subtracao_de_listas(test_input) == expected

#verifica lista_variaveis e lista_variaveis_variadas

@pytest.mark.parametrize("test_input, expected", [(['2', '4'], ['1', 2, '3', 4]), ([2, 4])]) 

def test_subtracao_de_listas(test_input, expected):
    assert subtracao_de_listas(test_input) == expected
    
#verifica lista_numeros_inteiros e lista_numeros_reais

@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 4, 5], [1.0, 2.0, 3.0, 4.0]), ([5])]) 

def test_subtracao_de_listas(test_input, expected):
    assert subtracao_de_listas(test_input) == expected
    

