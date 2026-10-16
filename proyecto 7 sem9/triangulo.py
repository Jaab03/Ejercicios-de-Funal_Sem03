class triangulo:

    def __init__(self):
        
        self.baase = float(input("\nIngresa la base del triángulo: ")) 
        self.altura = float(input("Ingresa la altua del triángulo: "))
        self.lado = float(input("Ingresa el lado del triángulo: "))
       
    def area(self):

        return self.baase * self.altura / 2

    def perimetro(self):

        return self.baase + self.lado