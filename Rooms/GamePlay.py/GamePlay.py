from GameFrame import Level

class Gameplay (Level)
    def _init_(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")