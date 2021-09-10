from solution import subtracao_de_listas

def solution(lista1, lista2):
    resposta = []

    for elemento in lista1:
        if elemento not in lista2:
            resposta.append(elemento)

    return resposta

def test_return_types(input1, input2):
    # verifica se o tipo de retorno da resposta é o esperado

    response = subtracao_de_listas(input1, input2)

    assert type(response) == list       # verifica se recebemos uma lista
    assert len(response) > 0            # verifica se a lista não esta vazia

def test_correct_answer(input1, input2):
    # verifica se a resposta esta correta

    response = subtracao_de_listas(input1, input2)
    
    assert response == solution(input1, input2)

input1 = [2, 7, 3.1, 'banana']; input2 = [2, 'banana', 'carro']

test_return_types(input1, input2)       # validamos o tipo de retorno da resposta
test_correct_answer(input1, input2)     # verificamos se a resposta esta correta