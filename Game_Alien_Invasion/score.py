
import pygame.font
from pygame.sprite import Group
from nave_invasion import Nave

class ScoreBoard():
    def __init__(self,ai_config,tela,stats):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.ai_config = ai_config
        self.stats = stats
        #configuraço da fonte na tela
        self.text_color = (220,220,220)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.pontuacao()
        self.historico()
        self.txt_level()
        self.prep_nave()

    def prep_nave(self):
        self.naves = Group()
        for nave_numero in  range(self.stats.nave_left):
            nave = Nave(self.ai_config,self.tela)
            nave.rect.x = 10 + nave_numero * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)

    def txt_level(self):
        self.font2 = pygame.font.SysFont(None,38)
        self.txt_lv_image = self.font2.render("Level",True,self.text_color,self.ai_config.bg_color)
        self.txt_lv_rect = self.txt_lv_image.get_rect()
        self.txt_lv_rect.right = self.level_rect.right
        self.txt_lv_rect.bottom = self.level_rect.top

    def prep_level(self):
        #Transforma o Lv em uma imagem renderizada
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.ai_config.bg_color)
        #posiciona o level abaixo da pontuaçao
        self.level_rect =self.level_image.get_rect()
        self.level_rect.right = self.tela_rect.right
        self.level_rect.top =  30


    def historico(self):
        self.font2 = pygame.font.SysFont(None, 38)
        self.historico_image = self.font2.render("Historico", True, self.text_color, self.ai_config.bg_color)
        self.historico_rect = self.historico_image.get_rect()
        self.historico_rect.left = self.high_score_rect.left
        self.historico_rect.bottom = self.high_score_rect.top

    def pontuacao(self):
        self.font2 = pygame.font.SysFont(None, 38)
        self.texto_image = self.font2.render("Pontuaçao", True, self.text_color, self.ai_config.bg_color)
        self.texto_rect = self.texto_image.get_rect()
        self.texto_rect.left = self.score_rect.left
        self.texto_rect.top = self.score_rect.top + 10


    def prep_high_score(self):
        #transforma a pontuaçao em uma imagem redenrizada
      high_score = int(round(self.stats.high_score,-1))
      high_score_str = "{:}".format(high_score)
      self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_config.bg_color)
       #Centrliza a imagem na tela
      self.high_score_rect = self.high_score_image.get_rect()
      self.high_score_rect.centerx = self.tela_rect.centerx
      self.high_score_rect.top = 30

    def prep_score(self):
        #transforma o texto em imagem
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_config.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.tela_rect.left
        self.score_rect.top = 30

    def show_score(self):
        #desenha a pontuaçao na tela
        self.tela.blit(self.score_image,self.score_rect)
        self.tela.blit(self.high_score_image,self.high_score_rect)
        self.tela.blit(self.texto_image,self.tela_rect)
        self.tela.blit(self.historico_image,self.historico_rect)
        self.tela.blit(self.level_image,self.level_rect)
        self.tela.blit(self.txt_lv_image,self.txt_lv_rect)
        self.naves.draw(self.tela)