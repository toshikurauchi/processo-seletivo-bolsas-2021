from solution import subtracao_de_listas
import pytest

@pytest.mark.parametrize("test_input,expected", 
                         [(([1,2,3,4,5],[4,5,6,7,8]),[1,2,3]), 
                          (([1,2,3,4,5],[4,5,6,7,8])),[1,2,3,5]), 
                          ((['Ovelha','maca', 81, 8.1], ['Oitenta e um',8.1, 81]), ['Ovelha','maca']),
                          ((['Ovelha','maca', 81, 8.1], ['Oitenta e um',8.1, 81]), ['Ovelha','maca',81]),
                          ((['mano','mana','boy','girl'],['mano','boy']), ['mana','girl']),
                          ((['mano','mana','boy','girl'],['mana','girl']), ['mano','boy']),
                          ((['mano','mana','boy','girl'],['mano','boy']),['mano','mana']))

                          
def test_subtracao_de_listas1(test_input, expected):
  assert subtracao_de_listas(test_input) == expected

# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
