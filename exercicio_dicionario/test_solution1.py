import pytest
from solution import primeiras_ocorrencias

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.

@pytest.mark.parametrize("palavra , dicionario",
[("palavra",{"p":0,"a":1,"l":2,"v":4,"r":5}),
 ("PaLAVra",{"P":0,"a":1,"L":2,"A":3,"V":4,"r":5})
])

def test_func(palavra,dicionario):
    assert primeiras_ocorrencias(palavra) == dicionario
