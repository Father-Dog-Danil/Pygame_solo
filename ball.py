class Ball:
    def __init__(self, x, y, sound, hero):
        self.x, self.y = x, y
        self.rect = (self.x, self.y, 66, 30)
        self.sound_key = sound
        self.invent_ball = True
        self.flag = 1
        self.hero = hero

    def collide(self):
        if self.hero.does_collide(self.rect) and self.flag:
            self.flag = 0
            self.invent_ball = False
            self.sound_key.play()