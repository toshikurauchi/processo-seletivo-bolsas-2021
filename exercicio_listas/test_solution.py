from typing import Type
import pytest

from solution import subtracao_de_listas

# testes relativos a acertos


@pytest.mark.parametrize("lista1, lista2, result", [
    [
        [2, 7, 3.1, 'banana'],
        [2, 7, 3.1, 'banana'],
        []
    ],
    [
        [2, 7, 3.1, 'banana'],
        [],
        [2, 7, 3.1, 'banana']
    ],
    [
        [2, 7, 3.1, 'banana'],
        [8, 'carro'],
        [2, 7, 3.1, 'banana']
    ],
    [
        [2, 7, 3.1, 'banana'],
        [2, 'banana', 'carro'],
        [7, 3.1]
    ],
    [
        [],
        [],
        []
    ],
    [
        [],
        [2, 'banana', 'carro'],
        []
    ]
])
def test_subtracao_de_listas_equal_type(lista1, lista2, result):
    assert subtracao_de_listas(lista1, lista2) == result

# testes relativos a erros


@pytest.mark.parametrize("lista1, lista2, result", [
    [
        [2, 7, 3.1, 'banana'],
        [2, 7, 3.1, 'banana'],
        [2, 7, 3.1, 'banana']
    ],
    [
        [2, 7, 3.1, 'banana'],
        [],
        []
    ],
    [
        [2, 7, 3.1, 'banana'],
        [8, 'carro'],
        [8, 'carro']
    ],
    [
        [2, 7, 3.1, 'banana'],
        [2, 'banana', 'carro'],
        [3.1, 7]
    ],
    [
        [2, 7, 3.1, 'banana'],
        [2, 'banana', 'carro'],
        [2, 'banana']
    ],
    [
        [],
        [2, 'banana', 'carro'],
        [2, 'banana', 'carro']
    ]
])
def test_subtracao_de_listas_nequal_type(lista1, lista2, result):
    assert subtracao_de_listas(lista1, lista2) != result

# testes relativos a exceções


@pytest.mark.parametrize("lista1, lista2, type", [
    [
        '2, 7, 3.1, banana',
        [2, 'banana', 'carro'],
        TypeError
    ],
    [
        [2, 'banana', 'carro'],
        None,
        TypeError
    ]
])
def test_subtracao_de_listas_exception_type(lista1, lista2, type):
    pytest.raises(type, subtracao_de_listas, (lista1, lista2))
