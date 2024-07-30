from modelos.programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        # Chamando a classe mãe(Programa) e criando o atributo nome e ano
        super().__init__(nome, ano)
        
        self.temporadas = temporadas

    # ----------
    #   
    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Temporadas: T{self.temporadas}')

    # ----------
    #   AO INVES DE USAR A FUNCAO IMPRIME, USAMOS ESSE JEITO DE FAZER
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Temporadas: T{self.temporadas}'