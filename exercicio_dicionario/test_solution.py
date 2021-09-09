from solution import primeiras_ocorrencias
class TestExercicioDicionario():
    # Teste do exemplo do exercício
    def test_exemplo(self):
        string_test = 'abracadabra'
        response = primeiras_ocorrencias(string_test)
        expected = {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
        assert response == expected

    # Teste para uma string com caracteres únicos
    def test_ocorrencias_unicas(self):
        string_test = 'abcdef'
        response = primeiras_ocorrencias(string_test)
        expected = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
        assert response == expected

    # Teste para uma string com um caractere
    def test_um_caractere(self):
        string_test = 'u'
        response = primeiras_ocorrencias(string_test)
        expected = {'u':0}
        assert response == expected
    
    # Teste para string vazia
    def test_string_vazia(self):
        string_test = ''
        response = primeiras_ocorrencias(string_test)
        expected = {}
        assert response == expected

    # Teste para string com um único caractere
    def test_unico_caractere(self):
        string_test = 'cccccccc'
        response = primeiras_ocorrencias(string_test)
        expected = {'c':0}
        assert response == expected

    # Teste para caracteres especiais e números
    def test_caracteres_esquisitos(self):
        string_test = 'h2hh?3h'
        response = primeiras_ocorrencias(string_test)
        expected = {'h':0,'2':1,'?':4,'3':5}
        assert response == expected
