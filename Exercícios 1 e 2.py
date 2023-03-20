class Mago:
    def __init__(self, nome, idade, escola, genero , raca):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.genero = genero
        self.raca = raca
        
    def andar(self):
        print('{} está andando.'.format(self.nome))
    
    def falar(self):
        print('Ola amigue! Meu nome é {}.'.format(self.nome))
        
    def invocarMagia(self):
        print('Invocando magia!')

    def qualRaça(self):
        print('Eu sou {}.'.format(self.raca))

    #Raça num contexto de RPG. (ex: Humano, Elfo, Orc, etc.)

    def boladeFogo(self):
        if self.raca == 'Morto-vivo':
            print('{} lança uma bola de gelo!'.format(self.nome))
        else: 
            print('{} lança uma bola de fogo!'.format(self.nome))

    #Mortos-vivos normalmente são relacionados à magias de gelo.



hp = Mago('Harry Potter', 17, 'Hogwarts','Masculino','Humano')
kt = Mago("Kael'thas Sunstrider", 2800,'Dalaran','Masculino','Elfo Sangrento')
ktz = Mago("Kel'thuzad", 58,'Dalaran','Masculino','Morto-vivo')
md = Mago("Medivh", '??', 'Independente', 'Masculino', 'Humano')


print(hp.nome)
print(hp.idade)
print(hp.escola)
print(hp.genero)
print(hp.raca)

print(kt.nome)
print(kt.idade)
print(kt.escola)
print(kt.genero)
print(kt.raca)

print(ktz.nome)
print(ktz.idade)
print(ktz.escola)
print(ktz.genero)
print(ktz.raca)

print(md.nome)
print(md.idade)
print(md.escola)
print(md.genero)
print(md.raca)

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

md.andar()
md.falar()
md.invocarMagia()
md.qualRaça()
md.boladeFogo()
