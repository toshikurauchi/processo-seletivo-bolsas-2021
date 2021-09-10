from solution import primeiras_ocorrencias

try:
    def teste_string_vazia():
        # Verifica a função para strings vazias

        string = ""
        expected = {}
        teste = primeiras_ocorrencias(string)
        assert teste==expected, "Dica: Sua função não parece funcionar para strings vazias."

    def teste_string_inteira():
        # Verifica se a função, com sucesso, determina o índice correto para a última letra, se 
        # essa for sua primeira ocorrência. O Erro comum aqui é talvez o código do aluno não esteja percorrendo
        # a string inteira.

        string = "aaab"
        expected = {"a": 0, "b":len(string)-1}
        teste = primeiras_ocorrencias(string)
        assert teste==expected, "Dica: Verifique se sua função percorre toda a string!"

    def teste_override_primeira():
        # Verifica se a função separa com sucesso a primeira ocorrência da letra,
        # sem trocar com a última ocorrência, erro que pode ser comum

        string = "abba"
        expected = {"a": 0, "b":1}
        teste = primeiras_ocorrencias(string)
        assert teste==expected, "Dica: Cuidado! Parece que sua função está selecionando as últimas ocorrências, e não as primeiras."

    def teste_string_pequena():
        # Verifica função para valores bem pequenos (uma string com apenas 1 caractere)

        string = "a"
        expected = {"a": 0}
        teste = primeiras_ocorrencias(string)
        assert teste==expected, "Dica: Sua função parece estar falhando com entradas bem pequenas. Reveja seu código e tente novamente."

    def teste_string_grande():
        # Verifica função para valores bem grandes

        string = "abababababababababababababababababababcd"
        expected = {"a": 0, "b": 1, "c": len(string)-2, "d": len(string)-1}
        teste = primeiras_ocorrencias(string)
        assert teste==expected, "Dica: Sua função parece estar falhando com entradas bem grandes. Reveja seu código e tente novamente."

    def teste_string_espaco():
        # Verifica função para strings com espaços

        string = "O cachorro"
        expected = {"O": 0, " ": 1, "c": 2, "a": 3, "h": 5, "o": 6, "r": 7}
        teste = primeiras_ocorrencias(string)
        assert teste==expected, "Dica: Preste atenção em strings com espaços. Espaços também contam como caracteres."

except Exception as error:
    print(f"Ops! Ocorreu um erro: \n{error}")