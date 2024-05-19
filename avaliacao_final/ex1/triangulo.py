def verifica_triangulo(a,b,c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        return 'Não é um triângulo'
    elif (a == b) and (a == c):
        return 'Equilátero'
    elif (a == b) or (a == c) or (b == c):
        return 'Isósceles'
    else:
        return 'Escaleno'
    