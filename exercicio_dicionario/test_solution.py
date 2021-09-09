import pytest
from solution import primeiras_ocorrencias

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
def test_ocorrencias():
    assert primeiras_ocorrencias('abracadabra') == {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}

def test_ocorrencias_uma_letra():
    assert primeiras_ocorrencias('y') == {'y': 0}

def test_ocorrencias_frase():
    assert primeiras_ocorrencias('testando mais de uma palavra') == {'t': 0, 'e': 1, 's': 2, 'a': 4, 'n': 5, 'd': 6, 'o': 7, ' ': 8, 'm': 9, 'i': 11, 'u': 17, 'p': 21, 'l': 23, 'v': 25, 'r': 26}

def test_ocorrencias_simbolos():
    assert primeiras_ocorrencias('ola, mundo!') == {'o': 0, 'l': 1, 'a': 2, ',': 3, ' ': 4, 'm': 5, 'u': 6, 'n': 7, 'd': 8, '!': 10}

def test_ocorrencias_entrada_grande():
    assert primeiras_ocorrencias('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaabgtfr')
