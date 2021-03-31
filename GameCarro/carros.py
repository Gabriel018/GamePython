import pygame

class Car():

   def __init__(self,janela,x,y,pos_x,pos_y):
    self.janela = janela
    self.x = x
    self.y = y
    self.pos_x = pos_x
    self.pos_y = pos_y

    carroPrincipal = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroPreto.png")
    CarroRect = carroPrincipal.get_rect()
    CarroRect.x = self.x
    CarroRect.y = self.y

    carroRed = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroRed.png")
    CarroRect2 = carroRed.get_rect()
    CarroRect2.y += self.pos_y + 100
    CarroRect2.x = self.pos_x

    carroRoxo = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroRoxo01.png")
    CarroRect3 = carroRoxo.get_rect()
    CarroRect3.x += self.pos_x + 120
    CarroRect3.y = self.pos_y - 400

    if CarroRect.colliderect(CarroRect2):
     exit()

    if CarroRect.colliderect(CarroRect3):
     exit()

    janela.blit(carroPrincipal, CarroRect)
    janela.blit(carroRed, CarroRect2)
    janela.blit(carroRoxo, CarroRect3)