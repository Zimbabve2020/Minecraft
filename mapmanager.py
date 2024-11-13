
class Mapmanager:
    def __init__(self):
        self.model = "models/block"
        self.texture = "textures/stone.png"
        self.color = (196, 226, 223, 0.8) 

        self.start_new()
        self.add_block((1, 1, 1))
        self.add_block((1, 1, 2      ))
    
    def add_block(self, position: tuple) -> None:
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setColor(self.color)
        self.block.setPos(position)
        self.block.reparentTo(self.land)

    def start_new(self):
        self.land = render.attachNewNode('Land')   

    def load_map(self, filename: str):   
        with open(filename, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line_lst = line.split(' ')
                for z in line_lst:
                    for i in range(int(z) + 1):
                        self.add_block((x, y, i))
                    x += 1
                y += 1
            return x, y
                                                         