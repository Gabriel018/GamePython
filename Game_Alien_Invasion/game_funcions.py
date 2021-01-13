import sys

import pygame
def check_eventos(nave):
     #redesenha o laço a cada passagem
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
              sys.exit
        #responde aos eventos precionados as teclas do mouse
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
                 nave.moving_right = True
           if event.key == pygame.K_LEFT:
                 nave.moving_left = True     
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_RIGHT:
                 nave.moving_right = False 
           if event.key == pygame.K_LEFT:
                 nave.moving_left = False        

              
def update_tela(ai_config, tela, nave):
    
    tela.fill(ai_config.bg_color)
    nave.blitme()
    #deixa a tela mais recente visivel
    pygame.display.flip()              