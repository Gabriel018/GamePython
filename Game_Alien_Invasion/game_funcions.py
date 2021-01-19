import sys
from bullet import Bullet
import pygame


def chek_event_Keydown(event, ai_config,tela ,nave ,bullets):
      
      if event.key == pygame.K_RIGHT:
            nave.moving_right = True
      if event.key == pygame.K_LEFT:
            nave.moving_left = True
      elif event.key == pygame.K_SPACE:
           new_bullet = Bullet(ai_config,tela,nave)
           bullets.add(new_bullet)      
def check_event_KeyUp(event,nave):
     if event.key == pygame.K_RIGHT:
            nave.moving_right = False 
     if event.key == pygame.K_LEFT:
            nave.moving_left = False                     

def check_eventos(ai_config, tela, nave, bullets):
     #redesenha o laço a cada passagem
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
              sys.exit     
                  
        #responde aos eventos precionados as teclas do mouse
       elif event.type == pygame.KEYDOWN:   
             chek_event_Keydown(event, ai_config, tela, nave ,bullets)  
       elif event.type == pygame.KEYUP:
             check_event_KeyUp(event,nave)
              
def update_tela(ai_config, tela, nave,bullets):
    
    tela.fill(ai_config.bg_color)
    nave.blitme()
    for bullet in bullets.sprites():
        bullet.b_draw_bullet()
    #deixa a tela mais recente visivel
    pygame.display.flip()   
               