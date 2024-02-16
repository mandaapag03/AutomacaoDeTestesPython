import unittest

def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius

def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit 

class TestExercicio2(unittest.TestCase):
    def test1(self):
        self.assertEqual(converte_para_fahrenheit(celsius=0), 32.0)

    def test2(self):
        self.assertEqual(converte_para_fahrenheit(celsius=27), 80.6)

    def test3(self):
        self.assertEqual(converte_para_celsius(fahrenheit=32), 0)

    def test4(self):
        self.assertEqual(converte_para_celsius(fahrenheit=41), 5.0)
        