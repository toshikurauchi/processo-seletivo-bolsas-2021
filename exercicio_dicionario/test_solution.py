import pytest
from solution import primeiras_ocorrencias

@pytest.mark.parametrize ("string, resultado", [
    ('abracadabra',{'a': 0, 'b':1, 'r':2, 'c':4, 'd':6}),
    ('palavra_teste',{'p':0, 'a':1, 'l':2, 'v':4, 'r':5, '_':7, 't':8, 'e':9,'s':10}),
    ('BaNAna',{'B':0, 'a':1, 'N':2, 'A':3, 'n':4}),
    ('          teste',{' ':0, 't': 10, 'e': 11, 's':12})
    ('#@* -_+&§',{'#':0, '@':1, '*':2, ' ':3, '-':4, '_':5, '+':6, '&':7, '§':8})
    ('',{})
])

def test_primeiras_ocorrencias (string, resultado):
    assert primeiras_ocorrencias(string) == {resultado} 