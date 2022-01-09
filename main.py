from menu import Menu
from setting import *


r = Menu()
screen = pygame.display.set_mode(size, mode)
q = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/loading.png')
screen.blit(q, (0, 0))
pygame.display.update()


import sys
from win import Win
from note import Note
from door_key import Key, Door
from hero import Hero
from enemy import Mushroom, Log1, Log2, Cockroach1, Spider, Stone
from NPC import Npc
from torch import Torch
from sprite import *
from lose import Lose
from portal import Portal


pygame.init()
pygame.mixer.music.load('data/SOUNDS/bg.mp3')
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)
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
boss_room = pygame.sprite.Group()
stone_boss = pygame.sprite.Group()

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

SPIDER = Spider(-300, 100, 0.1, spider_sprites, spider_kill_sprites, boss_room)


door_right = Door(size[0] - 15, size[1] // 2 - 85, passage_list, 'y', hero)
door_left = Door(0, size[1] // 2 - 85, passage_list, 'y', hero)
door_up1 = Door(size[0] // 2 - 174 // 2, 0, passage_list, 'x', hero)
door_up2 = Door(size[0] // 2 - 174 // 2, 0, passage_list, 'x', hero)

key_sound = pygame.mixer.Sound('data/SOUNDS/KEY2.mp3')
note_sound = pygame.mixer.Sound('data/SOUNDS/note.mp3')
hp = heart_list[hp_count]
timer = 0
font = pygame.font.Font(None, 68)
font3 = pygame.font.Font(None, 68)
font2 = pygame.font.Font(None, 30)
key1 = Key(size[0] - 200, size[1] // 2 - 30, key_sound, hero)
note = Note(size[0] // 2 - 30, size[1] // 2 - 30, hero, note_sound)
count_ball = 0
key2 = Key(size[0] - 100, size[1] - 160, key_sound, hero)
dialog1 = ['О! пришёл!', 'кто я такой?', 'не могу сказать...', 'они уже близко,', 'прыгай в портал!']
dialog2 = ['Оно ждёт', 'поторопись', 'пророчество...', 'ты избран', 'спаси нас.']
npc = Npc(size[0] - 200, size[1] // 2 - 50, npc_list1, npc_anime_list1, dialog1)
npc2 = Npc(size[0] - 200, size[1] // 2 - 50, npc_list1, npc_anime_list1, dialog2)
portal1 = Portal(0, 0, portal_list1, portal_list_anime1, portal_tp_list1, npc, FPS)
portal2 = Portal(0, 0, portal_list2, portal_list_anime2, portal_tp_list2, npc2, FPS)
time_count = pygame.time.get_ticks()
pygame.mouse.set_visible(False)
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
                c = Lose(text)
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
                c = Lose(text)
        if door_right.collide():
            run = 0
            hero.x = 60
            room3()
        if not key2.key_invent:
            if door_up1.collide():
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
        screen.blit(door_up1.sprite, (door_up1.x, door_up1.y))
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
                c = Lose(text)
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
            if door_up2.collide():
                run = 0
                hero.y = size[1] - 160
                room9()
        if door_left.collide():
            run = 0
            hero.x = size[0] - 100
            room6()
        elif door_right.collide():
            run = 0
            hero.x = 60
            room7()
        if key1.key_invent:
            screen.blit(bg_dung, (0, 0))
        else:
            screen.blit(bg_dung_blood, (0, 0))
        screen.blit(text, (150, 10))
        screen.blit(door_right.sprite, (door_right.x, door_right.y))
        screen.blit(door_left.sprite, (door_left.x, door_left.y))
        screen.blit(door_up2.sprite, (door_up2.x, door_up2.y))
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
                c = Lose(text)
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
                c = Lose(text)
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
                c = Lose(text)
        if door_left.collide():
            run = 0
            hero.x = size[0] - 100
            room5()
        if not note.invent:
            screen.blit(bg_dung_p, (0, 0))
        else:
            screen.blit(bg_dung_p_blood, (0, 0))
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
        if note.invent:
            key1.collide()
            screen.blit(key_sprite, (key1.x, key1.y))
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
                if event.key == pygame.K_SPACE:
                    run = 2
            elif event.type == pygame.QUIT:
                sys.exit()
        hero.render()
        if hp_count < 3 and timer < time_count:
            timer = time_count + 500
            if hp_count == 3:
                run = 0
                pygame.mixer.music.set_volume(0)
                c = Lose(text)
        if door_right.collide():
            run = 0
            hero.x = 60
            room6()
        screen.blit(bg_bibl, (0, 0))
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
        note.collide()
        if note.invent and run != 2:
            screen.blit(note_image1, (size[0] // 2 - 300, size[1] // 2 - 225))
        screen.blit(note_image2, (note.x, note.y))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


def room9():
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
                elif event.key == pygame.K_SPACE and npc2.flag2 < 2:
                    npc2.dialog()
            elif event.type == pygame.QUIT:
                sys.exit()
        hero.render()
        torch1.render()
        text_d = font2.render(npc2.text, True, (255, 255, 255))
        screen.blit(bg_dung, (0, 0))
        screen.blit(text, (150, 10))
        keys = pygame.key.get_pressed()
        if npc2.flag2:
            if npc2.flag2 == 2:
                portal2.render1()
                screen.blit(portal2.sprite, (portal2.x, portal2.y))
            elif npc2.flag2 == 3:
                portal2.render2()
                # PORTAL EXIT
                screen.blit(portal2.sprite, (portal2.x, portal2.y))
                if hero.does_collide(portal2.rect):
                    npc2.flag2 = 4
                    sound_tp.play()
            elif npc2.flag2 == 4:
                portal2.render3()
                screen.blit(portal2.sprite, (portal2.x, portal2.y))
            elif npc2.flag2 == 5:
                run = 0
                hero.x = size[0] // 2 - hero.w // 2
                hero.y = size[1] // 2 - hero.h // 2
                hero.h = 130
                room_boss()
            if 1 in keys:
                hero.move(keys)
        screen.blit(hp, (10, 10))
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        if hero.y + 130 < npc2.y + 180:
            if npc2.flag2 != 4:
                screen.blit(hero.image, (hero.x, hero.y))
            screen.blit(npc2.sprite, (npc2.x, npc2.y))
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
        elif hero.y + 130 > npc2.y + 180 < torch1.y + 240:
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
            if npc2.flag2 != 4:
                screen.blit(hero.image, (hero.x, hero.y))
            screen.blit(npc2.sprite, (npc2.x, npc2.y))
        else:
            screen.blit(torch1.sprite, (torch1.x, torch1.y))
            screen.blit(npc2.sprite, (npc2.x, npc2.y))
            if npc2.flag2 != 4:
                screen.blit(hero.image, (hero.x, hero.y))

        if npc2.flag1:
            if abs(hero.y - npc2.y) < 100 and abs(hero.x - npc2.x) < 100:
                npc2.render1()
        else:
            npc2.render2()
        if npc2.count1 > 0:
            screen.blit(text_d, (npc2.x - len(npc2.text), npc2.y - 30))
        clock.tick(FPS)
        pygame.display.set_caption(f'{clock.get_fps()}')
        pygame.display.update()


stone1 = Stone(1000, stone, stone_boss, hero.speed)
stone2 = Stone(2000, stone, stone_boss, hero.speed)
stone3 = Stone(3000, stone, stone_boss, hero.speed)
stone4 = Stone(3200, stone, stone_boss, hero.speed)
stone5 = Stone(4000, stone, stone_boss, hero.speed)
stone6 = Stone(4400, stone, stone_boss, hero.speed)
stone7 = Stone(5500, stone, stone_boss, hero.speed)
stone8 = Stone(4500, stone, stone_boss, hero.speed)
stone9 = Stone(5700, stone, stone_boss, hero.speed)
stone10 = Stone(5900, stone, stone_boss, hero.speed)
stone11 = Stone(6500, stone, stone_boss, hero.speed)
stone12 = Stone(1260, stone, stone_boss, hero.speed)
stone13 = Stone(1700, stone, stone_boss, hero.speed)
stone14 = Stone(2400, stone, stone_boss, hero.speed)
stone15 = Stone(2860, stone, stone_boss, hero.speed)
stone16 = Stone(1500, stone, stone_boss, hero.speed)
stone17 = Stone(3600, stone, stone_boss, hero.speed)
stone18 = Stone(6700, stone, stone_boss, hero.speed)
stone19 = Stone(7100, stone, stone_boss, hero.speed)
stone20 = Stone(7300, stone, stone_boss, hero.speed)
stone21 = Stone(7600, stone, stone_boss, hero.speed)


def room_boss():
    global run, time_count, text, event, timer, hp_count, hp, count, count_ball_text
    run = 1
    pygame.mixer.music.load('data/SOUNDS/boss.mp3')
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)
    hero.f()
    a = 0
    b = 1
    v = 0
    chunk = 7
    n = hero.speed
    x_screen = 0
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
        SPIDER.x += 0.05
        for i in range(chunk):
            screen.blit(bg_boss, (x_screen + size[0] * i, 0))
        keys = pygame.key.get_pressed()
        if 1 in keys:
            if x_screen > size[0] * (-chunk + 1):
                a = 1
                if hero.move_boss(keys) == 1 and b:
                    x_screen -= hero.speed
                    stone1.list.update(hero.speed)
                elif hero.move_boss(keys) == 2 and b:
                    x_screen -= hero.speed
                    stone1.list.update(hero.speed)
            else:
                hero.move(keys)
                screen.blit(door_right.sprite, (door_right.x, door_right.y))
                SPIDER.x += 1
        elif a:
            SPIDER.x += 1
        if 170 < hero.y < size[1] - 370:
            SPIDER.y = hero.y - 170
        if hp_count < 3:
            if hero.does_collide_enemy(SPIDER.list):
                b = 0
                hp_count = 3
                hp = heart_list[hp_count]
                screen.blit(hp, (10, 10))
                sound_damage.play()
        if 1:
            if v:
                hero.speed = n
            if hero.does_collide_enemy(stone1.list):
                v = 1
                hero.speed = hero.speed / 2
                #  sound_damage.play()
                timer = time_count + 800
                SPIDER.x += 0.4
        count_ball_text = font.render(str(count_ball), True, (255, 255, 255))
        if count == 336:
            count = 0
        if SPIDER.flag:
            run = 0
            pygame.mixer.music.set_volume(0)
            c = Lose(text)
        if b:
            SPIDER.move()
            SPIDER.render1()
            screen.blit(hero.image, (hero.x, hero.y))
        else:
            SPIDER.render2()
        if door_right.collide():
            run = 0
            pygame.mixer.music.set_volume(0)
            w = Win(text)
        stone1.list.draw(screen)
        SPIDER.list.draw(screen)
        screen.blit(text, (150, 10))
        screen.blit(ball_list[count // 16], (size[0] - 100, 10))
        count += 1
        screen.blit(count_ball_text, (size[0] - 50, 10))
        screen.blit(hp, (10, 10))
        pygame.display.set_caption(f'{clock.get_fps()}')
        clock.tick(FPS)
        pygame.display.update()


room0()
