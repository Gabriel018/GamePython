


class Config():
    
    def __init__(self):
        #inicia a configuraçao do jogo
        #Configuraçao da tela
        self.tela_width = 1200
        self.tela_heigth = 600
        self.bg_color = (0, 0, 25)

        #configuraçoes do projetil
        self.bullet_width = 15
        self.bullet_heigth = 40
        self.bullet_color = (0,0,0)
        self.bullets_permitidas = 3

        #taxa de velocidade do jogo
        self.speed_scala = 1.2

        self.score_scala = 1.5


        self.frota_vel_drop = 10


        #Configuraçoes da Nave
        self.nave_limit = 3

        self.inicializa_config()

        self.alien_point  = 10

    def inicializa_config(self):
        # inicia as config que mudam no decorrer do jogo
        self.nave_velocidade = 1.0
        self.bullet_velocidade = 2.0
        self.alien_speed = 0.1
        self.frota_direction = 1

    def add_speed(self):
        # umenta a velocidade do jogo
        self.nave_velocidade  *=  self.speed_scala
        self.bullet_velocidade *= self.speed_scala
        self.alien_speed  *= self.speed_scala
        self.frota_direction *=self.speed_scala
        self.alien_point  = int(self.alien_point*self.score_scala)
        print(self.alien_point)
