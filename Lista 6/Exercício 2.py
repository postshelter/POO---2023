class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass


class AssinaturaSimples(Assinatura):
    def calcular_preco(self): #Não sabia se usava um print (ex:'O preço da assinatura é R$29,99) ou se só retornava o valor, como no enunciado dizia retorne optei por só retornar o valor.
        return 29.99 

    def exibir_detalhes(self):
        print("Assinatura Simples: Acesso a filmes e séries em qualidade padrão.")


class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium: Acesso a filmes e séries em qualidade HD e Ultra HD.")

Simples = AssinaturaSimples()
Premium = AssinaturaPremium()

assinaturas = []

assinaturas.append(Simples)
assinaturas.append(Premium)

for assinatura in assinaturas:
    print ('Tipo de assinatura: {}'.format(type(assinatura).__name__)) #Não tinha certeza se o tipo/nome da assinatura precisava ser um atributo, optei por não fazer ser um atributo e pesquisei esse comando na internet para exibir o nome da classe no lugar.
    print(assinatura.calcular_preco())
    assinatura.exibir_detalhes()
