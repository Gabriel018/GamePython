import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_config,tela):
        super(Alien, self).__init__()
        self.tela = tela
        self.ai_config = ai_config
        #Carrega a imagen do alien
        self.image = pygame.image.load('C:/JogosPython/GamePython/Game_Alien_Invasion/image/hungry_alien.png')
        self.rect = self.image.get_rect()
        #inicia proximo ao canto superior esquerdo
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Armazena a posiçao exata do alien
        self.x = float(self.rect.x)

    def check_borderd(self):
        # Se o alien estiver na borda devolve true
        tela_rect = self.tela.get_rect()
        if self.rect.right >= tela_rect.right:
            return True
        if self.rect.left <= tela_rect.left:
            return True

    def update(self):
        #atualiza a direçao do alien
        self.x -= (self.ai_config.alien_speed * self.ai_config.frota_direction)
        self.rect.x = self.x


    def blitme(self):
        #Desenha o aliem em sua posiçao inicial
        self.tela.blit(self.image,self.rect)
