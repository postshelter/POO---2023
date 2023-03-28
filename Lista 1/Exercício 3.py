#Dividi a atividade em 2 classes, a classe Data com o construtor padrão e a classe DataCustom com o construtor personalizado para ficar mais organizado.


#Classe com o construtor padrão.
class Data:
    def __init__(self, dia, mes, ano):

        self.dia = dia
        self.mes = mes
        self.ano = ano

def retornoMesExtenso(self):
    if self.mes == 1:
        return 'Janeiro'
    elif self.mes == 2:
        return 'Fevereiro'
    elif self.mes == 3:
        return 'Março'
    elif self.mes == 4:
        return 'Abril'
    elif self.mes == 5:
        return 'Maio'
    elif self.mes == 6:
        return 'Junho'
    elif self.mes == 7:
        return 'Julho'
    elif self.mes == 8:
        return 'Agosto'
    elif self.mes == 9:
        return 'Setembro'
    elif self.mes == 10:
        return 'Outubro'
    elif self.mes == 11:
        return 'Novembro'
    elif self.mes == 12:
        return 'Dezembro'
    else:
        return 'Data inválida.'
def exibirData(self):
    print('{}/{}/{}'.format(self.dia,self.mes,self.ano))

def exibirDataPorExtenso(self, cidade):
    mes = self.retornoMesExtenso()
    print("{}, {} de {} de {}.".format(cidade,self.dia,self.mes,self.ano))

#Classe com o construtor personalizado.   
class DataCustom:
    def __init__(self,):
        self.__dia = 1
        self.__mes = 1
        self.__ano = 0

    def alterarDia(self,dia):
        self.__dia = dia

    def alterarMes(self,mes):
        self.__mes = mes

    def alterarAno(self,ano):
        self.__ano = ano

    def retornarDia(self):
        return self.__dia
    
    def retornarMes(self):
        return self.__mes
    
    def retornarAno(self):
        return self.__ano    
    
    def exibirData(self):
        print('{}/{}/{}'.format(self.__dia,self.__mes,self.__ano))

    def retornoMesExtenso(self):
        if self.__mes == 1:
            return 'Janeiro'
        elif self.__mes == 2:
            return 'Fevereiro'
        elif self.__mes == 3:
            return 'Março'
        elif self.__mes == 4:
            return 'Abril'
        elif self.__mes == 5:
            return 'Maio'
        elif self.__mes == 6:
            return 'Junho'
        elif self.__mes == 7:
            return 'Julho'
        elif self.__mes == 8:
            return 'Agosto'
        elif self.__mes == 9:
            return 'Setembro'
        elif self.__mes == 10:
            return 'Outubro'
        elif self.__mes == 11:
            return 'Novembro'
        elif self.__mes == 12:
            return 'Dezembro'
        else:
            return 'Data inválida.'   
    def exibirDataPorExtenso(self, cidade):
        self.__mes = self.retornoMesExtenso()
        print("{}, {} de {} de {}.".format(cidade,self.__dia,self.__mes,self.__ano))



data1 = Data(17,12,1992)
exibirData(data1)

data2 = DataCustom()
data2.alterarDia(17)
data2.alterarMes(12)
data2.alterarAno(1992)
dia2 = data2.retornarDia()
mes2 = data2.retornarMes()
ano2 = data2.retornarAno()
print(dia2)
print(mes2)
print(ano2)
print(data2.retornarDia())
data2.exibirData()
data2.exibirDataPorExtenso('São Leopoldo')


