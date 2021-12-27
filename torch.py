class Torch:
    def __init__(self, x, y, sprite):
        self.sprite_list = sprite
        self.x, self.y = x, y
        self.sprite = sprite[0]
        self.count = 0
        self.cof = int(100)

    def render(self):
        if self.count >= len(self.sprite_list) * self.cof:
            self.count = 0
        self.sprite = self.sprite_list[self.count // self.cof]
        self.count += 1