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
                if randint(1,100) < 25:
                    is_bomb = True
                piece = Piece(is_bomb,False)
                linha.append(piece)
            self.tabuleiro.append(linha)
        self.load_tabuleiro_num()
    
    def get_piece(self,linha,coluna):
        return self.tabuleiro[linha][coluna]
    
    def click(self,linha,coluna,flag):

        peca = self.get_piece(linha,coluna)

        if flag:
            
            peca.is_bandeira = not peca.is_bandeira
            return
        
        peca.is_click = True
        
    
    
    def load_tabuleiro_num(self):
        for row in range(self.linha):
            for coluna in range(self.coluna):
                peca = self.get_piece(row,coluna)
                peca.vizinhos = self.get_vizinhos(row,coluna)
                peca.num_bomb = self.get_num_bombs(peca.vizinhos)
    
    def get_vizinhos(self,line,col):
        vizin = []
        for row in range(line - 1,line + 2):
            for colm in range(col - 1,col + 2):
                decisao = row < 0 or row >= self.linha or colm < 0 or colm >= self.coluna
                if row == line and colm == col or decisao:
                    continue

                vizin.append((row,colm))

        return vizin
    
    def get_num_bombs(self,lista_vizinhos):
        cont = 0

        for l,c in lista_vizinhos:

            if self.get_piece(l,c).is_bomb:
                cont += 1
        
        return cont