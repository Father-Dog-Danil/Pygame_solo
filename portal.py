class Portal:
    def __init__(self, x, y, sprite, anime, anime_tp, npc, FPS):
        self.npc = npc
        self.sprite_list = sprite
        self.sprite_list_anime = anime
        self.list_anime_tp = anime_tp
        self.x, self.y = x, y
        self.rect = (self.x + 100, self.y + 100, 150, 150)
        self.count1 = 0
        self.count2 = 1
        self.sprite = sprite[0]
        self.flag1 = 1
        self.cof = int(FPS * 0.3)

    def render1(self):
        if self.count1 + 1 >= len(self.sprite_list_anime) * self.cof:
            self.npc.flag2 = 3
        self.sprite = self.sprite_list_anime[self.count1 // self.cof]
        self.count1 += 1

    def render2(self):
        if self.count1 >= len(self.sprite_list) * self.cof:
            self.count1 = 0
        self.sprite = self.sprite_list[self.count1 // self.cof]
        self.count1 += 1

    def render3(self):
        if self.count1 >= len(self.list_anime_tp) * self.cof:
            self.npc.flag2 = 5
            self.count1 = 5
        self.sprite = self.list_anime_tp[self.count1 // self.cof]
        self.count1 += 1