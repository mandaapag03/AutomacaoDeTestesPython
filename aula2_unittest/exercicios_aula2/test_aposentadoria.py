import unittest, aposentadoria

class Tests_Aposentadoria(unittest.TestCase):
    def test_exception_invalid_idade_value(self):
        self.assertRaises(
            ValueError, 
            aposentadoria.verificar_qualificacao_empregado,
            0, 10)
        
    def test_exception_invalid_tempo_de_servico_value(self):
        self.assertRaises(
            ValueError, 
            aposentadoria.verificar_qualificacao_empregado,
            20, 0)
        
    def test_exception_invalid_idade_type(self):
        self.assertRaises(
            TypeError, 
            aposentadoria.verificar_qualificacao_empregado,
            '65', 30)
        
    def test_exception_invalid_tempo_de_servico_type(self):
        self.assertRaises(
            TypeError, 
            aposentadoria.verificar_qualificacao_empregado,
            65, '30')
        
    def test_input_ok_1(self):
        self.assertEqual(
            aposentadoria.verificar_qualificacao_empregado(65, 20),
            aposentadoria.REQUERER)
        
    def test_input_ok_2(self):
        self.assertEqual(
            aposentadoria.verificar_qualificacao_empregado(59, 30),
            aposentadoria.REQUERER)
        
    def test_input_ok_3(self):
        self.assertEqual(
            aposentadoria.verificar_qualificacao_empregado(60, 25),
            aposentadoria.REQUERER)
        
    def test_input_not_ok_1(self):
        self.assertEqual(
            aposentadoria.verificar_qualificacao_empregado(59, 24),
            aposentadoria.NAO_REQUERER)
        
if __name__ == '__main__':
    unittest.main()
