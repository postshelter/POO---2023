import math

class figuraGeometrica():
    def calcularArea():
        pass
    
    def calcularPerimetro():
        pass

class Retangulo(figuraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base*self.altura
    
    def calcularPerimetro(self):
        return 2*(self.base + self.altura)

class Triangulo(figuraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self): 
        return (self.base*self.altura)/2
    
    def calcularPerimetro(self): #Triângulo equilátero.
        return self.base*3

class Circulo(figuraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi*self.raio**2
    
    def calcularPerimetro(self):
        return 2*math.pi*self.raio
    
retangulo1 = Retangulo(10, 15)
triangulo1 = Triangulo(10, 15)
circulo1 = Circulo(10)

print(retangulo1.calcularArea())
print(retangulo1.calcularPerimetro())
print(triangulo1.calcularArea())
print(triangulo1.calcularPerimetro())
print(circulo1.calcularArea())
print(circulo1.calcularPerimetro())
    
