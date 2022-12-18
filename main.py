from game import Game
from tabuleiro import Tabuleiro

tabuleiro = Tabuleiro()
jogo = Game(tabuleiro)

while True:

    jogo.event_game()
    jogo.draw_game()