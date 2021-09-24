from solution import primeiras_ocorrencias

def test_string(self):
    assert primeiras_ocorrencias('abracadabra') == {'a': 0, 'b':1, 'r':2, 'c':4, 'd':6}

def test_string_com_caracter_especial(self):
    assert primeiras_ocorrencias('palavra_teste') == {'p':0, 'a':1, 'l':2, 'v':4, 'r':5, '_':7, 't':8, 'e':9,'s':10}

def test_string_com_letras_maiusculas_e_minusculas (self):
    assert primeiras_ocorrencias('BaNAna') == {'B':0, 'a':1, 'N':2, 'A':3, 'n':4}

def test_string_com_espaco_e_caracteres_repetidos(self):
    assert primeiras_ocorrencias('          teste') == {' ':0, 't': 10, 'e': 11, 's':12}

def test_string_com_caracteres_especiais (self):
    assert primeiras_ocorrencias('#@* -_+&§') == {'#':0, '@':1, '*':2, ' ':3, '-':4, '_':5, '+':6, '&':7, '§':8}

def test_string_vazia (self):
    assert primeiras_ocorrencias('') == {'':0}