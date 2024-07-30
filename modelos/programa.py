class Programa():
    """ Descrição da classe """
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        """Adicionando um like"""
        self._likes += 1

    # ----------
    # PROPERTY - Usando @property, você pode "reutilizar" o 
    # nome de uma propriedade para evitar a criação de novos nomes 
    # para os getters, setters e deleters.
    # Então ao inves de criar um get_nome, vou continuar usando o "nome" assim não afetando
    # outros processos que usam esse modulo ou atributo.
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}')
    
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}'