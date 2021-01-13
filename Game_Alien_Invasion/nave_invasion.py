
import pygame

class Nave():
    # inicia inicia a aeronave e poem e sua posiçao 
  def __init__(self, tela):
     
     self.tela = tela 

     self.image = pygame.image.load('C:/PythonFiles/image/nave.bmp')
     self.rect = self.image.get_rect()

     self.tela_rect  = tela.get_rect()

     self.rect.centerx = self.tela_rect.centerx
     self.rect.bottom = self.tela_rect.bottom

     #movimento
     self.moving_right = False
     self.moving_left = False

  def update(self):
        if self.moving_right:
              self.rect.centerx += 1
        if self.moving_left:
              self.rect.centerx -= 1
  def blitme(self):
    self.tela.blit(self.image,self.rect)

