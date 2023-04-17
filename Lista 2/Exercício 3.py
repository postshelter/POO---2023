ver = 0

class CadastroCliente:
    def __init__(self, nome, sobrenome, datanasc, email, cpf, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.datanasc = datanasc
        self.email = email
        self.cpf = cpf
        self.senha = senha

    def cadastrar(self):
        self.nome = input('Informe o seu nome: ')
        self.sobrenome = input('Informe o seu sobrenome: ')
        self.datanasc = input('Informe sua data de nascimento:')
        self.email = input('Informe seu e-mail: ')
        self.cpf = input('Informe seu CPF: ')
        self.senha = input('Informe a senha que deseja utilizar: ')

    def checarDados(self):
        print('Nome: {}'.format(self.nome))
        print('Sobrenome: {}'.format(self.sobrenome))
        print('Data de Nascimento: {}'.format(self.datanasc))
        print('E-mail: {}'.format(self.email))
        print('CPF: {}'.format(self.cpf))
        print('Senha: {}'.format(self.senha))

    

cadastro = CadastroCliente('','','','','','')
cadastro.cadastrar()

while ver < 3:
    emailver = input('Informe seu e-mail: ')
    senhaver = input('Informe sua senha: ')
    if emailver == cadastro.email and senhaver == cadastro.senha:
         cadastro.checarDados()
    else:
        print('Dados incorretos, tente novamente.')
        ver+=1
else:
    print('Conta bloqueada!')
    input('Pressione ENTER para finalizar o programa.')
