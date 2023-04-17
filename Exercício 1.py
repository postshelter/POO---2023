import random

class Dado:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)
    


dado_d6 = Dado(6)
dado_d8 = Dado(8)
dado_d12 = Dado(12)

for i in range(3):
    print('O resultado é {}.'.format(dado_d6.roll()))
    print('O resultado é {}.'.format(dado_d8.roll()))
    print('O resultado é {}.'.format(dado_d12.roll()))


