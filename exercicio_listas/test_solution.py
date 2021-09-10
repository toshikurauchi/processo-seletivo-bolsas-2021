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


@pytest.mark.parametrize("lista1, lista2", [
    [
        '2, 7, 3.1, banana',
        [2, 'banana', 'carro']
    ],
    [
        [2, 'banana', 'carro'],
        None
    ],
    [
        None,
        None
    ]
])
def test_subtracao_de_listas_type_error(lista1, lista2):
    if(lista2 is None):
        # simulando caso em que não é passado um ou os dois argumentos

        if(lista1 is None):
            pytest.raises(TypeError, subtracao_de_listas)
        else:
            pytest.raises(TypeError, subtracao_de_listas, lista1)
    else:
        pytest.raises(TypeError, subtracao_de_listas, (lista1, lista2))
