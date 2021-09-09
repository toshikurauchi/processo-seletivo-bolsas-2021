from solution import primeiras_ocorrencias
import pytest


# Testando solução com uma palavra muito longa
def test_primeiras_ocorrencias_palavra_grande():
    palavra = 'pneumoultramicroscopicossilicovulcanoconiótico'
    assert primeiras_ocorrencias(palavra) == {'p': 0, 'n': 1, 'e': 2, 'u': 3, 'm': 4, 'o': 5, 'l': 7, 't': 8, 'r': 9, 'a': 10, 'i': 12, 'c': 13, 's': 16, 'v': 30, 'ó': 41}

# Testando solução com uma frase aleatória
def test_primeiras_ocorrencias_frase():
    palavra = 'olarmaeu  ahoi'
    assert primeiras_ocorrencias(palavra) == {'o': 0, 'l': 1, 'a': 2, 'r': 3, 'm': 4, 'e': 6, 'u': 7, ' ': 8, 'h': 11, 'i': 13}

# Testando solução com números
def test_primeiras_ocorrencias_numeros():
    palavra = 214432423
    assert primeiras_ocorrencias(palavra) == None, "O formato do argumento para função é um inteiro e não uma string"

# Testando solução nula
def test_primeiras_ocorrencias_nulo():
    palavra = ""
    assert primeiras_ocorrencias(palavra) == {}, "O valor inserido está sendo reconhecido como nulo"