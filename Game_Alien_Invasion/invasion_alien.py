import sys
import pygame
from config_invasion import Config
from nave_invasion import Nave
import game_funcions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
        #Inicia o jogo e cria um objeto
     pygame.init()
     bullets = Group()
     aliens = Group()
     ai_config = Config()
     tela = pygame.display.set_mode((ai_config.tela_width,ai_config.tela_heigth))
     #Cria a espaço nave
     nave = Nave(ai_config, tela)
     #cria a frota de aliens
     gf.create_aliens(ai_config,tela,nave,aliens)
     pygame.display.set_caption("Invasao_alien")
      #inicia o laço de repetiçao do jogo
     while True:

      gf.check_eventos(ai_config, tela, nave, bullets)
      nave.update()
      bullets.update()
      gf.bullets_update(bullets)
      gf.update_aliens(ai_config,aliens)
      gf.update_tela(ai_config, tela, nave, aliens , bullets)



      
         
                 
         
run_game()        


