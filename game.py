from direct.showbase.ShowBase import ShowBase
from hero import Hero
from mapmanager import Mapmanager


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        x, y = self.land.load_map('maps/land2.txt')
        self.hero = Hero((x//2, y//2, 1), self.land)
        base.camLens.setFov(90)

        start_snd = base.loader.loadSfx("sounds/inecraft_forest.ogg")
        start_snd.set_volume(0.1)
        start_snd.setLoop(True)
        start_snd.play()

        color = (.6, .64, .21)
        base.setBackgroundColor(Color)

game = Game()
game.run() 