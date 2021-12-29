import pygame
pygame.init()


class Lose:
    def __init__(self):
        sound_lose = pygame.mixer.Sound('data/SOUNDS/LOSE.mp3')
        sound_lose.play()
        image = pygame.image.load('data/IMAGE_GAME/IMAGE_MAP/MAP1.png')
        lose = pygame.image.load('data/IMAGE_GAME/IMAGE_BUTTON/LOSE.png')
        screen = pygame.display.set_mode((400, 400))
        font = pygame.font.Font(None, 100)
        text = font.render("YOU LOSE!", True, (200, 10, 10))
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.update()
            screen.blit(image, (-10, -10))
            screen.blit(lose, (0, 0))
            screen.blit(text, (10, 10))


c = Lose()