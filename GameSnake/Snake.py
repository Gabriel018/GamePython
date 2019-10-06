import pygame, random
from pygame.locals import *

pygame.init()

def colisao (c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def posicao_randown():
    x = random.randint(0,600)
    y = random.randint(0,600)
    return (x//10*10,y//10*10)

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake")


Snake = [(100, 100),(100, 100),(100, 100)]
Snake_format = pygame.Surface((20,20))
Snake_format.fill((0,0,128))

food = pygame.Surface((20,20))
food.fill((255,0,0))
food_pos = posicao_randown()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
Minhadirecao = RIGHT

clock = pygame.time.Clock()

while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    Minhadirecao = UP
                if event.key == K_DOWN:
                    Minhadirecao = DOWN
                if event.key == K_LEFT:
                    Minhadirecao = LEFT
                if event.key == K_RIGHT:
                    Minhadirecao = RIGHT


        if colisao(Snake[0],food_pos):
           food_pos = posicao_randown()
           Snake.append((0,0))








        for i in range(len(Snake) - 1, 0, -1):
            Snake[i] = (Snake[i - 1][0], Snake[i - 1][1])

        if Minhadirecao == UP:
            Snake[0] = (Snake[0][0], Snake[0][1] - 10)
        if Minhadirecao == DOWN:
            Snake[0] = (Snake[0][0], Snake[0][1] + 10)
        if Minhadirecao == RIGHT:
            Snake[0] = (Snake[0][0] + 10, Snake[0][1])
        if Minhadirecao == LEFT:
            Snake[0] = (Snake[0][0] - 10, Snake[0][1])

        janela.fill((0,0,0))
        janela.blit(food,food_pos)
        for pos in Snake:
            janela.blit(Snake_format,pos)
            pygame.display.update()