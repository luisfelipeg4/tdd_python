
class Calculator:
  
    def __init__(self):
       self.value = 0
    
    def add(self,a,b):
        self.value = a + b
    def minus(self,a,b):
        self.value = a - b
    def div(self,a,b):
        self.value = a / b
    def mul(self,a,b):
        self.value = a * b
    def mod(self,a,b):
        self.value = a % b