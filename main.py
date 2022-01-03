from menu import *
import pygame
from setting import *


screen = pygame.display.set_mode(size, mode)
l = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/loading.png')
screen.blit(l, (0, 0))
pygame.display.update()

import sys
from door_key import Key, Door
from random import randint
from hero import Hero
from enemy import Mushroom, Log1, Log2, Cockroach1
from NPC import Npc
from torch import Torch
from sprite import *
from lose import Lose
pygame.init()


class Portal:
    def __init__(self, x, y, sprite, anime, anime_tp):
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
            npc.flag2 = 3
        self.sprite = self.sprite_list_anime[self.count1 // self.cof]
        self.count1 += 1

    def render2(self):
        if self.count1 >= len(self.sprite_list) * self.cof:
            self.count1 = 0
        self.sprite = self.sprite_list[self.count1 // self.cof]
        self.count1 += 1

    def render3(self):
        if self.count1 >= len(self.list_anime_tp) * self.cof:
            npc.flag2 = 5
            self.count1 = 5
        self.sprite = self.list_anime_tp[self.count1 // self.cof]
        self.count1 += 1

pygame.mixer.music.load('data/SOUNDS/bg.mp3')
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)
sound_win_level = pygame.mixer.Sound('data/SOUNDS/WIN_LEVEL.mp3')
sound_tp = pygame.mixer.Sound('data/SOUNDS/tp.mp3')
sound_damage = pygame.mixer.Sound('data/SOUNDS/DAMAGE.mp3')
all_sprites = pygame.sprite.Group()
sound_tp.set_volume(volume)
sound_damage.set_volume(volume)

hp_count = 0
hero = Hero(speed_hero, hero_list, size, hero_walk_list, FPS)
clock = pygame.time.Clock()
run = 1
mushroom_w = 70

list_mushroom_room1 = pygame.sprite.Group()
list_log_room2 = pygame.sprite.Group()
list_log_room3 = pygame.sprite.Group()
list_log_room4 = pygame.sprite.Group()
list_log_room5 = pygame.sprite.Group()
list_log_room6 = pygame.sprite.Group()

mushroom1 = Mushroom(size[0] // 4, size[1] // 2, size[1] // 2 - mushroom_w, speed_mushroom, 'y', mushroom_enemy_list,
                     list_mushroom_room1)
mushroom2 = Mushroom(0, size[1] // 2, 1220, speed_mushroom * 2, 'x', mushroom_enemy_list, list_mushroom_room1)
mushroom3 = Mushroom(size[0] // 2, 0, size[1] // 2 - mushroom_w, speed_mushroom, 'y', mushroom_enemy_list,
                     list_mushroom_room1)
mushroom4 = Mushroom(size[0] // 2, size[1] // 2, size[1] // 2 - mushroom_w, speed_mushroom, 'y', mushroom_enemy_list,
                     list_mushroom_room1)
mushroom5 = Mushroom(size[0] - size[0] // 4, 0, size[1] - mushroom_w, speed_mushroom * 2, 'y', mushroom_enemy_list,
                     list_mushroom_room1)
torch1 = Torch(size[0] // 2 - 40, size[1] // 2 - 120, torch_list)
portal1 = Portal(0, 0, portal_list, portal_list_anime, portal_tp_list)
coridor_log = 300

log1 = Log1(size[0] - 205 * 1, 0, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log2 = Log1(size[0] - 205 * 2, 0, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log3 = Log1(size[0] - 205 * 3, 0, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log4 = Log1(size[0] - 205 * 4, 0, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log5 = Log1(size[0] - 205 * 5, 0, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)

log6 = Log1(size[0] - 205 * 1, coridor_log, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log7 = Log1(size[0] - 205 * 2, coridor_log, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log8 = Log1(size[0] - 205 * 3, coridor_log, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log9 = Log1(size[0] - 205 * 4, coridor_log, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)
log10 = Log1(size[0] - 205 * 5, coridor_log, size[1] - coridor_log - 55, speed_log, log_enemy_list, list_log_room2)

log11 = Log2(-400, 15 + 200 * 0, size[0] + 460, speed_log2, log_enemy_list_y, list_log_room3)
log12 = Log2(-950, 15 + 245 * 1, size[0] + 1010, speed_log2, log_enemy_list_y, list_log_room3)
log13 = Log2(-400, 15 + 245 * 2, size[0] + 460, speed_log2, log_enemy_list_y, list_log_room3)

log14 = Log2(-1400, 15 + 200 * 0, size[0] + 1460, speed_log2, log_enemy_list_y, list_log_room3)
log15 = Log2(-1400, 15 + 245 * 2, size[0] + 1460, speed_log2, log_enemy_list_y, list_log_room3)
log16 = Log2(-1600, 15 + 245 * 1, size[0] + 1660, speed_log2, log_enemy_list_y, list_log_room3)

cockroach1 = Cockroach1(20 + 165 * 0, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach2 = Cockroach1(20 + 165 * 1, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach3 = Cockroach1(20 + 165 * 2, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach4 = Cockroach1(20 + 165 * 3, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach5 = Cockroach1(20 + 165 * 4, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach6 = Cockroach1(20 + 165 * 5, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach7 = Cockroach1(20 + 165 * 6, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach8 = Cockroach1(20 + 165 * 7, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)
cockroach9 = Cockroach1(20 + 165 * 8, 5, size[1] - 155, speed_cockroach, cockroach_walk_up,
                        cockroach_walk_down, list_log_room4, cockroach_sniffs_down, cockroach_sniffs_up)

door_right = Door(size[0] - 15, size[1] // 2 - 85, passage_list, 'y', hero)
door_left = Door(0, size[1] // 2 - 85, passage_list, 'y', hero)
door_up = Door(size[0] // 2 - 174 // 2, 0, passage_list, 'x', hero)

key_sound = pygame.mixer.Sound('data/SOUNDS/KEY2.mp3')
hp = heart_list[hp_count]
timer = 0
font = pygame.font.Font(None, 68)
font3 = pygame.font.Font(None, 68)
font2 = pygame.font.Font(None, 30)
key1 = Key(size[0] // 2 - 30, size[1] // 2 - 30, key_sound, hero)
count_ball = 0
key2 = Key(size[0] - 100, size[1] - 160, key_sound, hero)
dialog = ['О! пришёл!', 'кто я такой?', 'не могу сказать...', 'они уже близко,', 'прыгай в портал!']
npc = Npc(size[0] - 200, size[1] // 2 - 50, npc_list1, npc_anime_list1, dialog)
time_count = pygame.time.get_ticks()

text = font.render(str(time_count // 1000 // 60) + ':' + str(time_count // 1000 % 60), True, (255, 255, 255))
count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
event = 0
flag_time = 0
count = 0
flag_music = 1


def room0():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
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
        if door_right.collide():
            run = 0
            hero.x = 60
            room1()
        screen.blit(bg, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door_right.sprite, (door_right.x, door_right.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(hero.image, (hero.x, hero.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room1():
    global run, time_count, text, event, timer, hp_count, hp, count_ball_text, count
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
        if hp_count < 3 and timer < time_count:
            timer = time_count + 500
            if hero.does_collide_enemy(mushroom1.list):
                hp_count += damage
                hp = heart_list[hp_count]
                sound_damage.play()
            if hp_count == 3:
                run = 0
                pygame.mixer.music.set_volume(0)
                c = Lose()
        if door_right.collide():
            run = 0
            hero.x = 60
            room2()
        screen.blit(bg, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(hp, (10, 10))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(door_right.sprite, (door_right.x, door_right.y))
        screen.blit(hero.image, (hero.x, hero.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        else:
            hero.render()
        mushroom1.list.update()
        mushroom1.list.draw(screen)
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room2():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
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
            if hero.does_collide_enemy(log1.list):
                hp_count += damage
                hp = heart_list[hp_count]
                sound_damage.play()
            if hp_count == 3:
                run = 0
                pygame.mixer.music.set_volume(0)
                c = Lose()
        if door_right.collide():
            run = 0
            hero.x = 60
            room3()
        if not key2.key_invent:
            if door_up.collide():
                run = 0
                hero.y = size[1] - 160
                room4()
        if door_left.collide():
            run = 0
            hero.x = size[0] - 100
            room1()
        screen.blit(bg, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door_left.sprite, (door_left.x, door_left.y))
        screen.blit(door_up.sprite, (door_up.x, door_up.y))
        screen.blit(door_right.sprite, (door_right.x, door_right.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(hero.image, (hero.x, hero.y))
        log1.list.update()
        log1.list.draw(screen)
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room3():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
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
            if hero.does_collide_enemy(log11.list):
                hp_count += damage
                hp = heart_list[hp_count]
                sound_damage.play()
            if hp_count == 3:
                c = Lose()
        screen.blit(bg, (0, 0))
        screen.blit(text, (150, 10))
        if door_left.collide():
            run = 0
            hero.x = size[0] - 100
            room2()
        screen.blit(door_left.sprite, (door_left.x, door_left.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        log11.list.update()
        log11.list.draw(screen)
        screen.blit(hero.image, (hero.x, hero.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        key2.collide()
        screen.blit(key_sprite, (key2.x, key2.y))
        clock.tick(FPS)
        pygame.display.update()


def room4():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
    run = 1
    pygame.mixer.music.set_volume(0)
    while run:
        time_count = pygame.time.get_ticks()
        text = font.render(str(time_count // 1000 // 60) + ':' + str(time_count // 1000 % 60), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = 0
                elif event.key == pygame.K_SPACE and npc.flag2 < 2:
                    npc.dialog()
            elif event.type == pygame.QUIT:
                sys.exit()
        hero.render()
        torch1.render()
        text_d = font2.render(npc.text, True, (255, 255, 255))
        screen.blit(bg_house, (0, 0))
        screen.blit(text, (150, 10))
        keys = pygame.key.get_pressed()
        if npc.flag2:
            if npc.flag2 == 2:
                portal1.render1()
                screen.blit(portal1.sprite, (portal1.x, portal1.y))
            elif npc.flag2 == 3:
                portal1.render2()
                # PORTAL EXIT
                screen.blit(portal1.sprite, (portal1.x, portal1.y))
                if hero.does_collide(portal1.rect):
                    npc.flag2 = 4
                    sound_tp.play()
            elif npc.flag2 == 4:
                portal1.render3()
                screen.blit(portal1.sprite, (portal1.x, portal1.y))
            elif npc.flag2 == 5:
                run = 0
                hero.x, hero.h = size[0] // 2 - 55 // 2, size[1] - 300
                hero.h = 130
                room5()
            if 1 in keys:
                hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        if hero.y + 130 < npc.y + 180:
            if npc.flag2 != 4:
                screen.blit(hero.image, (hero.x, hero.y))
            screen.blit(npc.sprite, (npc.x, npc.y))
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
        elif hero.y + 130 > npc.y + 180 < torch1.y + 240:
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
            if npc.flag2 != 4:
                screen.blit(hero.image, (hero.x, hero.y))
            screen.blit(npc.sprite, (npc.x, npc.y))
        else:
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
            screen.blit(npc.sprite, (npc.x, npc.y))
            if npc.flag2 != 4:
                screen.blit(hero.image, (hero.x, hero.y))

        if npc.flag1:
            if abs(hero.y - npc.y) < 100 and abs(hero.x - npc.x) < 100:
                npc.render1()
        else:
            npc.render2()
        if npc.count1 > 0:
            screen.blit(text_d, (npc.x - len(npc.text), npc.y - 30))
        clock.tick(FPS)
        pygame.display.set_caption(f'{clock.get_fps()}')
        pygame.display.update()


def room5():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text, flag_music
    run = 1
    if flag_music:
        pygame.mixer.music.load('data/SOUNDS/dung.mp3')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        door_up.c = 2
    flag_music = 0
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
        if not key1.key_invent:
            if door_up.collide():
                run = 0
                hero.y = size[1] - 160
                room0()
        if door_left.collide():
            run = 0
            hero.x = size[0] - 100
            room6()
        elif door_right.collide():
            run = 0
            hero.x = 60
            room7()
        screen.blit(bg_dung, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door_right.sprite, (door_right.x, door_right.y))
        screen.blit(door_left.sprite, (door_left.x, door_left.y))
        screen.blit(door_up.sprite, (door_up.x, door_up.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(hero.image, (hero.x, hero.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room6():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
    run = 1
    while run:
        time_count = pygame.time.get_ticks()
        if hp_count < 3 and timer < time_count:
            timer = time_count + 500
            if hero.does_collide_enemy(cockroach1.list):
                hp_count += damage
                hp = heart_list[hp_count]
                sound_damage.play()
            if hp_count == 3:
                run = 0
                pygame.mixer.music.set_volume(0)
                c = Lose()
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
            if hp_count == 3:
                run = 0
                pygame.mixer.music.set_volume(0)
                c = Lose()
        if door_right.collide():
            run = 0
            hero.x = 60
            room5()
        elif door_left.collide():
            run = 0
            hero.x = size[0] - 100
            room8()
        screen.blit(bg_dung, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door_right.sprite, (door_right.x, door_right.y))
        screen.blit(door_left.sprite, (door_left.x, door_left.y))
        cockroach1.list.update(time_count)
        cockroach1.list.draw(screen)
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(hero.image, (hero.x, hero.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room7():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
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
            if hp_count == 3:
                run = 0
                pygame.mixer.music.set_volume(0)
                c = Lose()
        if door_left.collide():
            run = 0
            hero.x = size[0] - 100
            room5()
        screen.blit(bg_dung_p, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door_left.sprite, (door_left.x, door_left.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(hero.image, (hero.x, hero.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room8():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
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
            if hp_count == 3:
                run = 0
                pygame.mixer.music.set_volume(0)
                c = Lose()
        if door_right.collide():
            run = 0
            hero.x = 60
            room6()
        screen.blit(bg_dung, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door_right.sprite, (door_right.x, door_right.y))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        key1.collide()
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(hero.image, (hero.x, hero.y))
        screen.blit(key_sprite, (key1.x, key1.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()

a = randint(0, 2)
b = randint(0, 1)
room0()
