class game_stats():
    def __init__(self,ai_config):
        self.ai_config = ai_config
        self.reset_stats()
        self.game_active = False
        self.score = 0
    def reset_stats(self):
        #Iniccializa os  dados estasstiticos
       self.nave_left = self.ai_config.nave_limit

