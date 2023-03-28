playlist = []

class Musica:
    def __init__(self, titulo, artistabanda, genero, ano, duracao):
        self.titulo = titulo
        self.artistabanda = artistabanda
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

    def play(self):
        print('Tocando agora {} por {}.'.format(self.titulo,self.artistabanda))

    def informacoes(self):
        print('''Título: {}\nArtista/Banda: {}\nGênero: {}\nAno: {}\nDuração: {}.'''.format(self.titulo, self.artistabanda, self.genero, self.ano, self.duracao))

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

playlist.append(lt)
playlist.append(ps)
playlist.append(utt)
playlist.append(rmb)
playlist.append(gbs)

print(playlist[0].titulo)
print(playlist[1].titulo)
print(playlist[2].titulo)
print(playlist[3].titulo)
print(playlist[4].titulo)



