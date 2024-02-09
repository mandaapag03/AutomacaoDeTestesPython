# calcula o volume de uma caixa retangular

def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura 

# Test 1
print("Doing test 1...")
try:
    response = calcula_volume(comprimento = 1, largura = 1, altura = 1)
    assert response == 1
    print("OK")
except AssertionError:
    print("Error")

# Test 2
print("Doing test 2...")
try:
    response = calcula_volume(comprimento = 2, largura = 4, altura = 3)
    assert response == 24
    print("OK")
except AssertionError:
    print("Error")

# Test 3 
print("Doing test 3...")
try:
    response = calcula_volume(comprimento= 5, largura=5, altura=2)
    assert response == 50
    print("OK")
except AssertionError:
    print("Error")