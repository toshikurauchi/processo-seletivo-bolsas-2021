from solution import subtracao_de_listas
import pytest

def solucao(lista1, lista2):
    resposta = []

    for elemento in lista1:
        if elemento not in lista2:
            resposta.append(elemento)

    return resposta

def test_subtraiListas():
    lista1 = [2, 7, 3.1, 'banana']
    lista2 = [2, 'banana', 'carro']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro ao subtrair as listas, era esperado {resposta}, mas foi devolvido {resultado}."

def test_inverteuInput():
    lista1 = [2, 7, 3.1, 'banana']
    lista2 = [2, 'banana', 'carro']
    resultado = subtracao_de_listas(lista2, lista1)
    resposta = solucao(lista2, lista1)
    assert resultado == resposta, f"Erro as entradas foram invertidas."

def test_lista1Vazia():
    lista1 = []
    lista2 = ['banana', 'sundae']
    resultado = subtracao_de_listas(lista1, lista2)
    assert resultado == lista1, f"Erro quando a primeira lista estava vazia era esperado {lista1}, mas foi devolvido {resultado}."

def test_lista2Vazia():
    lista1 = ['banana', 'sundae']
    lista2 = []
    resultado = subtracao_de_listas(lista1, lista2)
    assert resultado == lista1, f"Erro quando a segunda lista estava vazia era esperado {lista1}, mas foi devolvido {resultado}."

def test_lista1Menor():
    lista1 = ['banana', 'sundae', 'chocolate']
    lista2 = ['chocolate', 'bife', 'pudim', 'brigadeiro', 'maçã']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando a primeira lista era menor que a segunda, era esperado {resposta}, mas foi devolvido {resultado}."

def test_lista2Menor():
    lista1 = ['chocolate', 'bife', 'pudim', 'brigadeiro', 'maçã']
    lista2 = ['banana', 'sundae', 'chocolate']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando a primeira lista era menor que a segunda, era esperado {resposta}, mas foi devolvido {resultado}."

def test_difCase():
    lista1 = ['BANANA', 'sundae', 'Pudim']
    lista2 = ['banana', 'SUNDAE', 'pUDIM']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando haviam elementos escritos com as mesmas letras mas cases diferentes, era esperado {resposta}, mas foi devolvido {resultado}."

def test_lista1Pequena():
    lista1 = ['banana']
    lista2 = ['porcos', 'glitter', 'piscina', 'humanos']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando a lista 1 tinha apenas um elemento, era esperado {resposta}, mas foi devolvido {resultado}."

def test_lista2Pequena():
    lista1 = ['porcos', 'glitter', 'piscina', 'humanos']
    lista2 = ['banana']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando a lista 2 tinha apenas um elemento, era esperado {resposta}, mas foi devolvido {resultado}."

def test_lista1Grande():
    lista1 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    lista2 = [1, 4, 9, 11, 10]
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando a lista 1 Era muito grande, era esperado {resposta}, mas foi devolvido {resultado}."

def test_lista2Grande():
    lista1 = [1, 4, 9, 11, 10]
    lista2 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando a lista 1 Era muito grande, era esperado {resposta}, mas foi devolvido {resultado}."

def test_elementosRepetidos():
    lista1 = ['banana', 'sundae', 'pudim', 'banana', 'maçã', 'banana', 'sundae']
    lista2 = ['banana', 'nhoque', 'misto-quente', 'sundae', 'sundae', 'sundae']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro quando haviam elementos repetidos nas listas, era esperado {resposta}, mas foi devolvido {resultado}."
    
def test_elementosForaOrdem():
    lista1 = ['avião', 'trem', 'carro', 'navio', 'humberto']
    lista2 = ['navio', 'carro', 'avião', 'trem', 'bicicleta']
    resultado = subtracao_de_listas(lista1, lista2)
    resposta = solucao(lista1, lista2)
    assert resultado == resposta, f"Erro as listas não tinham os elementos nos mesmos indices, era esperado {resposta}, mas foi devolvido {resultado}."

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
