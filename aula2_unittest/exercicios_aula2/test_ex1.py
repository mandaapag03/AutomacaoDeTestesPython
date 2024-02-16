import unittest
import ex1

class TestEx1(unittest.TestCase):
    def test_exception_value_error_1(self):
        self.assertRaises(ValueError, ex1.avaliar_notas, -1, 0, 0, 0)
    
    def test_exception_value_error_2(self):
        self.assertRaises(ValueError, ex1.avaliar_notas, 0, -1, 0, 0)
    
    def test_exception_value_error_3(self):
        self.assertRaises(ValueError, ex1.avaliar_notas, 0, 0, -1, 0)
    
    def test_exception_equals_1(self):
        self.assertEqual(ex1.avaliar_notas(10,10,10,10), 'A')
    
    def test_exception_equals_3(self):
        self.assertEqual(ex1.avaliar_notas(9,9,9,9), 'A')
    
    def test_exception_equals_4(self):
        self.assertEqual(ex1.avaliar_notas(8.9,8.9,8.9,8.9), 'B')
    
    def test_exception_equals_5(self):
        self.assertEqual(ex1.avaliar_notas(7.5,7.5,7.5,7.5), 'B')
    
    def test_exception_equals_6(self):
        self.assertEqual(ex1.avaliar_notas(7.4,7.4,7.4,7.4), 'C')
    
    def test_exception_equals_7(self):
        self.assertEqual(ex1.avaliar_notas(6.0,6.0,6.0,6.0), 'C')
    
    def test_exception_equals_8(self):
        self.assertEqual(ex1.avaliar_notas(5.9,5.9,5.9,5.9), 'D')
    
    def test_exception_equals_9(self):
        self.assertEqual(ex1.avaliar_notas(0.0,0.0,0.0,0.0), 'D')

if __name__ == '__main__':
    unittest.main()