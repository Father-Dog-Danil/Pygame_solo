import sys
import pygame
pygame.init()


class Key:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.rect = (self.x, self.y, 66, 30)
        self.sound_key = pygame.mixer.Sound('../SOUNDS/KEY2.mp3')
        self.key_invent = False

    def collide(self):
        if hero.does_collide(self.rect):
            self.key_invent = True
            self.sound_key.play()
            self.x, self.y = 1200, 10


class Door:
    def __init__(self, x, y, sprite_list):
        self.sprite_list = sprite_list
        self.sprite = self.sprite_list[0]
        self.x, self.y = x, y
        self.rect = (self.x, self.y, 50, 150)

    def collide(self):
        self.sprite = self.sprite_list[1]
        if hero.does_collide(self.rect):
            sys.exit()


class Hero:
    def __init__(self):
        self.speed = 15
        self.image_hero_list = [
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus1.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus2.png'),
            pygame.image.load('../IMAGE_GAME/IMAGE_HERO_D/anonimus3.png')]
        self.count = 0
        self.x_hero = self.wall_x = 8
        self.y_hero = self.wall_y = 8
        self.rect1 = (self.x_hero - 5, self.y_hero - 10, 60, 150)
    def move(self, keys):
        if keys[pygame.K_SPACE]:
            sys.exit()
        if keys[pygame.K_s] and a.walls('down'):
            self.y_hero += self.speed
        elif keys[pygame.K_w] and a.walls('up'):
            self.y_hero -= self.speed
        if keys[pygame.K_d] and a.walls('right'):
            self.x_hero += self.speed
        elif keys[pygame.K_a] and a.walls('left'):
            self.x_hero -= self.speed
        self.rect1 = (self.x_hero, self.y_hero, 55, 129)
    def render(self):
        if self.count >= 12:
            self.count = 0
        self.image_hero = self.image_hero_list[self.count // 4]
        self.count += 1
    def does_collide(self, rect2):
        self.rect2 = rect2
        if self.rect1[0] <= self.rect2[0] + self.rect2[2] and self.rect1[0] + self.rect1[2] >= self.rect2[0] \
                and self.rect1[1] <= self.rect2[1] + self.rect2[3] and self.rect1[3] + self.rect1[1] >= self.rect2[1]:
            return True
        else:
            return False
class Game:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen
        self.x_hero = self.wall_x = 8
        self.y_hero = self.wall_y = 8

    def walls(self, arg):
        if arg == 'up':
            if hero.y_hero < self.wall_y + 5:
                return 0
            else:
                return 1
        elif arg == 'down':
            if hero.y_hero > self.size[1] - 135:
                return 0
            else:
                return 1
        if arg == 'left':
            if hero.x_hero < self.wall_x + 5:
                return 0
            else:
                return 1
        elif arg == 'right':
            if hero.x_hero > self.size[0] - 60:
                return 0
            else:
                return 1


class Enemy:
    def __init__(self, x, y, dist, speed, orientation, sprite_list):
        self.sprite_list = sprite_list
        self.orientation = orientation
        self.control_x = x
        self.control_y = y
        self.x = x
        self.y = y
        self.dist = dist
        self.speed = speed
        self.flag = 1
        self.count = 0
        self.image_enemy = self.sprite_list[0]

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

    def render(self):
        if self.count >= 16:
            self.count = 0
        self.image_enemy = self.sprite_list[self.count // 4]
        self.count += 1


    def does_collide(self):
        self.rect1 = (self.x, self.y, 50, 50)
        self.rect2 = (hero.x_hero, hero.y_hero, 55, 129)
        if self.rect1[0] <= self.rect2[0] + self.rect2[2] and self.rect1[0] + self.rect1[2] >= self.rect2[0] \
                and self.rect1[1] <= self.rect2[1] + self.rect2[3] and self.rect1[3] + self.rect1[1] >= self.rect2[1]:
            return True
        else:
            return False

pygame.init()
pygame.mixer.music.load('../SOUNDS/sound_bg1.ogg')
pygame.mixer.music.set_volume(0.1)
sound_win_level = pygame.mixer.Sound('../SOUNDS/WIN_LEVEL.mp3')
sound_damage = pygame.mixer.Sound('../SOUNDS/DAMAGE.mp3')
pygame.mixer.music.play(-1)

size = (1280, 720)
screen = pygame.display.set_mode(size)
enemy_list = [
    pygame.image.load('../IMAGE_GAME/IMAGE_ENEMY/RED1.png'),
    pygame.image.load('../IMAGE_GAME/IMAGE_ENEMY/RED2.png'),
    pygame.image.load('../IMAGE_GAME/IMAGE_ENEMY/RED3.png'),
    pygame.image.load('../IMAGE_GAME/IMAGE_ENEMY/RED4.png')]
heart_list = [
    pygame.image.load('../IMAGE_GAME/IMAGE_MAP/HEART1.png'),
    pygame.image.load('../IMAGE_GAME/IMAGE_MAP/HEART2.png'),
    pygame.image.load('../IMAGE_GAME/IMAGE_MAP/HEART3.png'),
    pygame.image.load('../IMAGE_GAME/IMAGE_MAP/HEART4.png')]
padlock = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/PADLOCK.png')
bg = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/MAP1.png')
key_sprite = pygame.image.load('../IMAGE_GAME/IMAGE_MAP/KEY.png')
passage_list = [pygame.image.load('../IMAGE_GAME/IMAGE_MAP/DOOR1.png'),
                (pygame.image.load('../IMAGE_GAME/IMAGE_MAP/DOOR2.png'))]
hp_count = 0
a = Game(size, screen)
hero = Hero()
clock = pygame.time.Clock()
run = 1
red1 = Enemy(size[0] // 4, size[1] // 2, size[1] // 2 - 55, 5, 'y', enemy_list)
red2 = Enemy(0, size[1] // 2, 1220, 10, 'x', enemy_list)
red3 = Enemy(size[0] // 2, 0, size[1] // 2 - 55, 5, 'y', enemy_list)
red4 = Enemy(size[0] // 2, size[1] // 2, size[1] // 2 - 55, 5, 'y', enemy_list)
red5 = Enemy(size[0] - size[0] // 4, 0, size[1] - 55, 15, 'y', enemy_list)
list_red = [red1, red2, red3, red4, red5]
hp = heart_list[hp_count]
timer = 0
font = pygame.font.Font(None, 68)
key = Key(600, 300)
door = Door(size[0] - 15, size[1] // 2 - 85, passage_list)
while run:
    time_count = pygame.time.get_ticks()
    text = font.render(str(time_count // 1000 // 60) + ':' + str(time_count // 1000 % 60), True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = 0
        elif event.type == pygame.QUIT:
            run = 0
    hero.render()
    if hp_count < 3 and timer < time_count:
        timer = time_count + 500
        if red1.does_collide() or red2.does_collide() or red3.does_collide() or red3.does_collide() \
                or red4.does_collide() or red5.does_collide():
            hp_count += 1
            hp = heart_list[hp_count]
            sound_damage.play()
        if hp_count == 3:
            run = 0
    if not key.key_invent:
        key.collide()
    else:
        door.collide()
    screen.blit(bg, (0, 0))
    screen.blit(text, (150, 10))
    screen.blit(key_sprite, (key.x, key.y))
    screen.blit(door.sprite, (door.x, door.y))
    keys = pygame.key.get_pressed()
    if 1 in keys:
        hero.move(keys)
    screen.blit(hp, (10, 10))
    for i in list_red:
        i.move()
        i.render()
        screen.blit(i.image_enemy, (i.x, i.y))
    screen.blit(hero.image_hero, (hero.x_hero, hero.y_hero))
    pygame.display.set_caption(f'{clock.get_fps()}')
    clock.tick(30)
    pygame.display.update()