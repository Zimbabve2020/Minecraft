from time import time

class Hero:
    def __init__(self, pos, land):
        self.camera_on = None
        self.mode = True
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor((0.2, 0.2, 0.3, 1))
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)

        self.camera_bind()
        self.accept_events()

        self.damage_snd = base.loader.loadSfx("sounds/inecraft_damage.ogg")
        self.up_snd = base.loader.loadSfx("sounds/up.mp3")

        self.last_move_sound_time = 0
        self.move_sound_delay = 0.3
        self.mode_snd = base.loader.loadSfx("sounds/step.ogg")

    def camera_bind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        base.camera.setH(180)
        self.camera_on = True

    def camera_up(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_on = False

    def switch_cam(self):
        if self.camera_on:
            self.camera_up()
        else:
            self.camera_bind()
        start_snd = base.loader.loadSfx("sounds/change_mode.ogg")
        start_snd = set.volume(0.5)
        start_snd.setLoop(False)
        start_snd.play()
    
    def turn_right(self):
        self.hero.setH((self.hero.getH() + 5) % 360)


    def turn_left(self):    
        self.hero.setH((self.hero.getH() - 5) % 360)

    def change_mode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

def try_move(self, angle):
    pos = self.look_at(angle)
    if self.land.is_empty(pos):
        pos = self.land.find_highest_empty(pos)
        self.hero.setPos(pos)
    else:
        pos = pos[0], pos[1], pos[2] + 1
        if self.land.is_empty(pos):
            self.up_snd.play()  
            self.hero.setPos(pos)
        else:
            self.damage_snd.play()

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)   

        current_time = time()
        if current_time - self.last_move_sound_time > self.move_sound_delay:
            self.move_snd.set_volume(0.5)
            self.move_snd.setLoop(False)
            self.move_snd.play()
            self.last_move_sound_time = current_time

    def check_dir(self, angle):
        if 0 <= angle <= 20:
            return 0, -1
        elif angle <= 65:
            return 1, -1
        elif angle <= 110:
            return 1, 0
        elif angle <= 155:
            return 1, 1
        elif angle <= 200:
            return 0, 1
        elif angle <= 245:
            return -1, 1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() - 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() - 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def up(self):
        self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.add_block(pos)
        else:
            self.land.build_block(pos)
        start_snd = base.loader.loadSfx("sounds/build.ogg")
        start_snd.set_volume(0.5)
        start_snd.play()

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.del_block(pos)
        else:
            self.land.del_block_from(pos)
        start_snd = base.loader.loadSfx("sounds/break.ogg")
        start_snd.set_volume(0.5)
        start_snd.play()

    def accept_events(self):
        base.accept('c', self.switch_cam)
        base.accept('d', self.turn_left)
        base.accept('d' + '-repeat', self.turn_left)
        base.accept('a', self.turn_right)
        base.accept('a' + '-repeat', self.turn_right)
        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)
        base.accept('s', self.back)
        base.accept('s' + '-repeat', self.back)
        base.accept('m', self.left)
        base.accept('m' + '-repeat', self.left)
        base.accept('n', self.right)
        base.accept('n' + '-repeat', self.right)
        base.accept('e', self.up)
        base.accept('e' + '-repeat', self.up)
        base.accept('q', self.down)
        base.accept('q' + '-repeat', self.down)
        base.accept('z', self.change_mode)
        base.accept("b", self.build)
        base.accept("m", self.destroy)
        base.accept("p", self.load_map_from_file)
        base.accept("o", self.save_map)




