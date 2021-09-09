import pytest
from solution import primeiras_ocorrencias

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
def test_ocorrencias():
    assert primeiras_ocorrencias('abracadabra') == {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}

def test_ocorrencias_um_caractere():
    assert primeiras_ocorrencias('y') == {'y': 0}

def test_ocorrencias_string_vazia():
    assert primeiras_ocorrencias('') == {}

def test_ocorrencias_caracteres_especiais():
    assert primeiras_ocorrencias('ola, mundo!?@') == {'o': 0, 'l': 1, 'a': 2, ',': 3, ' ': 4, 'm': 5, 'u': 6, 'n': 7, 'd': 8, '!': 10, '?': 11, '@': 12} 

def test_ocorrencias_repeticao():
    assert primeiras_ocorrencias('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaa') == {'a': 0, 'b': 36}
