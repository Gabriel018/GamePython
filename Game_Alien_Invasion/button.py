import pygame.font

class Button():

    def __init__(self,ai_config,tela,msg):
        #inicia o botao
        self.tela = tela
        self.tela_rect = tela.get_rect()

        #Define as dimençoes do Botao
        self.width, self.height = 200,50
        self.button_color = (255,255,0)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,38)

        #Constroi o objeto Rect

        self.rect = pygame.Rect(0,0 , self.width,self.height)
        self.rect.center = self.tela_rect.center
        self.prep_msg(msg)

    def prep_msg(self,msg):
        #Transforma msg em imagem renderizada e centraliza o texto do botao

        self.msg_image = self.font.render(msg,True,self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #desenha o button na tela
        self.tela.fill(self.button_color,self.rect)
        self.tela.blit(self.msg_image,self.msg_image_rect)
