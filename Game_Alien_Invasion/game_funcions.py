import sys
from bullet import Bullet
import pygame
from alien import Alien

def check_frota_borderd(ai_config,aliens):
    #responde propriamente se algum alien alcançou a borda
    for alien in aliens.sprites():
        if alien.check_borderd():
         change_frota_direction(ai_config,aliens)
         break
def change_frota_direction(ai_config,aliens):
    #Faz toda a frota  descer e muda sua direçao
    for alien in aliens.sprites():
        alien.rect.y += ai_config.frota_vel_drop
        ai_config.frota_direction = -1


def update_aliens(ai_config,aliens):
    #verifica a posiçao dos aliens entao atualiza a frota de aliens
    check_frota_borderd(ai_config,aliens)
    aliens.update()
def get_number_aliens(ai_config,alien_width):
    avaliacao_space_x = ai_config.tela_width - 2 * alien_width
    number_aliens_x = int(avaliacao_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_config,nave_height,alien_height):
    avaliacao_space_y = (ai_config.tela_heigth - (3 * alien_height) - nave_height)
    number_rows = int(avaliacao_space_y / ( 2 * alien_height))
    return number_rows

def create_alien(ai_config,tela,aliens,alien_number,number_rows):
    #cria um alien em uma determinada posiçao
    alien = Alien(ai_config, tela)
    alien_width  = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_rows
    aliens.add(alien)

def create_aliens(ai_config,tela,nave,aliens,):
    alien = Alien(ai_config,tela)
    number_aliens  = get_number_aliens(ai_config,alien.rect.height)
    number_rows = get_number_rows(ai_config, nave.rect.height, alien.rect.height)
    for row_number in range(number_rows):
     for alien_number in range(number_aliens):
        create_alien(ai_config,tela,aliens,alien_number,row_number)

def bullets_update(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_config,tela,nave,bullets):
    if len(bullets) <= ai_config.bullets_permitidas:
        new_bullet = Bullet(ai_config, tela, nave)
        bullets.add(new_bullet)

    #Cria uma linha de aliens


def chek_event_Keydown(event, ai_config,tela ,nave ,bullets):
      if event.key == pygame.K_RIGHT:
            nave.moving_right = True
      if event.key == pygame.K_LEFT:
            nave.moving_left = True
      elif event.key == pygame.K_SPACE:
       fire_bullet(ai_config,tela,nave,bullets)
      elif event.key == pygame.K_q:
          sys.exit()
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

def update_tela(ai_config, tela, nave,aliens,bullets):

    tela.fill(ai_config.bg_color)
    nave.blitme()
    for bullet in bullets.sprites():
        bullet.b_draw_bullet()
    aliens.draw(tela)
    #deixa a tela mais recente visivel
    pygame.display.flip()   
               