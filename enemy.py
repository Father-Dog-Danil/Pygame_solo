import pygame
from random import randint


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y, dist, speed, orientation, sprite_list, list1):
        self.sprite_list = sprite_list
        self.list = list1
        self.w, self.h = 70, 60
        super().__init__(self.list)
        self.orientation = orientation
        self.control_x = x
        self.control_y = y
        self.x = x
        self.y = y
        self.add(self.list)
        self.image = pygame.Surface((self.w, self.h))
        self.image = sprite_list[0]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.dist = dist
        self.speed = speed
        self.flag = 1
        self.count = 0
        self.flag1 = 1

    def update(self):
        self.move()
        self.render()

    def move(self):
        if self.orientation == 'x':
            if self.flag:
                if self.control_x + self.dist >= self.x:
                    self.x += self.speed
                else:
                    self.flag = 0
            else:
                if self.control_x <= self.x:
                    self.x -= self.speed
                else:
                    self.flag = 1
        elif self.orientation == 'y':
            if self.flag:
                if self.control_y + self.dist >= self.y:
                    self.y += self.speed
                else:
                    self.flag = 0
            else:
                if self.control_y <= self.y:
                    self.y -= self.speed
                else:
                    self.flag = 1
        self.image = pygame.Surface((self.w, self.h))
        self.image = self.image
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def render(self):
        if self.count >= len(self.sprite_list) * 2:
            self.flag1 = 0
        elif self.count <= 0:
            self.flag1 = 1
        if self.flag1:
            self.image = self.sprite_list[self.count // 2]
            self.count += 1
        else:
            self.count -= 1
            self.image = self.sprite_list[self.count // 2]


class Log1(pygame.sprite.Sprite):
    def __init__(self, x, y, dist, speed, sprite_list, list1):
        self.sprite_list = sprite_list
        self.list = list1
        self.w, self.h = 200, 70
        super().__init__(self.list)
        self.control_x = x
        self.control_y = y
        self.x = x
        self.y = y
        self.add(self.list)
        self.image = pygame.Surface((self.w, self.h))
        self.image = sprite_list[0]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.dist = dist
        self.speed = speed
        self.flag = 1
        self.count = 0
        self.flag1 = 1
        self.cof2 = 60

    def update(self):
        self.move()

    def move(self):
        self.image = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if self.flag:
            self.render1()
            if self.control_y + self.dist >= self.y:
                self.y += self.speed
            else:
                self.flag = 0
        else:
            self.render2()
            if self.control_y <= self.y:
                self.y -= self.speed
            else:
                self.flag = 1
        self.add(self.list)

    def render1(self):
        if self.count >= int(len(self.sprite_list) * self.cof2) or self.count < 0:
            self.count = 0
        self.flag1 = 0
        self.image = self.sprite_list[self.count // self.cof2]
        self.count += 1

    def render2(self):
        if self.count >= int(len(self.sprite_list) * self.cof2):
            self.count = 0
        self.flag1 = 0
        self.image = self.sprite_list[self.count // self.cof2]
        self.count -= 1


class Log2(pygame.sprite.Sprite):
    def __init__(self, x, y, dist, speed, sprite_list, list1):
        self.sprite_list = sprite_list
        self.list = list1
        self.w, self.h = 70, 200
        super().__init__(self.list)
        self.control_x = x
        self.control_y = y
        self.x = x
        self.y = y
        self.add(self.list)
        self.image = pygame.Surface((self.w, self.h))
        self.image = sprite_list[0]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.dist = dist
        self.speed = speed
        self.flag = 1
        self.count = 0
        self.flag1 = 1
        self.cof2 = 30

    def update(self):
        self.move()
        self.render()

    def move(self):
        if self.flag:
            if self.control_x + self.dist >= self.x:
                self.x += self.speed
            else:
                self.flag = 0
        else:
            self.x = - 55
            self.flag = 1
        self.add(self.list)
        self.image = pygame.Surface((self.w, self.h))
        self.image = self.image
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def render(self):
        if self.count >= int(len(self.sprite_list) * self.cof2):
            self.count = 0
        self.flag1 = 0
        self.image = self.sprite_list[self.count // self.cof2]
        self.count += 1


class Cockroach1(pygame.sprite.Sprite):
    def __init__(self, x, y, dist, speed, up, down, list1, sniffs_d, sniffs_u):
        self.up = up
        self.sniffs_d, self.sniffs_u = sniffs_d, sniffs_u
        self.down = down
        self.list = list1
        self.w, self.h = 70, 150
        super().__init__(self.list)
        self.control_x = x
        self.control_y = y
        self.x = x
        self.y = y
        self.add(self.list)
        self.image = pygame.Surface((self.w, self.h))
        self.image = down[0]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.dist = dist
        self.speed = speed
        self.flag = 1
        self.count = 0
        self.flag1 = 1
        self.cof1 = 10
        self.cof2 = 5
        self.time = 0
        self.count_time = 0

    def update(self, time):
        self.time = time
        self.move()

    def move(self):
        if self.count_time < self.time:
            if self.flag:
                if self.control_y + self.dist >= self.y:
                    self.y += self.speed
                else:
                    if self.count_time < self.time:
                        self.count_time = self.time + randint(0, 2000)
                    self.flag = 0
            else:
                if self.control_y <= self.y:
                    self.y -= self.speed
                else:
                    if self.count_time < self.time:
                        self.count_time = self.time + randint(0, 2000)
                    self.flag = 1
            self.render1()
        else:
            self.render2()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def render1(self):
        if self.flag:
            if self.count >= len(self.down) * self.cof1:
                self.count = 0
            self.image = self.down[self.count // self.cof1]
            self.count += 1
        else:
            if self.count >= len(self.up) * self.cof1:
                self.count = 0
            self.image = self.up[self.count // self.cof1]
            self.count += 1

    def render2(self):
        if self.flag:
            if self.count >= len(self.sniffs_d) * self.cof2:
                self.count = 0
            self.image = self.sniffs_d[self.count // self.cof2]
            self.count += 1
        else:
            if self.count >= len(self.sniffs_u) * self.cof2:
                self.count = 0
            self.image = self.sniffs_u[self.count // self.cof2]
            self.count += 1
