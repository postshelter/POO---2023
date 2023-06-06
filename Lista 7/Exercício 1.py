import csv

class Usuario:
    def __init__(self, nome=None, sobrenome=None, data_de_nascimento=None, cpf=None, nome_de_usuario=None, senha=None, assinaturas=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.nome_de_usuario = nome_de_usuario
        self.senha = senha
        self.assinaturas = []

    def adicionar_assinatura(self,assinatura):
        self.assinaturas.append(assinatura)

    def cancelar_assinatura(self,id_assinatura):
        self.assinaturas.remove(id_assinatura)

    def exibir_dados(self):
        print('Nome: {}'.format(self.nome))
        print('Sobrenome: {}'.format(self.sobrenome))
        print('Data de Nascimento: {}'.format(self.data_de_nascimento))
        print('CPF: {}'.format(self.cpf))
        print('Nome de Usuário: {}'.format(self.nome_de_usuario))
        print('Senha: {}'.format(self.senha))

    def serializar(self):
        return"{},{},{},{},{},{}".format(self.nome, self.sobrenome, self.data_de_nascimento, self.cpf, self.nome_de_usuario, self.senha)
    
    def deserializar(self):
        pass

class Assinatura():
    def __init__(self, tipo=None, preço=None, id_usuario=None, status=None):
        self.tipo=tipo
        self.preço=preço
        self.id_usuario=id_usuario
        self.status=status

    def exibir_dados(self):
        print('Tipo: {}'.format(self.tipo))
        print('Preço: {}'.format(self.preço))
        print('ID do Usuário: {}'.format(self.id_usuario))
        print('Status da assinatura: {}'.format(self.status))

    def serializar(self):
        return"{},{},{},{}".format(self.tipo,self.preço,self.id_usuario,self.status)
    
    def desserializar(self):
        pass


def ler_usuarios_csv(arquivo):
    usuarios = []
    arqCSV = open(arquivo)
    leitor = csv.reader(arqCSV,delimiter=';')
    for linha in leitor:
        usuario = Usuario()
        usuario.desserializar(linha)
        usuarios.append(usuario)
    return usuarios
