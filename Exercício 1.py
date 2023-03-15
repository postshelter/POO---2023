class Mago:
    def __init__(self, nome, idade, escola, gênero , raça):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.gênero = gênero
        self.raça = raça
        
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def qualRaça(self):
        print('Eu sou {}.'.format(self.raça))

    def boladeFogo(self):
        print('{} lança uma bola de fogo!'.format(self.nome))    
        
        

hp = Mago('Harry Potter', 17, 'Hogwarts','Masculino','Humano')
kt = Mago('Kaelthas Sunstrider', 'boa pergunta','Dalaran','Masculino','Elfo Sangrento')
ktz = Mago('Kelthuzad','bastante','Dalaran','Masculino','Morto-vivo')

print(hp.nome)
print(hp.idade)
print(hp.escola)
print(hp.gênero)
print(hp.raça)

print(kt.nome)
print(kt.idade)
print(kt.escola)
print(kt.gênero)
print(kt.raça)

print(ktz.nome)
print(ktz.idade)
print(ktz.escola)
print(ktz.gênero)
print(ktz.raça)

hp.andar()
hp.falar()
hp.invocarMagia()
hp.qualRaça()
hp.boladeFogo()

kt.andar()
kt.falar()
kt.invocarMagia()
kt.qualRaça()
kt.boladeFogo()

ktz.andar()
ktz.falar()
ktz.invocarMagia()
ktz.qualRaça()
ktz.boladeFogo()