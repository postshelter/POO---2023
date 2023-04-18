#Exercício 1
class Pais:
    def __init__(self, codigo_iso=None, nome=None, populacao=None, dimensao=None):
        self.codigo_iso = codigo_iso
        self.nome = nome
        self.populacao = populacao
        self.dimensao = dimensao
        self.fronteiras = []

    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
    def setCodigo(self, codigo_iso):
        self.codigo_iso = codigo_iso

    def getCodigo(self):
        return self.codigo_iso
    
    def setPopulacao(self, populacao):
        self.populacao = populacao

    def getPopulacao(self):
        return self.populacao

    def setDimensao(self, dimensao):
        self.dimensao = dimensao

    def getDimensao(self):
        return self.dimensao    

    def compararIgual(self,pais):
        if self.codigo_iso == pais.getCodigo():
            return True
        else:
            return False
        
    def calcularDensidade(self):
        densidade = self.populacao / self.dimensao
        return densidade
    
    def verificarFronteira(self, pais):
        for i in self.fronteiras:
            if i.compararIgual(pais) == True:
                return True
        return False
    
    def adicionarFronteira(self, pais):
        self.fronteiras.append(pais)

    def getFronteiras(self):
        return self.fronteiras
    
    def listarFronteiras(self):
        for i in self.fronteiras:
            print(i.getCodigo())

    def fronteirasComuns(self, pais):
        fronteirasPais = pais.getFronteiras()
        fronteirasComuns = []
        for i in fronteirasPais:
            if self.verificarFronteira(i) == True:
                fronteirasComuns.append(i)
        return fronteirasComuns
    
pais01 = Pais()
pais02 = Pais()
pais03 = Pais()
pais04 = Pais()
pais05 = Pais()
pais06 = Pais()


print('------------Dados do País 01------------')
pais01.setNome('Brasil')
pais01.setCodigo('BRA')
pais01.setDimensao(8510345.538)
pais01.setPopulacao(211755692)
print(pais01.getCodigo())
print(pais01.getNome())
print(pais01.getDimensao())
print(pais01.getPopulacao())
print(pais01.calcularDensidade())



print('------------Dados do País 02------------')
pais02.setNome('Argentina')
pais02.setCodigo('ARG')
pais02.setDimensao(2796427)
pais02.setPopulacao(45606000)
pais02.calcularDensidade()
print(pais02.getCodigo())
print(pais02.getNome())
print(pais02.getDimensao())
print(pais02.getPopulacao())
print(pais02.calcularDensidade())



print('------------Dados do País 03------------')
pais03.setNome('Uruguai')
pais03.setCodigo('URU')
pais03.setDimensao(173626)
pais03.setPopulacao(3474000)
print(pais03.getCodigo())
print(pais03.getNome())
print(pais03.getDimensao())
print(pais03.getPopulacao())
print(pais03.calcularDensidade())



print('------------Dados do País 04------------')
pais04.setNome('Paraguai')
pais04.setCodigo('PAR')
pais04.setDimensao(406752)
pais04.setPopulacao(6348917)
print(pais04.getCodigo())
print(pais04.getNome())
print(pais04.getDimensao())
print(pais04.getPopulacao())
print(pais04.calcularDensidade())



print('------------Dados do País 05------------')
pais05.setNome('Chile')
pais05.setCodigo('CHI')
pais05.setDimensao(756945)
pais05.setPopulacao(16970265)
print(pais05.getCodigo())
print(pais05.getNome())
print(pais05.getDimensao())
print(pais05.getPopulacao())
print(pais05.calcularDensidade())



print('------------Dados do País 06------------')
pais06.setNome('Peru')
pais06.setCodigo('PER')
pais06.setDimensao(1285216)
pais06.setPopulacao(33359000)
print(pais06.getCodigo())
print(pais06.getNome())
print(pais06.getDimensao())
print(pais06.getPopulacao())
print(pais06.calcularDensidade())



pais01.adicionarFronteira(pais02)
pais01.adicionarFronteira(pais03)
pais01.adicionarFronteira(pais04)
pais01.adicionarFronteira(pais06)



pais02.adicionarFronteira(pais01)
pais02.adicionarFronteira(pais03)
pais02.adicionarFronteira(pais04)
pais02.adicionarFronteira(pais05)



print('------------Fronteiras do Brasil-----------')
pais01.listarFronteiras()



print('------------Fronteiras da Argentina------------')
pais02.listarFronteiras()



print('------------Fronteiras em comum------------')

        
vizinhosComuns = (pais01.fronteirasComuns(pais02))

for i in vizinhosComuns:
    print(i.getCodigo())



#Exercício 2
class Continente:
    def __init__(self, nome = None):
        self.nome = nome
        self.paises = []
        
    def setNome(self, nome):
        self.nome = nome

    def adicionarPais(self, pais):
        self.paises.append(pais)

    def dimensaoTotal(self):
        return sum (pais.dimensao for pais in self.paises)
    
    def populacaoTotal(self):
        return sum (pais.populacao for pais in self.paises)
    
    def dimensaoMax(self):
        return max (pais.dimensao for pais in self.paises)
    
    def dimensaoMin(self):
        return min (pais.dimensao for pais in self.paises)
    
    def densidadeDemografica(self):
        return self.populacaoTotal() / self.dimensaoTotal()

    def populacaoMax(self):
        maior_pop = 0
        nomemaxpop = ''
        for pais in self.paises:
            if pais.populacao > maior_pop:
                maior_pop = pais.populacao
                nomemaxpop = pais.nome
                return nomemaxpop
            
    def populacaoMin(self):
        menor_pop = float('inf') #Tive que procurar essa variável na internet, não consegui fazer inicializando com zero.
        nomeminpop = ''
        for pais in self.paises: 
            if pais.populacao < menor_pop:
                menor_pop = pais.populacao
                nomeminpop = pais.nome
        return nomeminpop
    
    def dimensaoMaxNome(self):
        maior_dim = 0
        nomemaxdim = ''
        for pais in self.paises:
            if pais.dimensao > maior_dim:
                maior_dim = pais.dimensao
                nomemaxdim = pais.nome
                return nomemaxdim

    def dimensaoMinNome(self):
        menor_dim = float('inf')
        nomemindim = ''
        for pais in self.paises:
            if pais.dimensao < menor_dim:
                menor_dim = pais.dimensao
                nomemindim = pais.nome
        return nomemindim
    
    def razaoTerritorial(self):
        return (self.dimensaoMax() / self.dimensaoMin())


continente1 = Continente('América do Sul')
continente1.adicionarPais(pais01)
continente1.adicionarPais(pais02)
continente1.adicionarPais(pais03)
continente1.adicionarPais(pais04)
continente1.adicionarPais(pais05)
continente1.adicionarPais(pais06)

dimensaototal = continente1.dimensaoTotal()
populacaototal = continente1.populacaoTotal()
densidade_demografica = continente1.densidadeDemografica()
populacaomaxima = continente1.populacaoMax()
populacaominima = continente1.populacaoMin()
dimensaomaxima = continente1.dimensaoMaxNome()
dimensaominima = continente1.dimensaoMinNome()
razaoterritorio = continente1.razaoTerritorial()


print('------------Informações do continente------------')
print ('A dimensão total do continente é de {} km².'.format(dimensaototal))
print('A população total do continente é de {} habitantes.'.format(populacaototal))
print('A densidade populacional do continente é de {} hab/km².'.format(densidade_demografica))
print('O país com o maior número de habitantes é {}.'.format(populacaomaxima))
print('O país com o menor número de habitantes é {}.'.format(populacaominima))
print('O país com a maior dimensão territorial é {}.'.format(dimensaomaxima))
print('O país com a menor dimensão territorial é {}.'.format(dimensaominima))
print('A razão territorial entre o maior e o menor país é {}.'.format(razaoterritorio))

