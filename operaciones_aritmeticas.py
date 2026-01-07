class operacionesAritmeticas:
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar_dos_numeros(self):
        return self.numero1 + self.numero2

    def restar_dos_numeros(self):
        return self.numero1 - self.numero2

    def multiplicar_dos_numeros(self):
        return self.numero1 * self.numero2

    def dividir_dos_numeros(self):
        if self.numero2 == 0:
            return "Error: División por cero"
        return self.numero1 / self.numero2



