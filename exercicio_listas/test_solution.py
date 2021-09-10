from solution import subtracao_de_listas

def correct_answer(lista1, lista2):
    resposta = []

    for elemento in lista1:
        if elemento not in lista2:
            resposta.append(elemento)

    return resposta

def test_return_types():
    # verifica se o tipo de retorno da resposta é o esperado

    entrada1 = [2, 7, 3.1, 'banana']; entrada2 = [2, 'banana', 'carro']
    response = subtracao_de_listas(entrada1, entrada2)

    assert type(response) == list       # verifica se recebemos uma lista
    assert len(response) > 0            # verifica se a lista não esta vazia

def test_correct_answer():
    # verifica se a resposta esta correta

    entrada1 = [2, 7, 3.1, 'banana']; entrada2 = [2, 'banana', 'carro']
    response = subtracao_de_listas(entrada1, entrada2)
    
    assert response == correct_answer(entrada1, entrada2)