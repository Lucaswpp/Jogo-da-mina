import pygame as pyg
from sys import exit
from os import listdir
from time import sleep
from tela_inicial import Tela_inicial

class Game():

    def __init__(self,tabuleiro):
        pyg.init()
        self.tabuleiro = tabuleiro
        self.altura = 630
        self.largura = 630
        self.janela = pyg.display.set_mode((self.largura,self.altura))
        self.fps = pyg.time.Clock()
        self.titulo = pyg.display.set_caption("Jogo da Mina")
        self.tamanho_piece = (self.altura/self.tabuleiro.linha,self.largura/self.tabuleiro.coluna)
        self.is_run_game = True
        self.is_win = False
        self.is_lose = False
        self.tela_inicial = Tela_inicial(self)
        self.game_state = 'run'
        self.load_img()

    def draw_game(self):
        self.fps.tick(30)

        if self.game_state == "run":
            for linha in range(self.tabuleiro.linha):
                for coluna in range(self.tabuleiro.coluna):
                    pos_tela = (coluna*self.tamanho_piece[0],linha*self.tamanho_piece[1])
                    piece = self.tabuleiro.get_piece(linha,coluna)
                    img = self.get_img(piece)
                    self.janela.blit(self.imagens[img],pos_tela)
        
        elif self.game_state == "lose":
            self.tela_inicial.draw_tela_inicial()

        pyg.display.update()
    
    def event_game(self):

        for evento in pyg.event.get():
            if evento.type == pyg.QUIT:
                exit()
                pyg.quit()
            
            elif evento.type == pyg.MOUSEBUTTONDOWN:
                pos_mouse = pyg.mouse.get_pos()
                pos_coluna = int(pos_mouse[0]/self.tamanho_piece[0])
                pos_linha = int(pos_mouse[1]/self.tamanho_piece[1])
                self.tabuleiro.click(pos_linha,pos_coluna,pyg.mouse.get_pressed()[2],self)

    def load_img(self):
        self.imagens = {}
        for i in listdir("assets"):
            imagem = pyg.image.load(f"assets/{i}")
            imagem = pyg.transform.scale(imagem,self.tamanho_piece)
            nome_arq = i.split(".")[0]
            self.imagens[nome_arq] = imagem
    
    def get_img(self,piece):

        if piece.is_click:

            if piece.is_bomb:
                return "bomb-at-clicked-block"
            
            return str(piece.num_bomb)
        
        elif piece.is_bandeira:
            return "flag"

        return "empty-block"

    def run_game(self):

        while self.is_run_game:

            self.event_game()
            self.draw_game()
            
            if self.is_win and not self.game_state == "win":
                self.game_state = "win"
                self.is_run_game = False
            
            elif self.is_lose and not self.game_state == "lose":
                self.game_state = "lose"
                sleep(3)