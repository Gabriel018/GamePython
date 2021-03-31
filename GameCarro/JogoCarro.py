import pygame,sys
from pygame.transform import scale
from pygame.image import load

class jogo_car():


 pygame.init()

x = 400
y = 300
pos_x = 300
pos_y = -400

velocidade = 10
velocidade2 = 20



#Cria janela

janela = pygame.display.set_mode((800,600))
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
    CarroRect2.y += pos_y + 100


    carroRoxo = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroRoxo01.png")
    CarroRect3 = carroRoxo.get_rect()
    CarroRect3.x += pos_x + 120
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
    global x, y
    comando = pygame.key.get_pressed()
    if comando[pygame.K_UP]:
        y -= velocidade
    if comando[pygame.K_DOWN]:
        y += velocidade
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
    pygame.time.delay(50)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False

    janela.blit(fundo,(0,0))
    Carros()
    controles()
    movinta_carro()
    pygame.display.update()



pygame.quit()