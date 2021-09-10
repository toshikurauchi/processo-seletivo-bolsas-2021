import pytest
from solution import primeiras_ocorrencias

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.

# Teste com parametrize misturando letras maísculas com minúsculas
@pytest.mark.parametrize("palavra , dicionario",
[("palavra",{"p":0,"a":1,"l":2,"v":4,"r":5}),
 ("PaLAVra",{"P":0,"a":1,"L":2,"A":3,"V":4,"r":5})
])

def test_func(palavra,dicionario):
    assert primeiras_ocorrencias(palavra) == dicionario

#Teste com palavras Maiores
def test_palavras_maiores():
    palavra = "compartimentalização"
    assert primeiras_ocorrencias(palavra) == {'c': 0, 'o': 1, 'm': 2, 'p': 3, 'a': 4, 'r': 5, 't': 6, 'i': 7, 'e': 9, 'n': 10, 'l': 13, 'z': 15, 'ç': 17, 'ã': 
18}

def test_n_string():
    palavra = 31459
    assert primeiras_ocorrencias(palavra) == "A entrada não foi uma string"
