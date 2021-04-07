
import pygame.font


class ScoreBoard():
    def __init__(self,ai_config,tela,stats):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.ai_config = ai_config
        self.stats = stats
        #configuraço da fonte na tela
        self.text_color = (220,220,220)
          #Texto placar Pontuaçao
        self.font = pygame.font.SysFont(None,48)
        self.font2 = pygame.font.SysFont(None, 38)
        self.texto_image = self.font2.render("Pontuaçao",True,self.text_color,self.ai_config.bg_color)
        self.texto_rect = self.texto_image.get_rect()
        self.texto_rect.left = self.tela_rect.left
        self.tela_rect.top = self.tela_rect.top
          #texto historico
        self.font2 = pygame.font.SysFont(None,38)
        self.historico_image = self.font2.render("Historico",True,self.text_color,self.ai_config.bg_color)
        self.historico_rect = self.historico_image.get_rect()
        self.historico_rect.centerx = self.tela_rect.centerx
        self.historico_rect.top = self.tela_rect.top

        #prepara a imagem
        self.prep_score()
        self.prep_high_score()
    def prep_high_score(self):
        #transforma a pontuaçao em uma imagem redenrizada
      high_score = int(round(self.stats.high_score,-1))
      high_score_str = "{:}".format(high_score)
      self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_config.bg_color)
       #Centrliza a imagem na tela
      self.high_score_rect = self.high_score_image.get_rect()
      self.high_score_rect.centerx = self.tela_rect.centerx
      self.high_score_rect.top = self.score_rect.top

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