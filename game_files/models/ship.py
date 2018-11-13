import pygame
import pygame.image
import os

class Ship():

    def __init__(self, screen):
        self.screen = screen
        
        # import and scale image
        img_path =  os.path.abspath("game_files/images")
        self.image = pygame.image.load(img_path + '/player-ship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    