import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_config, tela,nave):
        super(Bullet,self).__init__()
        self.tela = tela

        #Cria um retangulo para o projetil
        self.rect = pygame.Rect(0, 0, ai_config.bullet_width, ai_config.bullet_heigth)
        self.rect.centerx  = nave.rect.centerx
        self.rect.top = nave.rect.top 

        #armazena o  valor do projeto com um valor decima
        self.y  = float(self.rect.y)
        self.color = ai_config.bullet_color

        self.nave_velocidade = ai_config.bullet_velocidade
    def update(self):
        #atualizaza a posiçao decimal do projeto
        self.y -= self.nave_velocidade
        #Atualizaçao do rect
        self.rect.y = self.y
    def b_draw_bullet(self):
        pygame.draw.rect(self.tela,self.color,self.rect)        