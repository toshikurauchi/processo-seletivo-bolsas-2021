from solution import primeiras_ocorrencias
import pytest

#testando exercício de tuplas com pytest.parametrize

@pytest.mark.parametrize("caractere1, índices_caracatere1", [('NinJa', {'N': 0, 'i': 1, 'n': 2, 'J': 3, 'a': 4})])

def test_primeiras_ocorrencias(caractere1, índices_caracatere1):
    assert primeiras_ocorrencias(caractere1) == índices_caracatere1

#com somente maiusculas

@pytest.mark.parametrize("caractere2, índices_caracateres", [('POKEMON', {'P': 0, 'O': 1, 'K': 2, 'E': 3, 'M': 4, 'N': 6})])

def test_primeiras_oc(caractere2, índices_caracateres):
    assert primeiras_ocorrencias(caractere2) == índices_caracateres

#com espaços

@pytest.mark.parametrize("caractere3, índices_caracateres3", [('Linkin Park', {'L': 0, 'i': 1, 'n': 2, 'k': 3, ' ': 6, 'P': 7, 'a': 8, 'r': 9})])

def test_primeiras_oc3(caractere3, índices_caracateres3):
    assert primeiras_ocorrencias(caractere3) == índices_caracateres3

#com assentos

@pytest.mark.parametrize("caractere4, índices_caracateres4", [('Cláudio Sérgio', {'C': 0, 'l': 1, 'á': 2, 'u': 3, 'd': 4, 'i': 5, 'o': 6, ' ': 7, 'S': 8, 'é': 9, 'r': 10, 'g': 11})])

def test_primeiras_oc4(caractere4, índices_caracateres4):
    assert primeiras_ocorrencias(caractere4) == índices_caracateres4
