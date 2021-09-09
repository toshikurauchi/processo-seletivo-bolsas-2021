def primeiras_ocorrencias(palavra):
    ocorrencias = {}

    for i in range(len(palavra)):
        caractere = palavra[i]
        
        if caractere not in ocorrencias:
            ocorrencias[caractere] = i
        # ocorrencias[caractere] = i
    return ocorrencias


print(primeiras_ocorrencias('abracadabra'))
print(primeiras_ocorrencias('y'))
print(primeiras_ocorrencias('testando mais de uma palavra'))
print(primeiras_ocorrencias('ola, mundo!'))
print(primeiras_ocorrencias('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaabgtfr'))