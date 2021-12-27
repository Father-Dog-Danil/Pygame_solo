class Npc:
    def __init__(self, x, y, sprite, spr, d):
        self.cof = 25
        self.sprite_list = sprite
        self.sprite_anime = spr
        self.d_list = d
        self.x, self.y = x, y
        self.count1 = 0
        self.count2 = 1
        self.sprite = sprite[0]
        self.flag1 = 1
        self.flag2 = 1
        self.text = self.d_list[0]

    def render1(self):
        if self.count1 < len(self.sprite_list) * self.cof:
            self.sprite = self.sprite_list[self.count1 // self.cof]
            self.count1 += 1
            self.flag2 = 0
        else:
            self.flag1 = 0

    def dialog(self):
        if self.count2 < len(self.d_list):
            self.text = self.d_list[self.count2]
            self.count2 += 1
        else:
            self.flag2 = 2

    def render2(self):
        if self.count1 >= len(self.sprite_anime) * self.cof:
            self.count1 = 0
        self.sprite = self.sprite_anime[self.count1 // self.cof]
        self.count1 += 1