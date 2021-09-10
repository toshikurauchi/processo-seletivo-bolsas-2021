from solution import primeiras_ocorrencias

class TestClass:
    def testTypes(self):
        x = "quantidade"
        dic = primeiras_ocorrencias(x)
        assert isinstance(dic, dict)
        for v in dic.values():
            assert isinstance(v, int)

    def testBlankEntry(self):
        x=""
        dic = primeiras_ocorrencias(x)
        sol={}
        assert dic==sol

    def testInitial(self):
        x = "abcabcd"
        dic=primeiras_ocorrencias(x)
        sol={'a': 0, 'b': 1, 'c': 2, 'd': 6}
        assert dic==sol
    
    def testLowerWord(self):
        x = "batata"
        dic=primeiras_ocorrencias(x)
        sol={'b': 0, 'a': 1, 't': 2}
        assert dic==sol

    def testHigherWord(self):
        x = "aBóbOrA"
        dic=primeiras_ocorrencias(x)
        sol={'a': 0, 'B': 1, 'ó': 2, 'b': 3, 'O': 4, 'r': 5, 'A': 6}
        assert dic==sol

    def testSpecialChars(self):
        x = "$$@@macarrãoÀ@@$$"
        dic=primeiras_ocorrencias(x)
        sol={'$': 0, '@': 2, 'm': 4, 'a': 5, 'c': 6, 'r': 8, 'ã': 10, 'o': 11, 'À': 12}
        assert dic==sol
        
    def testNumericEntry(self):
        x = "01233210"
        dic=primeiras_ocorrencias(x)
        sol={'0': 0, '1': 1, '2': 2, '3': 3}
        assert dic==sol
    


# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
