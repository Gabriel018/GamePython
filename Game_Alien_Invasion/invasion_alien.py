import sys
import pygame
from config_invasion import Config
from nave_invasion import Nave
import game_funcions as gf

def run_game():
        #Inicia o jogo e cria um ojeti
     pygame.init()

     ai_config = Config()
     tela = pygame.display.set_mode((ai_config.tela_with, ai_config.tela_heigth))
     #Cria a espaço nave
     nave = Nave(tela)
     pygame.display.set_caption("Invasao_alien")
      #inicia o laço de repetiçao do jogo
     while True:
         
      gf.check_eventos(nave)
      nave.update()
      gf.update_tela(ai_config, tela, nave)
         
                 
         
run_game()        


