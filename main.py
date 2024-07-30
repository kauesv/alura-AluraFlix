from modelos.filme import Filme
from modelos.serie import Serie
from modelos.playlist import Playlist

def main():

    # -------------------------------------
    #   Criando obj
    #
    tmep = Filme('Todo mundo em pânico', 1999, 100)
    demolidor = Serie('Demolidor', '2016', 2)

    tmep.dar_likes()
    demolidor.dar_likes()
    demolidor.dar_likes()

    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    vingadores.dar_likes()
    #print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}')

    atlanta = Serie('atlanta', 2018, 2)
    atlanta.dar_likes()
    atlanta.dar_likes()
    #print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}')

    # -------------------------------------
    #   listando os filmes e series criados
    #
    filmes_e_series = [vingadores, atlanta, demolidor, tmep]

    # -------------------------------------
    #   playlist
    #
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    print(f'Tamanho do playlist: {playlist_fim_de_semana.tamanho}')

    for programa in playlist_fim_de_semana:
        print(programa)

    #Validar se o domolidor esta dentro da lista
    print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')


# Valida se é o arquivo principal
if __name__ == '__main__':
    main()