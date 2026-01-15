class OperacionesAritmeticas:
    def suma(self, sumando1, sumando2):
        if not isinstance(sumando1, (int, float)) or not isinstance(sumando2, (int, float)):
            raise ValueError ("Los sumandos debenser numeros")  
        return sumando1 + sumando2
    def division(self, division1, division2):
        return division1/division2
