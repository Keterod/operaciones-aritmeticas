
class operacionesAritmeticas:
    def __int__(self, numero1=0, numero2=0):
        self.numero1= numero1
        self.nuemro2= numero2

    def sumar_dos_numeros(self):
        return self.numero1 +self.numero2
    
if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))

operaciones= operacionesAritmeticas(numero1, numero2)

print("La suma es:", operaciones.sumar_dos_numeros())




