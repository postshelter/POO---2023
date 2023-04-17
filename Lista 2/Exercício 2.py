class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        

    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2
    
    def multiplicacao(self):
        return self.num1 * self.num2
    
    def divisao (self):
        if self.num1 == 0 or self.num2 == 0:
            print('Erro: divisão por zero.')
            return -1
        else:
            return self.num1 / self.num2
    
calc1 = Calculadora(10,2)
calcerro = Calculadora(10,0)


print (calc1.soma())
print (calc1.subtracao())
print (calc1.multiplicacao())
print (calc1.divisao())

print (calcerro.soma())
print (calcerro.subtracao())
print (calcerro.multiplicacao())
print (calcerro.divisao())

