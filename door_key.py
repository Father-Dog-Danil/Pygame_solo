class Key:
    def __init__(self, x, y, sound, hero):
        self.x, self.y = x, y
        self.rect = (self.x, self.y, 66, 30)
        self.sound_key = sound
        self.key_invent = True
        self.flag = 1
        self.hero = hero

    def collide(self):
        if self.hero.does_collide(self.rect) and self.flag:
            self.flag = 0
            self.key_invent = False
            self.sound_key.play()
            self.x, self.y = 1100, 15


class Door:
    def __init__(self, x, y, sprite_list, orient, hero):
        self.hero = hero
        self.x, self.y = x, y
        self.sprite_list = sprite_list
        if orient == 'y':
            self.c = 0
            self.rect = (self.x, self.y, 50, 150)
        elif orient == 'x':
            self.c = 2
            self.rect = (self.x, self.y, 150, 50)
        self.sprite = self.sprite_list[self.c]

    def collide(self):
        self.sprite = self.sprite_list[self.c + 1]
        if self.hero.does_collide(self.rect):
            return 1
        else:
            return 0
