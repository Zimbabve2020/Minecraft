from direct.showbase.ShowBase import ShowBase

from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        base.camLens.setFov(90)
        self.land = Mapmanager()
        self.land.load_map('maps/land2.txt')

game = Game()
game.run() 