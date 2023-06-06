class UnidadeMilitar():
    def mover(self):
        print('A unidade se move.')

    def atacar(self):
        print('A unidade ataca.')


class Soldado(UnidadeMilitar):
    def mover(self):
        print('O soldado avança.')

    def atacar(self):
        print('O soldado desfere um golpe com sua espada.')


class Arqueiro(UnidadeMilitar):
    def mover(self):
        print('O arqueiro se move.')

    def atacar(self):
        print('O arqueiro dispara uma flecha.')


class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print('O cavaleiro ordena que seu cavalo avance.')

    def atacar(self):
        print('O cavaleiro desfere um golpe com sua lança.')
        

soldado1 = Soldado()
arqueiro1 = Arqueiro()
cavaleiro1 = Cavaleiro()

unidades = []

unidades.append(soldado1)
unidades.append(arqueiro1)
unidades.append(cavaleiro1)

for unidade in unidades:
    unidade.mover()
    unidade.atacar()
