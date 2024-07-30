from modelos.programa import Programa

class Filme(Programa):
    """ A Classe Filme recebe como Classe Mãe(herança) o Programa, assim assim recebendo todos 
    os atributos e métodos
    """
    def __init__(self, nome, ano, duracao):
        
        # Chamando a classe mãe(Programa) e criando o atributo nome e ano (Subscrevendo o metodo init)
        # Com o Super a gente consegue usar tudo que esta disponivel da classe mãe(Programa)
        super().__init__(nome, ano)
        
        # Aqui estou agregando um novo atributo a classe Filme
        self.duracao = duracao

    # ----------
    #   
    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Duração: {self.duracao}Min')

    # ----------
    #   AO INVES DE USAR A FUNCAO IMPRIME, USAMOS ESSE JEITO DE FAZER
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Duração: {self.duracao}Min'