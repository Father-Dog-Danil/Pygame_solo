import pygame
pygame.init()
import sys
from setting import *


class Menu:
    def __init__(self):
        self.weight = 306
        self.height = 64
        size = (1280, 720)
        pygame.mixer.music.load('data/SOUNDS/menu.mp3')
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)
        self.sprite_list_hero = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win3.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win4.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win5.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win6.png')]
        self.play_button_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/play_button1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/play_button2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/play_button3.png')]
        self.exit_button_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/exit_button1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/exit_button2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/exit_button3.png')]
        self.new_button_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/new_button1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/new_button2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/new_button3.png')]
        self.music_button_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/music_button1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/music_button2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/music_button3.png')]
        self.play_button = self.play_button_list[0]
        self.exit_button = self.exit_button_list[0]
        self.new_button = self.new_button_list[0]
        self.music_button = self.music_button_list[0]
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.bg = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/MAP2.png')
        self.screen.blit(self.bg, (0, 0))
        flag = 1
        self.cursor_play = 1
        self.cursor_new = 1
        self.cursor_exit = 1
        self.cursor_music = 1
        self.count = 0
        while flag:
            if self.count >= len(self.sprite_list_hero) * 6:
                self.flag1 = 0
            elif self.count <= 0:
                self.flag1 = 1
            if self.flag1:
                self.image = self.sprite_list_hero[self.count // 6]
                self.count += 1
            else:
                self.count -= 1
                self.image = self.sprite_list_hero[self.count // 6]
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.image, (size[0] // 4 - 55 // 2, size[1] // 2 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 4) * 3 - 55 // 2, size[1] // 2 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 6 - 55 // 2, size[1] // 2 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 6) * 5 - 55 // 2, size[1] // 2 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 12 - 55 // 2, size[1] // 2 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 12) * 11 - 55 // 2, size[1] // 2 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 4 - 55 // 2, size[1] // 4 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 4) * 3 - 55 // 2, size[1] // 4 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 6 - 55 // 2, size[1] // 4 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 6) * 5 - 55 // 2, size[1] // 4 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 12 - 55 // 2, size[1] // 4 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 12) * 11 - 55 // 2, size[1] // 4 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 12 - 55 // 2, size[1] // 2 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 12) * 11 - 55 // 2, size[1] // 2 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 4 - 55 // 2, size[1] * 0.75 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 4) * 3 - 55 // 2, size[1] * 0.75 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 6 - 55 // 2, size[1] * 0.75 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 6) * 5 - 55 // 2, size[1] * 0.75 - 143 // 2))

            self.screen.blit(self.image, (size[0] // 12 - 55 // 2, size[1] * 0.75 - 143 // 2))
            self.screen.blit(self.image, ((size[0] // 12) * 11 - 55 // 2, size[1] * 0.75 - 143 // 2))

            self.play_button_coordinate = (size[0] // 2 - self.weight // 2, 150 - self.height // 2)
            self.screen.blit(self.play_button, self.play_button_coordinate)
            self.new_button_coordinate = (size[0] // 2 - self.weight // 2, 250 - self.height // 2)
            self.screen.blit(self.new_button, self.new_button_coordinate)
            self.music_button_coordinate = (size[0] // 2 - self.weight // 2, 350 - self.height // 2)
            self.screen.blit(self.music_button, self.music_button_coordinate)
            self.exit_button_coordinate = (size[0] // 2 - self.weight // 2, 450 - self.height // 2)
            self.screen.blit(self.exit_button, self.exit_button_coordinate)
            self.w, self.h = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.cursor_play = 0
                        self.cursor_exit = 0
                        self.cursor_new = 0
                        self.cursor_music = 0
            if size[0] // 2 - self.weight // 2 < self.w < size[0] // 2 + self.weight // 2 and \
                150 + self.height // 2 > self.h > 150 - self.height // 2:
                if self.cursor_play:
                    self.play_button = self.play_button_list[1]
                else:
                    self.play_button = self.play_button_list[2]
                    self.screen.blit(self.play_button, self.play_button_coordinate)
                    flag = 0
            elif size[0] // 2 - self.weight // 2 < self.w < size[0] // 2 + self.weight // 2 and \
                250 + self.height // 2 > self.h > 250 - self.height // 2:
                if self.cursor_new:
                    self.new_button = self.new_button_list[1]
                else:
                    self.new_button = self.new_button_list[2]
                    self.screen.blit(self.new_button, self.new_button_coordinate)
                    f = open('data/floor.txt', 'r')
                    old_data = f.read()
                    new_data = old_data.replace(old_data, str(0))
                    f = open('data/floor.txt', 'w')
                    f.write(new_data)

                    f = open('data/time.txt', 'r')
                    old_data = f.read()
                    new_data = old_data.replace(old_data, str(0))
                    f = open('data/time.txt', 'w')
                    f.write(new_data)

                    f = open('data/heart.txt', 'r')
                    old_data = f.read()
                    new_data = old_data.replace(old_data, str(0))
                    f = open('data/heart.txt', 'w')
                    f.write(new_data)

                    flag = 0

            elif size[0] // 2 - self.weight // 2 < self.w < size[0] // 2 + self.weight // 2 and \
                350 + self.height // 2 > self.h > 350 - self.height // 2:
                if self.cursor_music:
                    self.music_button = self.music_button_list[1]
                else:
                    self.music_button = self.music_button_list[2]
                    self.screen.blit(self.music_button, self.music_button_coordinate)

            elif size[0] // 2 - self.weight // 2 < self.w < size[0] // 2 + self.weight // 2 and \
            450 + self.height // 2 > self.h > 450 - self.height // 2:
                if self.cursor_exit:
                    self.exit_button = self.exit_button_list[1]
                else:
                    self.exit_button = self.exit_button_list[2]
                    self.screen.blit(self.exit_button, self.exit_button_coordinate)
                    sys.exit()
            else:
                self.play_button = self.play_button_list[0]
                self.exit_button = self.exit_button_list[0]
                self.new_button = self.new_button_list[0]
                self.music_button = self.music_button_list[0]
                self.cursor_play = 1
                self.cursor_exit = 1
                self.cursor_new = 1
                self.cursor_music = 1

            pygame.display.update()
