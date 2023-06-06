class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar():
        print('Acelerando o veículo!')

    def frear():
        print('Freando o veículo!')

    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

    def ligar_radio():
        print('Ligando o rádio do carro!')

    def abrir_porta():
        print('Abrindo a porta do carro!')

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def empinar():
        print('Empinando a moto!')

    def buzinar():
        print('Buzinando a moto!')

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima

    def carregar():
        print('Carregando o caminhão!')

    def descarregar():
        print('Descarregando o caminhão!')


