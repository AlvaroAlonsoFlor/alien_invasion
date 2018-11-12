import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('../images/player-ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    