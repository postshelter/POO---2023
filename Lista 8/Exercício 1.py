import random


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def exibirDescricao(self):
        print('O nome do animal é {}'.format(self.nome))

    
class Carnivoro(Animal):
    def caçar(self):
        print('{} sai para caçar.'.format(self.nome))

    def exibirDescricao(self):
        super().exibirDescricao()
        print('{} é um animal carnívoro.'.format(self.nome))


class Herbivoro(Animal):
    def pastar(self):
        print('{} sai para pastar.'.format(self.nome))

    def exibirDescricao(self):
        super().exibirDescricao()
        print('{} é um animal herbívoro.'.format(self.nome))


class Onivoro(Carnivoro,Herbivoro,Animal):
    def comer(self):
        sorteio = random.randint(0,1)
        if sorteio == 0:
            super().caçar()
        else:
            super().pastar()

    def exibirDescricao(self):
        Animal.exibirDescricao(self)
        print('{} é um animal onívoro.'.format(self.nome))

aguia = Carnivoro('Águia')
zebra = Herbivoro('Zebra')
urso = Onivoro('Urso')

aguia.caçar()
aguia.exibirDescricao()
zebra.pastar()
zebra.exibirDescricao()
urso.comer()
urso.exibirDescricao()
