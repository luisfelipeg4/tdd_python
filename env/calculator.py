
class Calculator:
  
    def __init__(self):
       self.value = 0
    
    def add(self,a,b):
        self.value = a + b
    
    def minus(self,a,b):
        self.value = a - b

    def division(self,a,b):
        try:
            self.value = a/b
        except ZeroDivisionError:
            self.value=0
        