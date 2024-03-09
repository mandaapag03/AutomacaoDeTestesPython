from src.bhaskara import Bhaskara
from pytest import mark

@mark.parametrize("a, b, c, qtd_raizes", [
    (10, 10, 10, 0),
])
def test_bhaskara_zero_raizes(bhaskara, a, b, c, qtd_raizes):
    assert bhaskara.calcular_raizes(a, b, c) == qtd_raizes

@mark.parametrize("a, b, c, qtd_raizes , raiz1", [
    (1, 0, 0, 1, 0),
    (10, 20, 10, 1, -1)
])
def test_bhaskara_uma_raiz(bhaskara, a, b, c, qtd_raizes , raiz1):
    assert bhaskara.calcular_raizes(a, b, c) == (qtd_raizes, raiz1)

@mark.parametrize("a, b, c, qtd_raizes , raiz1, raiz2", [
    (1, -5, 6, 2, 3, -2),
])
def test_bhaskara_duas_raizes(bhaskara, a, b, c, qtd_raizes , raiz1, raiz2):
    assert bhaskara.calcular_raizes(a, b, c) == (qtd_raizes, raiz1, raiz2)
