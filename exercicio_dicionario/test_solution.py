from solution import primeiras_ocorrencias

try:
    def teste1():
        # Verifica se a função, com sucesso, determina o índice correto para a última letra, se 
        # essa for sua primeira ocorrência. O Erro comum aqui é talvez o código do aluno não esteja percorrendo
        # a string inteira.

        string = "aaab"
        expected = {"a": 0, "b":len(string)-1}
        teste = primeiras_ocorrencias(string)
        print("\nDica:")
        print("Verifique se sua função percorre toda a string!\n")
        assert teste==expected

    def teste2():
        # Verifica se a função separa com sucesso a primeira ocorrência da letra,
        # sem trocar com a última ocorrência, erro que pode ser comum

        string = "abba"
        expected = {"a": 0, "b":1}
        teste = primeiras_ocorrencias(string)
        print("\nDica:")
        print("Cuidado! Parece que sua função está selecionando as últimas ocorrências, e não as primeiras.\n")
        assert teste==expected

    def teste3():
        # Verifica função para valores bem pequenos (uma string com apenas 1 caractere)

        string = "a"
        expected = {"a": 0}
        teste = primeiras_ocorrencias(string)
        print("\nDica:")
        print("Sua função parece estar falhando com entradas bem pequenas. Reveja seu código e tente novamente\n")
        assert teste==expected

    def teste4():
        # Verifica função para valores bem grandes

        string = "abababababababababababababababababababcd"
        expected = {"a": 0, "b": 1, "c": len(string)-2, "d": len(string)-1}
        teste = primeiras_ocorrencias(string)
        print("\nDica:")
        print("Sua função parece estar falhando com entradas bem grandes. Reveja seu código e tente novamente\n")
        assert teste==expected

    def teste5():
        # Verifica função para strings com espaços

        string = "O cachorro"
        expected = {"O": 0, " ": 1, "c": 2, "a": 3, "h": 5, "o": 6, "r": 7}
        teste = primeiras_ocorrencias(string)
        print("\nDica:")
        print("Preste atenção em strings com espaços. Espaços também contam como caracteres\n")
        assert teste==expected

except Exception as error:
    print(f"Ops! Ocorreu um erro: \n{error}")