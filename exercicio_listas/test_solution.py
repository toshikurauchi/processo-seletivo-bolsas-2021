from solution import subtracao_de_listas


# Escreva seus testes neste arquivo. Para ajudar já importamos a função.


# teste com listas vazias
# com uma lista vazia
# com elementos repetidos

# teste com listas l1 e l2 vazias
def test_l1_l2_vazia():
    assert subtracao_de_listas([],[]) == []

# teste com a lista l1 vazia e l2 cheia
def test_l1_vazia():
    assert subtracao_de_listas([],[1,2,'batman']) == []

# teste com a lista l1 cheia e l2 vazia
def test_l2_vazia():
    assert subtracao_de_listas([3,4,5,'flash','superman'],[]) == [3,4,5,'flash','superman']

# teste com a lista l1 com elementos repetidos e l2 sem elementos iguais
def test_l1_repetida():
    assert subtracao_de_listas(['coringa', 'coringa', 'coringa'],[1,2,3]) == ['coringa']

# teste com a lista l1 com múltiplos elementos e l2 com elementos repetidos
def test_l2_repetida():
    assert subtracao_de_listas(['batman', 'beyond', '#', '1' ],['arrow', 'green', 'arrow', 'green']) == ['batman', 'beyond', '#', '1' ]

# teste com a lista l1 e l2 muito grandes e com valores repetidos
def test_l1_l2_grande():
    assert subtracao_de_listas(['batatman', 6,7,899999,85069,456806,'ahdsdaofew','jauispaliasdfrs','batatman', 6,7,899999,85069,456806,'ahdsdaofew','jauispaliasdfrs','batatman', 6,7,899999,85069,456806,'ahdsdaofew','jauispaliasdfrs','batatman', 6,7,899999,85069,456806,'ahdsdaofew','jauispaliasdfrs'],['bizarro', 'green', 'arrow', 'green','batatman', 6,7,899999,85069,456806,'ahdsdaofew','jauispaliasdfrs','batatman', 6,7,899999,85069,456806,'ahdsdaofew','jauispaliasdfrs']) == []