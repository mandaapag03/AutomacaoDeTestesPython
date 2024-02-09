def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius

def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit 

# converte_para_fahrenheit
# Test 1
print("converte_para_fahrenheit")
print("Doing test 1...")
try:
    response = converte_para_fahrenheit(celsius=0)
    assert response == 32.0
    print("OK")
except AssertionError:
    print("Error")

# Test 2
print("Doing test 2...")
try:
    response = converte_para_fahrenheit(celsius=27)
    assert response == 80.6
    print("OK")
except AssertionError:
    print("Error")

#converte_para_celsius
# Test 1
print("converte_para_celsius")
print("Doing test 1...")
try:
    response = converte_para_celsius(fahrenheit=32)
    assert response == 0
    print("OK")
except AssertionError:
    print("Error")

# Test 2
print("Doing test 2...")
try:
    response = converte_para_celsius(fahrenheit=41)
    assert response == 5.0
    print("OK")
except AssertionError:
    print("Error")