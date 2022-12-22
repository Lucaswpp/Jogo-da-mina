import pygame as pyg

BRANCO = (255,255,255)
class Tela_inicial():

    def __init__(self,game):

        self.game = game
        self.altura = self.game.altura
        self.largura = self.game.largura
        self.canvas = pyg.Surface((self.largura,self.altura))
        self.path_font = "font/Pixel.ttf"
        self.fonte_lose = pyg.font.Font(self.path_font,65).render("Game over",True,BRANCO)
        self.JCENTER = (self.largura/2,self.altura/2)
        self.pos_fonte_lose = self.fonte_lose.get_rect(center=self.JCENTER)
        self.font_aviso = pyg.font.Font(self.path_font,32).render("Clique no r para jogar",True,BRANCO)
        self.font_aviso_rect = self.font_aviso.get_rect(center=(self.JCENTER[0],self.JCENTER[1] + 50))

    def draw_tela_inicial(self):

        self.game.janela.blit(self.canvas,(0,0))
        self.game.janela.blit(self.fonte_lose,self.pos_fonte_lose)