import pytest
from triangulo import verifica_triangulo

def test_nao_triangulo():
    a = 1
    b = 1
    c = 12 
    assert verifica_triangulo(a, b, c) == 'Não é um triângulo'

def test_triangulo_equilatero():
    a = 12
    b = 12
    c = 12 
    assert verifica_triangulo(a, b, c) == 'Equilátero'

def test_triangulo_isosceles():
    a = 5
    b = 5
    c = 3
    assert verifica_triangulo(a, b, c) == 'Isósceles'

def test_triangulo_escaleno():
    a = 4
    b = 5
    c = 6 
    assert verifica_triangulo(a, b, c) == 'Escaleno'