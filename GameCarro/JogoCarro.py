import pygame,sys
from random import  randint,random
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import Sprite,Group,GroupSingle
from time import sleep

class Cars():

 pygame.init()


x = 300
y = 440
pos_x = 400
pos_y = -400

velocidade = 5
velocidade2 = 20
tempo = pygame.time.Clock()
score = 0

dificuldade  = 1.3


#Cria janela

altura,largura = 800,600

janela = pygame.display.set_mode((altura,largura))
fundo = pygame.image.load("c:/JogosPython/GamePython/GameCarro/estrada.png")
fundo = pygame.transform.scale(fundo,(800,600))  #Redirecionamneto da imagem
pygame.display.set_caption("Jogo do carro")

janela_aberta = True


def Carros():
    global x,y
    carroPrincipal = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroPreto.png")
    CarroRect = carroPrincipal.get_rect()
    CarroRect.x = x
    CarroRect.y = y

    carroRed = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroRed.png")
    CarroRect2 = carroRed.get_rect()
    CarroRect2.x = pos_x
    CarroRect2.y += pos_y

        


    carroRoxo = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroRoxo01.png")
    CarroRect3 = carroRoxo.get_rect()
    CarroRect3.x += pos_x - 100
    CarroRect3.y = pos_y - 400

    carroYellow = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroYellow.png")
    CarroRect4 = carroYellow.get_rect()
    CarroRect4.x = pos_x
    CarroRect4.y += pos_y -800

    #colisoes
    if CarroRect.colliderect(CarroRect2):
        exit()

    if CarroRect.colliderect(CarroRect3):
        exit()

    #motra na tela
    janela.blit(carroPrincipal,CarroRect)
    janela.blit(carroRed,CarroRect2)
    janela.blit(carroRoxo,CarroRect3)
    janela.blit(carroYellow,CarroRect4)

def controles():
    global x, y,pos_y
    comando = pygame.key.get_pressed()
    if comando[pygame.K_UP]:
        pos_y += 10
    if comando[pygame.K_LEFT]:
        x -= velocidade
    if comando[pygame.K_RIGHT]:
        x += velocidade

def movinta_carro():
    global pos_y,velocidade
    if (pos_y >= 1500):
        pos_y = -700
    pos_y += velocidade



while janela_aberta:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False


    janela.blit(fundo,(0,0))
    Carros()
    controles()
    movinta_carro()
    tempo.tick(40)
    pygame.display.update()



pygame.quit()