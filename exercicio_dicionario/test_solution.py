from solution import primeiras_ocorrencias

class TestClass:
    def test_type(self):
        x="Hello World"
        dic=primeiras_ocorrencias(x)
        typ=isinstance(dic,dict)
        assert typ==True

    def test_valuesTypes(self):
        x = "quantidade"
        dic=primeiras_ocorrencias(x)
        inteiro=True
        for v in dic.values():
            if not isinstance(v,int):
                inteiro=False
                break
        assert inteiro==True

    def test_ascendingValues(self):
        x = "abcdefghijklmnooooonm"
        dic=primeiras_ocorrencias(x)
        assert list(dic.values())==sorted(dic.values())

    def test_uniqueKeys(self):
        x = "bananananananas"
        dic=primeiras_ocorrencias(x)
        unico=True
        keys=[]
        for k in dic.keys():
            if k in keys:
                unico=False
                break
            else:
                keys.append(k)
        assert unico==True

    def test_initial(self):
        x = "abcabcd"
        dic=primeiras_ocorrencias(x)
        sol={'a': 0, 'b': 1, 'c': 2, 'd': 6}
        assert dic==sol
    
    def test_lowerWord(self):
        x = "batata"
        dic=primeiras_ocorrencias(x)
        sol={'b': 0, 'a': 1, 't': 2}
        assert dic==sol

    def test_higherWord(self):
        x = "aBóbOrA"
        dic=primeiras_ocorrencias(x)
        sol={'a': 0, 'B': 1, 'ó': 2, 'b': 3, 'O': 4, 'r': 5, 'A': 6}
        assert dic==sol

    def test_specialChars(self):
        x = "$$@@macarrãoÀ@@$$"
        dic=primeiras_ocorrencias(x)
        sol={'$': 0, '@': 2, 'm': 4, 'a': 5, 'c': 6, 'r': 8, 'ã': 10, 'o': 11, 'À': 12}
        assert dic==sol
        
    def test_numericEntry(self):
        x = "01233210"
        dic=primeiras_ocorrencias(x)
        sol={'0': 0, '1': 1, '2': 2, '3': 3}
        assert dic==sol
    


# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
