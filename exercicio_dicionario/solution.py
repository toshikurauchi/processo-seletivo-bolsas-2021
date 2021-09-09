def primeiras_ocorrencias(palavra):
    try: 
        ocorrencias = {}

        for i in range(len(palavra)):
            caractere = palavra[i]
            if caractere not in ocorrencias:
                ocorrencias[caractere] = i
                
        return ocorrencias

    except:
        return None

palavra = 214432423
print(primeiras_ocorrencias(palavra))