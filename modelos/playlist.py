class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #  dunder method - que, ao ser implementado, permite que a classe seja considerada um objeto iterável
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)