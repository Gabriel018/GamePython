import pygame

class Carros():

   def __init__(self,ai_config,janela):
    super(Carros, self).__init__()
    self.janela = janela
    self.ai_config = ai_config
    self.image = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroPreto.png")
    self.rect = self.image.get_rect()

