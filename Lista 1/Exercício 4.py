class Musica:
    def __init__(self, nome, artistabanda, genero, ano, duracao):
        self.nome = nome
        self.artistabanda = artistabanda
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

    def play(self):
        print('Tocando agora {} por {}.'.format(self.nome,self.artistabanda))

    def informacoes(self):
        print('''Título: {}\nArtista/Banda: {}\nGênero: {}\nAno: {}\nDuração: {}.'''.format(self.nome, self.artistabanda, self.genero, self.ano, self.duracao))

lt = Musica('Lagtrain', 'Inabakumori', 'Vocaloid','2020','4:11')
ps = Musica('Post Shelter', 'Inabakumori', 'Vocaloid','2022','3:20')
utt = Musica('UNDER THE TREE', 'SiM', 'J-Rock', '2023', '2:20')
rmb = Musica ('The Rumbling', 'SiM', 'J-Rock', '2022', '3:41')
gbs = Musica('goosebumps', 'Travis Scott', 'Rap', '2016', '4:04')

lt.play()
lt.informacoes()

ps.play()
ps.informacoes()

utt.play()
utt.informacoes()

rmb.play()
rmb.informacoes()

gbs.play()
gbs.informacoes()
