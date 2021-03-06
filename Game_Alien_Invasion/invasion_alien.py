import sys
import pygame
from button import Button
from config_invasion import Config
from Game_Estatistic import game_stats
from nave_invasion import Nave
import game_funcions as gf
from pygame.sprite import Group
from alien import Alien
from score import ScoreBoard

def run_game():
        #Inicia o jogo e cria um objeto
     pygame.init()
     bullets = Group()
     aliens = Group()
     ai_config = Config()
     tela = pygame.display.set_mode((ai_config.tela_width,ai_config.tela_heigth))
     #Cria a espaço nave
     nave = Nave(ai_config, tela)
     stats = game_stats(ai_config)
     #cria o painel de pontos
     sc = ScoreBoard(ai_config,tela,stats)
     #cria a frota de aliens
     gf.create_aliens(ai_config,tela,nave,aliens)

     pygame.display.set_caption("Invasao_alien")
     play_button = Button(ai_config,tela,"Jogar")
      #inicia o laço de repetiçao do jogo
     while True:

        gf.check_eventos(ai_config,tela,stats,sc,nave,aliens,bullets,play_button)
        if stats.game_active:
          nave.update()
          bullets.update()
          gf.bullets_update(ai_config,tela,sc,stats,nave,aliens,bullets)
          gf.update_aliens(ai_config,stats,sc,tela,nave,aliens,bullets)
        gf.update_tela(ai_config, tela,stats,sc, nave, aliens, bullets,play_button,)

run_game()        


