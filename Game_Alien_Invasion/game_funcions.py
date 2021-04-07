import sys
from bullet import Bullet
import pygame
from alien import Alien
from time import sleep


def check_high_score(stats,sc):
    #verifica se ha uma nov apontuaçao
    if stats.score > stats.high_score:
       stats.high_score = stats.score
       sc.prep_high_score()


def chek_alien_botton(ai_config,stats,tela,nave,aliens,bullets):
    #verifica se algum alien colidiu  com a borda
    tela_rect  = tela.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_rect.bottom:
           nave_hit(ai_config,stats,tela,nave,aliens,bullets)


def nave_hit(ai_config,stats,tela,nave,aliens,bullets):
    #Responde ao fato da espaçonave ter sido atingida por um alien
    if stats.nave_left > 0:
       stats.nave_left -= 1
    #Esvazia a lista de Aliens
       aliens.empty()
       bullets.empty()
    #Cria uma frota e centraliza
       create_aliens(ai_config,tela,nave,aliens)
       nave.center_nave()
       sleep(1)
    else:
       stats.game_active = False
       pygame.mouse.set_visible(True)


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


def update_aliens(ai_config,stats,tela,nave,aliens,bullets):
    #verifica a posiçao dos aliens entao atualiza a frota de aliens
    check_frota_borderd(ai_config,aliens)
    aliens.update()
    #verifica se houve colisao entre a nave e o alien
    if pygame.sprite.spritecollideany(nave,aliens):
       nave_hit(ai_config,stats,tela,nave,aliens,bullets)
       print("Oh Shit")
    chek_alien_botton(ai_config,stats,tela,nave,aliens,bullets)
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

def bullets_update(ai_config,tela,sc,stats,nave,aliens,bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien(ai_config,tela,sc,stats,nave,aliens,bullets)
def check_bullet_alien(ai_config,tela,sc,stats,nave,aliens,bullets):
    # Verifica se os objetos colidiram
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += ai_config.alien_point
        sc.prep_score()
        check_high_score(stats,sc)
    if len(aliens) ==  0:
        bullets.empty()
        ai_config.add_speed()
        create_aliens(ai_config,tela,nave,aliens)

def fire_bullet(ai_config,tela,nave,bullets):
    if len(bullets) <= ai_config.bullets_permitidas:
        new_bullet = Bullet(ai_config, tela, nave)
        bullets.add(new_bullet)

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


def check_eventos(ai_config,tela,stats,sc,nave,aliens,bullets,play_button):
     #redesenha o laço a cada passagem
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
              sys.exit
        #responde aos eventos precionados as teclas do mouse
       elif event.type == pygame.KEYDOWN:   
             chek_event_Keydown(event, ai_config, tela, nave ,bullets)
       elif event.type == pygame.KEYUP:
             check_event_KeyUp(event,nave)
       elif event.type == pygame.MOUSEBUTTONDOWN:
           mouse_x,mouse_y = pygame.mouse.get_pos()
           check_play_buttons(ai_config, tela, stats, play_button, nave, aliens,
                      bullets, mouse_x, mouse_y)

def check_play_buttons(ai_config,tela, stats, play_button, nave, aliens,
                      bullets, mouse_x, mouse_y):
    #inicia um novo jogo quando o botao e clicado
     btn_cliked =  play_button.rect.collidepoint(mouse_x,mouse_y)
     if btn_cliked and not stats.game_active:
           #Reinicializa as configuraçoes do jogo
           stats.game_active = True
           stats.reset_stats()
           ai_config.inicializa_config()
           # Oculta o visor do Mouse
           pygame.mouse.set_visible(False)
           print("foi clicado")

def update_tela(ai_config,tela,stats,sc,nave,aliens,bullets,play_button):
    tela.fill(ai_config.bg_color)
    #desenha a pontuaçao do  jogo
    for bullet in bullets.sprites():
        bullet.b_draw_bullet()
    nave.blitme()
    aliens.draw(tela)
    sc.show_score()
    if not stats.game_active:
       play_button.draw_button()
     #deixa a tela mais recente visivel
    pygame.display.flip()   
               