
import pygame,sys

def objetos():
    global veloc_x, veloc_y,velo_z

    pygame.draw.rect(tela, (255, 255, 255), Objeto1)
    Objeto1.x += veloc_x
    Objeto1.y -= veloc_y
    #Objeto1.y += veloc_y

    pygame.draw.rect(tela, (0, 0, 0), Objeto2)
    Objeto2.y += veloc_y
    #coliçao com a borda Objeto 1
    if Objeto1.right >= screm_height or Objeto1.left <=0:
        veloc_x *= -1
    if Objeto1.bottom >= screm_width or Objeto1.top <=0:
        veloc_y *= -1

    if Objeto2.bottom >= screm_width or Objeto2.top <=0:
        veloc_y *= -1


    pygame.draw.rect(tela,(25,25,0),Objeto3)
    #colisao com a borda objeto 2

    #colisao com outro objeto

    if Objeto1.colliderect(Objeto2):
       veloc_x *= -1
    if Objeto1.colliderect(Objeto3):
       veloc_x *= -1

    tolerance = 30
    if Objeto1.colliderect(Objeto2):
        if abs(Objeto2.bottom - Objeto1.top) < tolerance:
            veloc_y *= -1
        if abs(Objeto2.top - Objeto1.bottom) < tolerance:
            veloc_y *= - 1
        if abs(Objeto2.left - Objeto1.right) < tolerance:
            veloc_x *= - 1
        if abs(Objeto2.right- Objeto1.left) < tolerance:
            veloc_x *= - 1
pygame.init()

screm_height,screm_width = 800,600

clock = pygame.time.Clock()
tela = pygame.display.set_mode((screm_height,screm_width))
pygame.display.set_caption("Colisao")
bg_color  = (100,100,100)


Objeto1 = pygame.Rect(670,550,40,40)
#velocidade
veloc_x, veloc_y = 4, 4


Objeto2 = pygame.Rect(750,100,40,120)
veloc_z = 30


Objeto3 = pygame.Rect(20,300,40,120)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        mov_tecla = pygame.key.get_pressed()
        if mov_tecla[pygame.K_UP]:
            Objeto3.y -= veloc_z
        if mov_tecla[pygame.K_DOWN]:
            Objeto3.y += veloc_z

    tela.fill(bg_color)
    objetos()
    pygame.display.update()
    clock.tick(80)





