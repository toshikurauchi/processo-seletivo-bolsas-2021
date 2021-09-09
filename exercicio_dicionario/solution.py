def primeiras_ocorrencias(palavra):
    ocorrencias = {}

    for i in range(len(palavra)):
        caractere = palavra[i]
        if caractere not in ocorrencias:
            ocorrencias[caractere] = i

    return ocorrencias