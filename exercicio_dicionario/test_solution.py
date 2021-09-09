from solution import primeiras_ocorrencias
# coding: utf-8

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
def test_primeiras_ocorrencias():
  assert primeiras_ocorrencias('abracadabra') == {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
  assert primeiras_ocorrencias('banana') == {'b': 0, 'a': 1, 'n': 2}
  assert primeiras_ocorrencias('aaaaaaa')  == {'a': 0}
  assert primeiras_ocorrencias('aaaaaaA') == { 'a': 0, 'A': 6 }
  assert primeiras_ocorrencias('     a') == { ' ': 0, 'a': 5 }
  assert primeiras_ocorrencias('Ola%20Tudo%20Bem?') == {'O': 0, 'l': 1, 'a': 2, '%': 3, '2': 4, '0': 5, 'T': 6, 'u': 7, 'd': 8, 'o': 9, 'B': 13, 'e': 14, 'm': 15, '?': 16}