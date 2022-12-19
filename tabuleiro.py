from peca import Piece
from random import randint
class Tabuleiro():

    def __init__(self):
        self.linha = 9
        self.coluna = 9
        self.load_tabuleiro()
    
    def load_tabuleiro(self):
        self.tabuleiro = []
        for linha in range(self.linha):
            linha = []
            for coluna in range(self.coluna):
                is_bomb = False
                if randint(1,100) > 50:
                    is_bomb = True
                piece = Piece(is_bomb,False)
                linha.append(piece)
            self.tabuleiro.append(linha)
    
    def get_piece(self,linha,coluna):
        return self.tabuleiro[linha][coluna]
    
    def click_bandeira(self,linha,coluna):
        self.get_piece(linha,coluna).is_bandeira = not self.get_piece(linha,coluna).is_bandeira
        