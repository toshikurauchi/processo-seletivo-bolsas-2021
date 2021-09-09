from solution import primeiras_ocorrencias


# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
def test_string_vazia():
    assert primeiras_ocorrencias('') == dict()


def test_zebra():
    assert primeiras_ocorrencias('zebra') == {'z': 0, 'e': 1, 'b': 2, 'r': 3, 'a': 4}


def test_abracadabra():
    assert primeiras_ocorrencias('abracadabra') == {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}


def test_iiiiiiiiiiiiiiiiiha():
    assert primeiras_ocorrencias('iiiiiiiiiiiiiiiiiha') == {'i': 0, 'h': 17, 'a': 18}