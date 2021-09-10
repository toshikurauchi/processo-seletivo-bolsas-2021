from solution import primeiras_ocorrencias

def test_dict_keys(entrada):
    # verificar se as chaves retornadas pela função são válidas

    response = primeiras_ocorrencias(entrada)
    assert type(response) == dict                       # verifica se o retorno é um dicionário

    for key in response.keys():
        assert len(key) == 1                            # verifica se a chave não é um único carácter
        assert key.isalpha()                            # verifica se é uma letra

def test_dict_values(entrada):
    # verifica se os valores são válidos
    
    response = primeiras_ocorrencias(entrada)           # não precisamos verificar se o retorno é um dicionário aqui, pois já o fizemos em uma chamada anterior

    for value in response.values():
        assert type(value) == int or type(value) == str 

        if type(value) == str:                          # caso o retorno seja em string
            assert value.isnumeric()                    # verifica se só recebemos números
            assert len(value) < 3 and len(value) > 0    # verifica se o tamanho do retorno é razoável

def solution(palavra):
    ocorrencias = {}

    for i in range(len(palavra)):
        caractere = palavra[i]
        if caractere not in ocorrencias:
            ocorrencias[caractere] = i

    return ocorrencias

def test_correct_answer(entrada):
    # verificamos se a resposta é a esperada

    assert primeiras_ocorrencias(entrada) == solution(entrada)

entrada = 'abracadabra'

test_dict_keys(entrada)        # validamos as chaves
test_dict_values(entrada)      # validamos os valores
test_correct_answer(entrada)   # validamos a resposta