# Importando as bibliotecas e arquivos necessários
import pytest
import six
from solution import primeiras_ocorrencias

# ------------------------------------------------------------------------

# Definindos as fixtures dos nossos testes 
# (ainda não sei se nesse caso irá ajudar muito, mas foi legal aprender para implementar em casos mais complexos) 

@pytest.fixture
def palavra_nula():
    return ''

# ------------------------------------------------------------------------

# Realizando os testes para diversos cenários

# Testando solução com uma palavra curta + pytest.mark.parametrize
@pytest.mark.parametrize('palavra_curta, saida_curta', [('olá', {'o': 0, 'l': 1, 'á': 2}), ('como', {'c': 0, 'o': 1, 'm': 2}), ('vai', {'v': 0, 'a': 1, 'i': 2})])
def test_primeiras_ocorrencias_palavra_curta(palavra_curta, saida_curta):
    assert primeiras_ocorrencias(palavra_curta) == saida_curta 

# Testando solução com uma palavra muito grande + pytest.mark.parametrize
@pytest.mark.parametrize('palavra_grande, saida_grande', [('pneumoultramicroscopicossilicovulcanoconiótico', {'p': 0, 'n': 1, 'e': 2, 'u': 3, 'm': 4, 'o': 5, 'l': 7, 't': 8, 'r': 9, 'a': 10, 'i': 12, 'c': 13, 's': 16, 'v': 30, 'ó': 41}),  ('antoniamartinsrodriguesdasilvajunior', {'a': 0, 'n': 1, 't': 2, 'o': 3, 'i': 5, 'm': 7, 'r': 9, 's': 13, 'd': 16, 'g': 19, 'u': 20, 'e': 21, 'l': 27, 'v': 28, 'j': 30}), ('testeissoehumtestetabelezanice', {'t': 0, 'e': 1, 's': 2, 'i': 5, 'o': 8, 'h': 10, 'u': 11, 'm': 12, 'a': 19, 'b': 20, 'l': 22, 'z': 24, 'n': 26, 'c': 28})])
def test_primeiras_ocorrencias_palavra_grande(palavra_grande, saida_grande):
    assert primeiras_ocorrencias(palavra_grande) == saida_grande

# Testando solução com uma frase aleatória + pytest.mark.parametrize
@pytest.mark.parametrize('frase, saida_frase', [('Olá, como vai?', {'O': 0, 'l': 1, 'á': 2, ',': 3, ' ': 4, 'c': 5, 'o': 6, 'm': 7, 'v': 10, 'a': 11, 'i': 12, '?': 13}), ('Eu vou indo, e você, tudo bem?', {'E': 0, 'u': 1, ' ': 2, 'v': 3, 'o': 4, 'i': 7, 'n': 8, 'd': 9, ',': 11, 'e': 13, 'c': 17, 'ê': 18, 't': 21, 'b': 26, 'm': 28, '?': 29}), ('Tudo bem, eu vou indo correndo', {'T': 0, 'u': 1, 'd': 2, 'o': 3, ' ': 4, 'b': 5, 'e': 6, 'm': 7, ',': 8, 'v': 13, 'i': 17, 'n': 18, 'c': 22, 'r': 24})])
def test_primeiras_ocorrencias_frase(frase, saida_frase):
    assert primeiras_ocorrencias(frase) == saida_frase
        
# Testando solução nula + fixtures
def test_primeiras_ocorrencias_nulo(palavra_nula):
    assert primeiras_ocorrencias(palavra_nula) == {}, "O valor inserido está sendo reconhecido como nulo"