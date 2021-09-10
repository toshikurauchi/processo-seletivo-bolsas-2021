from typing import Type
from solution import primeiras_ocorrencias
import pytest

class TesteOcorrencias:

    @pytest.mark.parametrize("arg, ans", [
        [
            'abracadabra',
            {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
        ],
        [
            'AaAaBbCdDe',
            {'A': 0, 'a': 1, 'B': 4, 'b': 5, 'C': 6, 'd': 7, 'D': 8, 'e': 9}
        ],
        [
            '.!@#$)(%$#$',
            {'.': 0, '!': 1, '@': 2, '#': 3, '$': 4, ')': 5, '(': 6, '%': 7}
        ],
        [
            'certa vez, eu vi algo de muito longe.',
            {'c': 0, 'e': 1, 'r': 2, 't': 3, 'a': 4, ' ': 5, 'v': 6, 'z': 8, ',': 9,
            'u': 12, 'i': 15, 'l': 18, 'g': 19, 'o': 20, 'd': 22, 'm': 25, 'n': 33,
            '.': 36}
        ]
    ])
    def teste_basico(self, arg, ans):
        assert primeiras_ocorrencias(arg) == ans

    @pytest.mark.parametrize("arg, ans", [
        [
            'abracadabra',
            {'a': 3, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
        ],
        [
            'AaAaBbCdDe',
            {'A': 1, 'a': 2, 'B': 5, 'b': 6, 'C': 7, 'd': 8, 'D': 9, 'e': 10}
        ],
        [
            'certa vez, eu vi algo de muito longe.',
            {'c': 0, 'e': 1, 'r': 2, 't': 3, 'a': 4, ' ': 26, 'v': 6, 'z': 8, ',': 9,
             'u': 12, 'i': 15, 'l': 18, 'g': 19, 'o': 20, 'd': 22, 'm': 25, 'n': 33,
             '.': 36}
        ]
    ])
    def teste_erro(self, arg, ans):
        assert primeiras_ocorrencias(arg) != ans

    @pytest.mark.parametrize("arg, ans", [
        [
            [1, 2, 3, 3, 2, 1],
            {1: 0, 2: 1, 3: 2}
        ],
        [
            (1, 2, 3, 3, 2, 1),
            {1: 0, 2: 1, 3: 2}
        ],
        [
            '',
            {}
        ]
    ])
    def teste_especial(self, arg, ans):
        assert primeiras_ocorrencias(arg) == ans

    @pytest.mark.parametrize("arg, arg2, exception", [
        [
            112359815,
            None,
            TypeError
        ],
        [
            None,
            None,
            TypeError
        ],
        [
            1,
            [1, 2, 3],
            TypeError
        ]
    ])
    def teste_expection(self, arg, arg2, exception):
        if arg2 != None: pytest.raises(TypeError, primeiras_ocorrencias, arg)
        else:            pytest.raises(TypeError, primeiras_ocorrencias, arg, arg2)

def teste_ocorrencias():

    # Casos -> Dicionário que guarda os testes e suas informações.
    # A estrutura foi pensada para que a adição e remoção de testes seja rápida e não exija trabalho.
    # Existem três casos pensados para os testes:
    #   equals --> Caso em que o teste é feito para garantir que o retorno da função seja igual do desejado.
    #   Exige: 
    #       arg ---> Argumento a ser passado para a função.
    #       ans ---> Resposta esperada do retorno da função.
    #
    #   nequals --> Caso em que o teste é feito para garantir que o retorno da função seja diferente do desejado.
    #   Exige: 
    #       arg ---> Argumento a ser passado para a função.
    #       ans ---> Resposta a ser comparada ao retorno da função.
    #
    #   exception --> Caso em que o teste é feito e espera-se que ele reaja com uma exceção.
    #   Exige: 
    #       arg ---> Argumento a ser passado para a função.
    #       exc-type ---> Tipo da exceção esperada da função.

    casos = {
        1: {
            'type': 'equals',
            'arg': 'abracadabra',
            'ans': {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
        },
        2: {
            'type': 'equals',
            'arg': 'AaAaBbCdDe',
            'ans': {'A': 0, 'a': 1, 'B': 4, 'b': 5, 'C': 6, 'd': 7, 'D': 8, 'e': 9}
        },
        3: {
            'type': 'equals',
            'arg': '.!@#$)(%$#$',
            'ans': {'.': 0, '!': 1, '@': 2, '#': 3, '$': 4, ')': 5, '(': 6, '%': 7}
        },
        4: {
            'type': 'equals',
            'arg': 'certa vez, eu vi algo de muito longe.',
            'ans': {'c': 0, 'e': 1, 'r': 2, 't': 3, 'a': 4, ' ': 5, 'v': 6, 'z': 8, ',': 9,
                    'u': 12, 'i': 15, 'l': 18, 'g': 19, 'o': 20, 'd': 22, 'm': 25, 'n': 33,
                     '.': 36}
        },
        5: {
            'type': 'nequals',
            'arg': 'abracadabra',
            'ans': {'a': 3, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
        },
        6: { # Caso onde os indices estao sendo contados com um numero a mais.
            'type': 'nequals',
            'arg': 'AaAaBbCdDe',
            'ans': {'A': 1, 'a': 2, 'B': 5, 'b': 6, 'C': 7, 'd': 8, 'D': 9, 'e': 10}
        },
        7: {
            'type': 'nequals',
            'arg': 'certa vez, eu vi algo de muito longe.',
            'ans': {'c': 0, 'e': 1, 'r': 2, 't': 3, 'a': 4, ' ': 26, 'v': 6, 'z': 8, ',': 9,
                    'u': 12, 'i': 15, 'l': 18, 'g': 19, 'o': 20, 'd': 22, 'm': 25, 'n': 33,
                    '.': 36}
        },
        8: { # Caso onde um inteiro e passado, esperace uma excecao do tipo TypeError
            'type': 'exception',
            'arg': 128175189259043,
            'exc-type': TypeError
        },
        9: { # Caso onde uma lista e passado, espera-se um tratamento sobre? Partirei do pressuposto que não.
            'type': 'equals',
            'arg': [1, 2, 3, 3, 2, 1],
            'ans': {1: 0, 2: 1, 3: 2}
        },
        10: { # Caso simples onde a string de argumento e vazia
            'type': 'equals',
            'arg': '',
            'ans': {}
        },
        11: { # Caso similar a lista, porem com uma tupla
            'type': 'equals',
            'arg': (1, 2, 3, 3, 2, 1),
            'ans': {1: 0, 2: 1, 3: 2}
        },
        12: { # Teste redundante, mas é feito mesmo assim
            'type': 'nequals', 
            'arg': 'AaAaBbCdDe',
            'ans': {'A': 0, 'B': 4, 'C': 6, 'D': 8, 'a': 1, 'b': 5, 'd': 7}
        },
        13: { # Teste sem argumentos
            'type': 'exception',
            'exc-type': TypeError
        },
    }

    # Estrutura que automaticamente faz os testes de acordo com os dados dos casos
    # *** É fácil adicionar novos tipos de testes, um elif resolve o problema ***
    for i in range(1, len(casos)):
        if casos[i]['type'] == 'equals':
            assert (primeiras_ocorrencias(casos[i]['arg']) == casos[i]['ans'])
        elif casos[i]['type'] == 'nequals':
            assert (primeiras_ocorrencias(casos[i]['arg']) != casos[i]['ans'])
        elif casos[i]['type'] == 'exception':
            pytest.raises(casos[i]['exc-type'], primeiras_ocorrencias, casos[i]['arg'])