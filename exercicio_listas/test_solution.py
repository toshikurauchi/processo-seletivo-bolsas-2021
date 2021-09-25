import pytest
from solution import subtracao_de_listas

@pytest.fixture
def listas():
    lista1=[1,2,3,23,44,"a","b","baaa",9.8]
    lista2=[1,3,22,4,"ab","b","da",9.8]
    return lista1,lista2

#Testes com listas diferentes
def test_subtracao_de_lista_1(listas):
    assert subtracao_de_listas(listas[0],listas[1])==[2,23,44,"a","baaa"]

def test_subtracao_de_lista_2(listas):
    assert subtracao_de_listas(listas[1],listas[0])==[22,4,"ab","da"]

#Testes com lista vazia
def test_subtracao_de_lista_vazia(listas):
    assert subtracao_de_listas([],listas[0])==[]

def test_subtracao_de_lista_vazia_2(listas):
    assert subtracao_de_listas(listas[0],[])==listas[0]

def test_subtracao_de_lista_vazia_2(listas):
    assert subtracao_de_listas([],[])==[]

#Teste com lista igual
def test_subtracao_de_lista_igual(listas):
    assert subtracao_de_listas(listas[0],listas[0])==[]

#Teste com tipos diferentes
def test_subtracao_de_lista_string_int():
    lista1=["1",2,"3",23,44,"a","b","baaa",9.8]
    lista2=[1,3,22,4,"ab","b","da",9.8]
    assert subtracao_de_listas(lista1,lista2)==["1",2,"3",23,44,"a","baaa"]