import pickle



class Mapmanager:
    def __init__(self):
        self.model = "models/block"
        self.texture = "textures/stone.png"
        self.colors = [
            (0.40, 0.30, 0.0, 1),
            (0.7, 0.70, 0.90, 1),
            (0.4, 0.50, 0.0, 1),
            (0.35, 0.50, 0.12, 1)
        ] 

        self.start_new()
        
    def set_color(self, z):
        if z < len(self.colors):
            return self.colors[z]    
        else:
            return self.colors[-1]
    
    def add_block(self, position: tuple) -> None:
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setColor(self.set_color(position[2]))
        self.block.setPos(position)
        self.block.setTag('at', str(position))
        self.block.reparentTo(self.land)

    def del_block(self, pos):
        blocks = self.find_blocks(pos)
        for block in blocks:
            block.removeNode()

    def find_blocks(self, pos):
        return self.land.findAllMatches('=at=' + str(pos))

    def is_empty(self, pos):
        blokcs = self.find_blocks(pos)
        if blocks:
            return False
        else:
            return True

    def find_highest_empty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return(x, y, z)

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

    def load_map_from_file(self):
        self.clear()
        with open('maps/my_map.dat', 'rb') as map:
            lenght = pickle.load(map)
            for i in range(lenght):
                pos = pickle.load(map)
                self.add_block(pos)

def save_map(self):
    blocks = self.land.getChildren()
    with open('maps/my_map.dat', 'wb') as map:
        pickle.dump(len(blocks), map)
        for block in blocks:
            x, y, z = block.getPos()
            pos = (int(x), int(y), int(z))
            pickle.dump(pos, map)

                                                         