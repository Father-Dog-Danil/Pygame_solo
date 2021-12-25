import sys
import pygame

pygame.init()


class Key:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.rect = (self.x, self.y, 66, 30)
        self.sound_key = pygame.mixer.Sound('data/SOUNDS/KEY2.mp3')
        self.key_invent = True

    def collide(self):
        if hero.does_collide(self.rect):
            self.key_invent = False
            self.sound_key.play()
            self.x, self.y = 1200, 10


class Door:
    def __init__(self, x, y, sprite_list, orient):
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
        if hero.does_collide(self.rect):
            return 1
        else:
            return 0


class Hero:
    def __init__(self, speed, list, size):
        self.speed = speed
        self.size = size
        self.image_hero_list = list
        self.count = 0
        self.x_hero = self.wall_x = 8
        self.y_hero = self.wall_y = 8
        self.rect1 = (self.x_hero - 5, self.y_hero - 10, 60, 150)
        self.cof = int(FPS * 0.3)

    def move(self, keys):
        if keys[pygame.K_s] and not hero.y_hero > self.size[1] - 135:
            self.y_hero += self.speed
        elif keys[pygame.K_w] and not hero.y_hero < self.wall_y + 5:
            self.y_hero -= self.speed
        if keys[pygame.K_d] and not hero.x_hero > self.size[0] - 60:
            self.x_hero += self.speed
        elif keys[pygame.K_a] and not hero.x_hero < self.wall_x + 5:
            self.x_hero -= self.speed
        self.rect1 = (self.x_hero, self.y_hero, 55, 129)

    def render(self):
        if self.count >= len(self.image_hero_list) * self.cof:
            self.count = 0
        self.image_hero = self.image_hero_list[self.count // self.cof]
        self.count += 1

    def does_collide(self, rect2):
        self.rect2 = rect2
        self.rect1 = (self.x_hero, self.y_hero, 55, 129)
        if self.rect1[0] <= self.rect2[0] + self.rect2[2] and self.rect1[0] + self.rect1[2] >= self.rect2[0] \
                and self.rect1[1] <= self.rect2[1] + self.rect2[3] and self.rect1[3] + self.rect1[1] >= self.rect2[1]:
            return True
        else:
            return False


class Enemy:
    def __init__(self, x, y, dist, speed, orientation, sprite_list, flag=0):
        self.sprite_list = sprite_list
        if self.sprite_list == red_enemy_list:
            self.w, self.h = 80, 80
        elif self.sprite_list == log_enemy_list:
            self.w, self.h = 200, 70
        elif self.sprite_list == log_enemy_list_y:
            self.w, self.h = 70, 200
        self.orientation = orientation
        self.control_x = x
        self.control_y = y
        self.x = x
        self.y = y
        self.dist = dist
        self.speed = speed
        self.flag = 1
        self.flag2 = flag
        self.count = 0
        self.image_enemy = self.sprite_list[0]
        self.rect = (self.x, self.y, self.w, self.h)
        self.cof = int(FPS * 0.08)
        self.flag1 = 1
        self.cof2 = int(FPS * 0.3)

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

    def move_tp(self):
        if self.orientation == 'x':
            if self.flag:
                if self.control_x + self.dist >= self.x:
                    self.x += self.speed
                else:
                    self.flag = 0
            else:
                self.x = - 55
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

        if self.count >= len(self.sprite_list) * 2:
            self.flag1 = 0
        elif self.count <= 0:
            self.flag1 = 1
        if self.flag1:
            self.image_enemy = self.sprite_list[self.count // 2]
            self.count += 1
        else:
            self.count -= 1
            self.image_enemy = self.sprite_list[self.count // 2]


    def render_log(self):
        if self.count >= int(len(self.sprite_list) * self.cof2):
            self.flag1 = 0
        elif self.count <= 0:
            self.flag1 = 1
        if self.flag1:
            self.image_enemy = self.sprite_list[self.count // self.cof2]
            self.count += 1
        else:
            self.count -= 1
            self.image_enemy = self.sprite_list[self.count // self.cof2]

    def does_collide(self):
        self.rect = (self.x, self.y, self.w, self.h)
        if hero.does_collide(self.rect):
            return 1
        else:
            return 0


class Nps:
    def __init__(self, x, y, sprite, spr, d):
        self.cof = int(FPS * 0.2)
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
            self.flag2 = 3

    def render2(self):
        if self.count1 >= len(self.sprite_anime) * self.cof:
            self.count1 = 0
        self.sprite = self.sprite_anime[self.count1 // self.cof]
        self.count1 += 1


class Torch:
    def __init__(self, x, y, sprite):
        self.sprite_list = sprite
        self.x, self.y = x, y
        self.sprite = sprite[0]
        self.count = 0
        self.cof = int(FPS * 0.5)

    def render(self):
        if self.count >= len(self.sprite_list) * self.cof:
            self.count = 0
        self.sprite = self.sprite_list[self.count // self.cof]
        self.count += 1


class Portal:
    def __init__(self, x, y, sprite):
        self.sprite_list = sprite
        self.x, self.y = x, y
        self.rect = (self.x, self.y, 160, 160)
        self.count1 = 0
        self.count2 = 1
        self.sprite = sprite[0]
        self.flag1 = 1
        self.cof = int(FPS * 0.8)

    def render(self):
        if self.count1 >= len(self.sprite_list) * self.cof:
            self.count1 = 0
        self.sprite = self.sprite_list[self.count1 // self.cof]
        self.count1 += 1


pygame.mixer.music.load('data/SOUNDS/sound_bg1.ogg')
pygame.mixer.music.set_volume(0.1)
sound_win_level = pygame.mixer.Sound('data/SOUNDS/WIN_LEVEL.mp3')
sound_damage = pygame.mixer.Sound('data/SOUNDS/DAMAGE.mp3')
pygame.mixer.music.play(-1)

size = (1280, 720)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

red_enemy_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED7.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED8.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED9.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED10.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED11.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED12.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/RED13.png')]

log_enemy_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/log1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/log2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/log3.png')]

log_enemy_list_y = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/log_y1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/log_y2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_ENEMY/log_y3.png')]

heart_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HEART4.png')]

padlock = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PADLOCK.png')
bg = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/MAP2.png').convert()
bg_house = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HOUSE1.png').convert()
bg_house_shadow = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/HOUSE2.png')
key_sprite = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/KEY.png')

passage_list = [pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR1.png'),
                pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR2.png'),
                pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR3.png'),
                pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/DOOR4.png')]

npc_list1 = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC6.png')]

npc_anime_list1 = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME7.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME8.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/NPC_ANIME9.png')
]

torch_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH5.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH6.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH7.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/TORCH4.png')]

portal_list = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL5.png')]

portal_list_anime = [
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME1.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME2.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME3.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME4.png'),
    pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/PORTAL_ANIME5.png')]

hero_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus3.png')]

hp_count = 0
FPS = 200
hero = Hero(450 / FPS, hero_list, size)
clock = pygame.time.Clock()
speed_red = 210 / FPS
run = 1
mushroom_w = 70
red1 = Enemy(size[0] // 4, size[1] // 2, size[1] // 2 - mushroom_w, speed_red, 'y', red_enemy_list)
red2 = Enemy(0, size[1] // 2, 1220, speed_red * 2, 'x', red_enemy_list)
red3 = Enemy(size[0] // 2, 0, size[1] // 2 - mushroom_w, speed_red, 'y', red_enemy_list)
red4 = Enemy(size[0] // 2, size[1] // 2, size[1] // 2 - mushroom_w, speed_red, 'y', red_enemy_list)
red5 = Enemy(size[0] - size[0] // 4, 0, size[1] - mushroom_w, speed_red * 2, 'y', red_enemy_list)
torch1 = Torch(size[0] // 2 - 40, size[1] // 2 - 120, torch_list)
portal1 = Portal(100, 100, portal_list)
speed_log = 150 / FPS
speed_log2 = 300 / FPS
coridor_log = 300
log1 = Enemy(size[0] - 205 * 1, 0, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log2 = Enemy(size[0] - 205 * 2, 0, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log3 = Enemy(size[0] - 205 * 3, 0, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log4 = Enemy(size[0] - 205 * 4, 0, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log5 = Enemy(size[0] - 205 * 5, 0, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)

log6 = Enemy(size[0] - 205 * 1, coridor_log, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log7 = Enemy(size[0] - 205 * 2, coridor_log, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log8 = Enemy(size[0] - 205 * 3, coridor_log, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log9 = Enemy(size[0] - 205 * 4, coridor_log, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)
log10 = Enemy(size[0] - 205 * 5, coridor_log, size[1] - coridor_log - 55, speed_log, 'y', log_enemy_list)

log11 = Enemy(-400, 15 + 200 * 0, size[0] + 460, speed_log2, 'x', log_enemy_list_y, 1)
log12 = Enemy(-950, 15 + 245 * 1, size[0] + 1010, speed_log2, 'x', log_enemy_list_y, 1)
log13 = Enemy(-400, 15 + 245 * 2, size[0] + 460, speed_log2, 'x', log_enemy_list_y, 1)

log14 = Enemy(-1400, 15 + 200 * 0, size[0] + 1460, speed_log2, 'x', log_enemy_list_y, 1)
log15 = Enemy(-1400, 15 + 245 * 2, size[0] + 1460, speed_log2, 'x', log_enemy_list_y, 1)
log16 = Enemy(-1600, 15 + 245 * 1, size[0] + 1660, speed_log2, 'x', log_enemy_list_y, 1)

list_red_room1 = [red1, red2, red3, red4, red5]
list_log_room2 = [log1, log2, log3, log4, log5, log6, log7, log8, log9, log10]
list_log_room3 = [log11, log12, log13, log14, log15, log16]
hp = heart_list[hp_count]
timer = 0
font = pygame.font.Font(None, 68)
font2 = pygame.font.Font(None, 30)
key1 = Key(30, size[1] - 100)
damage = 1
key2 = Key(size[0] - 100, size[1] - 160)
door1 = Door(size[0] - 15, size[1] // 2 - 85, passage_list, 'y')
door2 = Door(0, size[1] // 2 - 85, passage_list, 'y')
door3 = Door(size[0] // 2 - 174 // 2, 0, passage_list, 'x')
door4 = Door(size[0] - 15, size[1] // 2 - 85, passage_list, 'y')
door5 = Door(0, size[1] // 2 - 85, passage_list, 'y')
dialog = ['О! пришёл!', 'кто я такой?', 'не могу сказать...', 'они уже близко,', 'прыгай в телепорт!']
npc = Nps(size[0] - 200, size[1] // 2 - 50, npc_list1, npc_anime_list1, dialog)
time_count = pygame.time.get_ticks()

text = font.render(str(time_count // 1000 // 60) + ':' + str(time_count // 1000 % 60), True, (255, 255, 255))
event = 0
flag_time = 0


def room1():
    global run, time_count, text, event, timer, hp_count, hp
    run = 1
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
                hp_count += damage
                hp = heart_list[hp_count]
                sound_damage.play()
            if hp_count == 3:
                sys.exit()
        if door1.collide():
            run = 0
            hero.x_hero, hero.y_hero = 60, size[1] // 2 - 85
            room2()
        screen.blit(bg, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door1.sprite, (door1.x, door1.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        for i in list_red_room1:
            i.render()
            i.move()
            screen.blit(i.image_enemy, (i.x, i.y))
        screen.blit(hero.image_hero, (hero.x_hero, hero.y_hero))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room2():
    global run, time_count, text, event, timer, hp_count, hp
    run = 1
    while run:
        time_count = pygame.time.get_ticks()
        text = font.render(str(time_count // 1000 // 60) + ':' + str(time_count // 1000 % 60), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = 0
            elif event.type == pygame.QUIT:
                sys.exit()
        hero.render()
        if hp_count < 3 and timer < time_count:
            timer = time_count + 500
            if log1.does_collide() or log2.does_collide() or log3.does_collide() \
                    or log4.does_collide() or log5.does_collide() or log6.does_collide() \
                    or log7.does_collide() or log8.does_collide() or log9.does_collide() or log10.does_collide():
                hp_count += damage
                hp = heart_list[hp_count]
                sound_damage.play()
            if hp_count == 3:
                sys.exit()
        if door4.collide():
            run = 0
            room3()
        if not key2.key_invent:
            if door3.collide():
                run = 0
                room4()
        if door2.collide():
            run = 0
            hero.x_hero, hero.y_hero = size[0] - 100, size[1] // 2 - 85
            room1()
        screen.blit(bg, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door2.sprite, (door2.x, door2.y))
        screen.blit(door3.sprite, (door3.x, door3.y))
        screen.blit(door4.sprite, (door4.x, door4.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        screen.blit(hero.image_hero, (hero.x_hero, hero.y_hero))
        log1.render_log()
        for i in list_log_room2:
            i.move()
            screen.blit(log1.image_enemy, (i.x, i.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room3():
    hero.x_hero, hero.y_hero = 60, size[1] // 2 - 85
    global run, time_count, text, event, timer, hp_count, hp
    run = 1
    while run:
        time_count = pygame.time.get_ticks()
        text = font.render(str(time_count // 1000 // 60) + ':' + str(time_count // 1000 % 60), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = 0
            elif event.type == pygame.QUIT:
                sys.exit()
        hero.render()
        if hp_count < 3 and timer < time_count:
            timer = time_count + 500
            if log11.does_collide() or log12.does_collide() or log13.does_collide() \
                    or log14.does_collide() or log15.does_collide() or log16.does_collide():
                hp_count += damage
                hp = heart_list[hp_count]
                sound_damage.play()
            if hp_count == 3:
                sys.exit()
        screen.blit(bg, (0, 0))
        screen.blit(text, (150, 10))
        if door5.collide():
            run = 0
            hero.x_hero, hero.y_hero = size[0] - 100, size[1] // 2 - 85
            room2()
        screen.blit(door3.sprite, (door3.x, door3.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        screen.blit(hero.image_hero, (hero.x_hero, hero.y_hero))
        for i in list_log_room3:
            i.move_tp()
            i.render_log()
            screen.blit(i.image_enemy, (i.x, i.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        key2.collide()
        screen.blit(key_sprite, (key2.x, key2.y))
        clock.tick(FPS)
        pygame.display.update()


def room4():
    global run, time_count, text, event, timer, hp_count, hp
    run = 1
    while run:
        time_count = pygame.time.get_ticks()
        text = font.render(str(time_count // 1000 // 60) + ':' + str(time_count // 1000 % 60), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    npc.dialog()
            elif event.type == pygame.QUIT:
                sys.exit()
        hero.render()
        torch1.render()
        portal1.render()
        text_d = font2.render(npc.text, True, (255, 255, 255))
        screen.blit(bg_house, (0, 0))
        screen.blit(text, (150, 10))
        keys = pygame.key.get_pressed()

        if npc.flag2:
            if npc.flag2 == 3:
                screen.blit(portal1.sprite, (portal1.x, portal1.y))
                if hero.does_collide(portal1.rect):
                    sys.exit()
            if 1 in keys:
                hero.move(keys)
        screen.blit(hp, (10, 10))
        if hero.y_hero + 130 < npc.y + 180:
            screen.blit(hero.image_hero, (hero.x_hero, hero.y_hero))
            screen.blit(npc.sprite, (npc.x, npc.y))
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
        elif hero.y_hero + 130 > npc.y + 180 < torch1.y + 240:
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
            screen.blit(hero.image_hero, (hero.x_hero, hero.y_hero))
            screen.blit(npc.sprite, (npc.x, npc.y))
        else:
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
            screen.blit(npc.sprite, (npc.x, npc.y))
            screen.blit(hero.image_hero, (hero.x_hero, hero.y_hero))

        if npc.flag1:
            if abs(hero.y_hero - npc.y) < 100 and abs(hero.x_hero - npc.x) < 100:
                npc.render1()
        else:
            npc.render2()
        if npc.count1 > 0:
            screen.blit(text_d, (npc.x - len(npc.text), npc.y - 30))
        clock.tick(FPS)
        pygame.display.set_caption(f'{clock.get_fps()}')
        pygame.display.update()


room1()
