# Unit_test/code/calculations.py

class Calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def get_sum(self):
        return self.a + self.b
    
    def get_difference(self):
        return self.a - self.b
    
    def get_product(self):
        return self.a * self.b
    
    def get_quotient(self):
        if self.b != 0:
            return self.a / self.b
        return None