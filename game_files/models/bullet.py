import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, settings, screen, ship):
        # Inheriting from Sprite, we can act in all grouped elements at once
        super(Bullet, self).__init__()

        # Create bullet and position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Bullet vertical position as a decimal
        self.y = float(self.rect.y)

        # Screen, color, speed
        self.speed = settings.bullet_speed
        self.color = settings.bullet_color
        self.screen = screen

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
