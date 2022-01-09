import pygame
import sys
pygame.init()


class Menu:
    def __init__(self):
        size = (400, 400)
        pygame.mixer.music.load('data/SOUNDS/menu.mp3')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        self.play_button_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/play_button1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/play_button2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/play_button3.png')]
        self.exit_button_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/exit_button1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/exit_button2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/exit_button3.png')]
        self.play_button = self.play_button_list[0]
        self.exit_button = self.exit_button_list[0]
        self.screen = pygame.display.set_mode(size)
        self.bg = pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/bg1.png')
        self.screen.blit(self.bg, (0, 0))
        flag = 1
        self.cursor_play = 1
        self.cursor_exit = 1
        while flag:
            self.screen.blit(self.bg, (0, 0))
            self.play_button_coordinate = self.play_button.get_rect(center=(size[0] // 2, 50))
            self.screen.blit(self.play_button, self.play_button_coordinate)
            self.exit_button_coordinate = self.exit_button.get_rect(center=(size[0] // 2, 150))
            self.screen.blit(self.exit_button, self.exit_button_coordinate)
            self.w, self.h = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.cursor_play = 0
                        self.cursor_exit = 0
            if self.w > 50 and self.h < 85 and self.w < 350 and self.h > 15:
                if self.cursor_play:
                    self.play_button = self.play_button_list[1]
                else:
                    self.play_button = self.play_button_list[2]
                    self.play_button_coordinate = self.play_button.get_rect(center=(size[0] // 2, 50))
                    self.screen.blit(self.play_button, self.play_button_coordinate)
                    flag = 0
            elif self.w > 50 and self.h < 180 and self.w < 350 and self.h > 105:
                if self.cursor_exit:
                    self.exit_button = self.exit_button_list[1]
                else:
                    self.exit_button = self.exit_button_list[2]
                    self.exit_button_coordinate = self.exit_button.get_rect(center=(size[0] // 2, 150))
                    self.screen.blit(self.exit_button, self.exit_button_coordinate)
                    sys.exit()
            else:
                self.play_button = self.play_button_list[0]
                self.exit_button = self.exit_button_list[0]
                self.cursor_play = 1
                self.cursor_exit = 1

            pygame.display.update()