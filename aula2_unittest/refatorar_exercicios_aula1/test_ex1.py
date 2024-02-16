import unittest
# import aula1_introducao_testes.exercicio_1 as ex1
# import aula1_introducao_testes.exercicio_2 as ex2

def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura 

class TestExercicio1(unittest.TestCase):
    def test1(self):
        self.assertEqual(calcula_volume(comprimento = 1, largura = 1, altura = 1), 1)

    def test2(self):
        self.assertEqual(calcula_volume(comprimento = 2, largura = 4, altura = 3), 24)
    
    def test3(self):
        self.assertEqual(calcula_volume(comprimento= 5, largura=5, altura=2), 50)

if __name__ == '__main__':
    unittest.main()