import pytest
from solution import subtracao_de_listas

#Entradas
lista1=[1,2,3,23,44,"a","b","baaa",9.8]
lista2=[1,3,22,4,"ab","b","da",9.8]
lista3=["1",2,"3",23,44,"a","b","baaa",9.8]
lista4=[1,3,22,4,"ab","b","da",9.8]

#Saídas
saida1=[2,23,44,"a","baaa"]
saida2=[22,4,"ab","da"]
saida3=["1",2,"3",23,44,"a","baaa"]
saida4=[1,3,22,4,"ab","da"]

lista_vazia=[]

#Testes com listas diferentes
@pytest.mark.parametrize("entrada,saida",[([lista1,lista2],[saida1,saida2])])
def test_listas_diferentes(entrada,saida):
    assert subtracao_de_listas(entrada[0],entrada[1])==saida[0]
    assert subtracao_de_listas(entrada[1],entrada[0])==saida[1]

#Testes com lista vazia
@pytest.mark.parametrize("entrada,saida",[([lista1,lista_vazia],[lista1,lista_vazia])])
def test_lista_vazia(entrada,saida):
    assert subtracao_de_listas(entrada[0],entrada[1])==saida[0]
    assert subtracao_de_listas(entrada[1],entrada[0])==saida[1]
    assert subtracao_de_listas(entrada[1],entrada[1])==saida[1]

#Teste com listas iguais
@pytest.mark.parametrize("entrada,saida",[([lista1,lista2],lista_vazia)])
def test_lista_igual(entrada,saida):
    assert subtracao_de_listas(entrada[0],entrada[0])==saida
    assert subtracao_de_listas(entrada[1],entrada[1])==saida

#Testes com tipos diferentes
@pytest.mark.parametrize("entrada,saida",[([lista3,lista4],[saida3,saida4])])
def test_lista_int_string(entrada,saida):
    assert subtracao_de_listas(entrada[0],entrada[1])==saida[0]
    assert subtracao_de_listas(entrada[1],entrada[0])==saida[1]