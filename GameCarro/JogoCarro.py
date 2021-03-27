import pygame

class jogo_car():

 pygame.init()

x = 400
y = 300
pos_x = 300
pos_y = -100

velocidade = 10
velocidade2 = 20

fundo =  pygame.image.load("c:/JogosPython/GamePython/GameCarro/fundo.png")

carroRoxo = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroRoxo01.png")


carroPrincipal = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroPreto.png")
CarroRect = carroPrincipal.get_rect()


carroRed = pygame.image.load("c:/JogosPython/GamePython/GameCarro/CarroRed.png")
CarroRect2 = carroRed.get_rect()


if CarroRect.collidepoint(100,100):
    print("colidiu")

#Cria janela
janela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo do carro")
janela_aberta = True




#Desenha Objeto

while janela_aberta:
    pygame.time.delay(50)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False


    comando = pygame.key.get_pressed()
    if comando[pygame.K_UP]:
       y -= velocidade
    if comando[pygame.K_DOWN]:
       y += velocidade
    if comando[pygame.K_LEFT]:
       x -= velocidade
    if comando[pygame.K_RIGHT]:
       x += velocidade

    if (pos_y >= 900):
        pos_y = -300

    pos_y += velocidade2

    janela.blit(fundo,(0,0))
    janela.blit(carroPrincipal,((x,y)))
    janela.blit(carroRoxo,(pos_x +110,pos_y -400))
    janela.blit(carroRed, (pos_x, pos_y ))


    pygame.display.update()



pygame.quit()
