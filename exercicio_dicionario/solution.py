def primeiras_ocorrencias(palavra):
    if type(palavra) == str:
        ocorrencias = {}

        for i in range(len(palavra)):
            caractere = palavra[i]
            if caractere not in ocorrencias:
                ocorrencias[caractere] = i

        return ocorrencias
    else:
        return "A entrada não foi uma string"
    
    

