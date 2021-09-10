from typing import Type
import pytest

from solution import primeiras_ocorrencias

# testes relativos a acertos


@pytest.mark.parametrize("string, result", [
    [
        'banana',
        {'b': 0, 'a': 1, 'n': 2}
    ],
    [
        'lorem ipsum lorem',
        {'l': 0, 'o': 1, 'r': 2, 'e': 3, 'm': 4,
            ' ': 5, 'i': 6, 'p': 7, 's': 8, 'u': 9}
    ],
    [
        '',
        {}
    ]
])
def test_primeiras_ocorrencias_equal_type(string, result):
    assert primeiras_ocorrencias(string) == result

# testes relativos a erros


@pytest.mark.parametrize("string, result", [
    [
        'banana',
        {'b': 0, 'a': 5, 'n': 4}
    ]
])
def test_primeiras_ocorrencias_nequal_type(string, result):
    assert primeiras_ocorrencias(string) != result

# testes relativos a exceções


@pytest.mark.parametrize("string", [
    [
        ['banana']
    ],
    [
        ['b', 'a', 'n', 'a', 'n', 'a']
    ]
])
def test_primeiras_ocorrencias_type_error(string):
    pytest.raises(TypeError, primeiras_ocorrencias, string)
