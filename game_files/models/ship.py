import pygame
import pygame.image
import os
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen, settings):

        super(Ship, self).__init__()

        self.screen = screen
        
        # import and scale image
        img_path =  os.path.abspath("game_files/images")
        self.image = pygame.image.load(img_path + '/player-ship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Alocate rectangle to image and place in center bottom
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # set a decimal value for the center, so we can pass floats to the ship speed
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center
        self.rect.bottom = self.screen_rect.bottom

        # Moving left or right for continuous movement
        self.move_right = False
        self.move_left = False

        # Settings
        self.settings = settings
        self.speed = settings.ship_speed

    def update_position(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed
        elif self.move_left and self.rect.left > 0:
            self.rect.centerx -= self.speed
    
    def recenter(self):
        self.center = self.screen_rect.centerx
        self.rect.centerx = self.screen_rect.centerx
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    
