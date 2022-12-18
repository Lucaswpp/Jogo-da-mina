import pygame as pyg
from sys import exit
from os import listdir

class Game():

    def __init__(self,tabuleiro):
        self.tabuleiro = tabuleiro
        self.altura = 630
        self.largura = 630
        self.janela = pyg.display.set_mode((self.largura,self.altura))
        self.fps = pyg.time.Clock()
        self.titulo = pyg.display.set_caption("Jogo da Mina")
        self.tamanho_piece = (self.altura/self.tabuleiro.linha,self.largura/self.tabuleiro.coluna)
        self.load_img()

    def draw_game(self):
        self.fps.tick(30)
        for linha in range(self.tabuleiro.linha):
            for coluna in range(self.tabuleiro.coluna):
                pos_tela = (coluna*self.tamanho_piece[0],linha*self.tamanho_piece[1])
                piece = self.tabuleiro.get_piece(linha,coluna)
                img = self.get_img(piece)
                self.janela.blit(self.imagens[img],pos_tela)
        pyg.display.update()
    
    def event_game(self):

        for evento in pyg.event.get():
            if evento.type == pyg.QUIT:

                exit()
                pyg.quit()
    def load_img(self):
        self.imagens = {}
        for i in listdir("assets"):
            imagem = pyg.image.load(f"assets/{i}")
            imagem = pyg.transform.scale(imagem,self.tamanho_piece)
            nome_arq = i.split(".")[0]
            self.imagens[nome_arq] = imagem
    
    def get_img(self,piece):

        if piece.is_bomb:
            return "bomb-at-clicked-block"
        
        else:
            return "empty-block"