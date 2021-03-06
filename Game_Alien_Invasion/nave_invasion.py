
import pygame
from pygame.sprite import  Sprite

class Nave(Sprite):
    # inicia inicia a aeronave e poem e sua posiçao
      def __init__(self,ai_config,tela):
          super(Nave,self).__init__()
          self.tela = tela
          self.ai_config = ai_config
          self.image = pygame.image.load('C:/JogosPython/GamePython/Game_Alien_Invasion/image/nave.png')
          self.rect = self.image.get_rect()

          self.tela_rect = tela.get_rect()

          self.rect.centerx = self.tela_rect.centerx
          self.rect.bottom = self.tela_rect.bottom

     # movimento
          self.moving_right = False
          self.moving_left = False
          self.center = float(self.rect.centerx)

      def update(self):
            #atualiza a posiçao da nave
            #atualiza o valor do centro da espaçonave e nao o rect
            if self.moving_right and self.rect.right < self.tela_rect.right:
               self.center += self.ai_config.nave_velocidade
            if self.moving_left and self.rect.left >0:
               self.center -= self.ai_config.nave_velocidade
            self.rect.centerx = self.center

      def blitme(self):
        self.tela.blit(self.image,self.rect)

      def center_nave(self):
          self.center = self.tela_rect.centerx