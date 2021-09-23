from solution import subtracao_de_listas
import pytest

def test_subtracao_de_listas1():
  assert subtracao_de_listas([1,2,3,4,5],[4,5,6,7,8]) == [1,2,3]
def test_subtracao_de_listas2():
  assert subtracao_de_listas([1,2,3,4,5],[4,5,6,7,8]) == [1,2,3,5]
def test_subtracao_de_listas3():
  assert subtracao_de_listas(['Ovelha','maca', 81, 8.1], ['Oitenta e um',8.1, 81]) == ['Ovelha','maca']
def test_subtracao_de_listas4():
  assert subtracao_de_listas(['Ovelha','maca', 81, 8.1], ['Oitenta e um',8.1, 81]) == ['Ovelha','maca',81]
def test_subtracao_de_listas5():
  assert subtracao_de_listas(['mano','mana','boy','girl'],['mano','boy']) == ['mana','girl']
def test_subtracao_de_listas6():
  assert subtracao_de_listas(['mano','mana','boy','girl'],['mana','girl']) == ['mano','boy']
def test_subtracao_de_listas7():
  assert subtracao_de_listas(['mano','mana','boy','girl'],['mano','boy']) == ['mano','mana']
# Escreva seus testes neste arquivo. Para ajudar já importamos a função.
