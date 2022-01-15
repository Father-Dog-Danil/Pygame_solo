import sys

import pygame
pygame.init()


class Win:
    def __init__(self, time):
        pygame.mouse.set_visible(True)
        sound_lose = pygame.mixer.Sound('data/SOUNDS/win.mp3')
        sound_lose.play()
        run = 1
        image = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/MAP2.png')
        self.sprite_list = [
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win1.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win2.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win3.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win4.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win5.png'),
            pygame.image.load('data/IMAGE_GAME/IMAGE_HERO_D/anonimus_win6.png')]
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((400, 400))
        font = pygame.font.Font(None, 100)
        self.count = 0
        text = font.render("YOU WIN!", True, (200, 10, 10))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = 0
                elif event.type == pygame.QUIT:
                    sys.exit()
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
            pygame.display.update()
            screen.blit(image, (-10, -10))
            screen.blit(self.image, (170, 200 - 130 // 2))
            screen.blit(text, (25, 10))
            screen.blit(time, (160, 300))
            clock.tick(60)