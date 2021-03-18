
import pygame.font


class ScoreBoard():
    def __init__(self,ai_config,tela,stats):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.ai_config = ai_config
        self.stats = stats
        #configuraço da fonte na tela
        self.text_color = (220,220,220)
        self.font = pygame.font.SysFont(None,48)

        #prepara a imagem
        self.prep_score()
    def prep_score(self):
        #transforma o texto em imagem
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_config.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right + 10
        self.score_rect.top = 20

    def show_score(self):
        #desenha a pontuaçao na tela
        self.tela.blit(self.score_image,self.score_rect)