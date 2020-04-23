import unittest  
from calculator import Calculator

class TestMyCalculator(unittest.TestCase):  
  
    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    def test_sum(self):
        self.calc.add(1, 3) 

        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)
    
    def test_minus(self):
        self.calc.minus(5, 3)  
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)
    
    def test_sum_fail(self):
        try:
            self.calc.add(1, 's') 
        except Exception as e:
            self.assertEqual(str(e),"unsupported operand type(s) for +: 'int' and 'str'")

    def test_sum_fail_list(self):
        try:
            self.calc.add(1, ['s','a']) 
        except Exception as e:
            self.assertEqual(str(e),"unsupported operand type(s) for +: 'int' and 'list'" )
    
    def test_div(self):
        self.calc.division(6, 3)  
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)
    
    def test_div_fail(self):
        self.calc.division(6,0) 
        self.assertEqual(0, self.calc.value)

    def test_div_fail_list(self):
        try:
            self.calc.division(1, 's') 
        except Exception as e:
            self.assertEqual(str(e),"unsupported operand type(s) for /: 'int' and 'str'" )
        
        