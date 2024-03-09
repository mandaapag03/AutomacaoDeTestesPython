import pytest
from src.cubo import cubo

@pytest.mark.parametrize("numero, numero_ao_cubo", [
    (0, 0),
    (1, 1),
    (2, 8),
    (-2, -8),
    (10, 1000)
])
def test_input_cubo_do_numero(numero, numero_ao_cubo):
    assert cubo(numero) == numero_ao_cubo