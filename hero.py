import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, speed, list1, size, walk, FPS):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = 55, 130
        self.x = size[0] // 2 - self.w // 2
        self.wall_x = 8
        self.y = size[1] // 2 - self.h // 2
        self.wall_y = 8
        self.image = pygame.Surface((self.w, self.h))
        self.image = list1[0]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.speed = speed
        self.size = size
        self.image_hero_list = list1
        self.image_hero_walk = walk
        self.count = 0
        self.cof = int(FPS * 0.1)

    def move(self, keys):
        if keys[pygame.K_s] and not self.y > self.size[1] - 140:
            self.y += self.speed
        elif keys[pygame.K_w] and not self.y < self.wall_y + 5:
            self.y -= self.speed
        if keys[pygame.K_d] and not self.x > self.size[0] - 65:
            self.x += self.speed
        elif keys[pygame.K_a] and not self.x < self.wall_x + 5:
            self.x -= self.speed
        self.image = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.render_walk()

    def move_boss(self, keys):
        if keys[pygame.K_s] and not self.y > self.size[1] - 140:
            self.y += self.speed
            return 2
        elif keys[pygame.K_w] and not self.y < self.wall_y + 5:
            self.y -= self.speed
            return 2
        if keys[pygame.K_d] and not self.x > self.size[0] - 65:
            self.image = pygame.Surface((self.w, self.h))
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.render_walk()
            return 1
        self.image = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.render_walk()
        return 0

    def render(self):
        if self.count >= len(self.image_hero_list) * self.cof:
            self.count = 0
        self.image = self.image_hero_list[self.count // self.cof]
        self.count += 1

    def render_walk(self):
        if self.count >= len(self.image_hero_list) * 15:
            self.count = 0
        self.image = self.image_hero_walk[self.count // 15]
        self.count += 1

    def does_collide_enemy(self, rect2):
        c = pygame.sprite.spritecollide(self, rect2, False)
        if c:
            return 1
        else:
            return 0

    def does_collide(self, rect2):
        self.rect2 = rect2
        self.rect1 = (self.x, self.y, self.w, self.h)
        if self.rect1[0] <= self.rect2[0] + self.rect2[2] and self.rect1[0] + self.rect1[2] >= self.rect2[0] \
                and self.rect1[1] <= self.rect2[1] + self.rect2[3] and self.rect1[3] + self.rect1[1] >= self.rect2[1]:
            return True
        else:
            return False

    def f(self):
        self.image = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.render_walk()