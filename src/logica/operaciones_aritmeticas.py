class OperacionesAritmeticas:
    def suma(self, sumando1, sumando2):
        if not isinstance(sumando1, (int, float)) or not isinstance(sumando2, (int, float)):
            raise TypeError ("Los sumandos deben ser numeros")  
        return sumando1 + sumando2
    
    def division(self, division1, division2):
        if not isinstance(division1, (int, float)) or not isinstance(division2, (int, float)):
            raise TypeError ("Los divisores deben ser numeros")  
        
        if division2 == 0:
            raise ZeroDivisionError
        
        return division1/division2
