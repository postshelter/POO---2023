import random
win = 0

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0

    def atualizar(self):
        movimento = random.randint(1,6)
        #print ('{} tirou {}.'.format(self.nome, movimento)) Usei durante o desenvolvimento para ver se as jogadas estavam tendo os efeitos corretos.
        self.pos+= movimento
        if self.pos % 5 == 0 :
            self.pos-= 1
            return self.pos
        elif self.pos == 7 or self.pos == 17:
            self.pos+=2
            return self.pos
        elif self.pos == 13:
            self.pos = 0
            return self.pos
        else:
            return self.pos
            

    def getPos(self):
        print('A posição do competidor {} é {}.'.format(competidor.nome,competidor.pos))
        return self.pos
    
nomes = ['Zodiark', 'Rubicante', 'Elidibus', 'Nidhogg', 'Shinryu']
competidores = []
for i in range (5):
    competidor = Competidor(nomes[i])
    competidores.append(competidor)

rodada = 1

while win == 0:
    print('-------------Rodada {} -------------'.format(rodada))
    rodada +=1
    for competidor in competidores:
        competidor.atualizar()
        print ('O competidor {} está na posição {}.'.format(competidor.nome,competidor.pos))
        if competidor.pos >=20:
            print ('{} venceu!'.format(competidor.nome))
            win+=1
            break
        