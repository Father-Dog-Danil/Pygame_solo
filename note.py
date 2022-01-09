class Note:
    def __init__(self, x, y, hero, sound):
        self.x, self.y = x, y
        self.rect = (self.x, self.y, 50, 50)
        self.invent = False
        self.flag = 1
        self.sound = sound
        self.hero = hero

    def collide(self):
        if self.hero.does_collide(self.rect) and self.flag:
            self.flag = 0
            self.invent = True
            self.sound.play()
            self.x, self.y = 1500, 0
