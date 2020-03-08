import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent an alien"""

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('resources/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def touch_edge(self):
        if self.rect.left <= 40:
            return 1
        elif self.rect.right >= self.settings.screen_res[0]-110:
            return -1
        else:
            return 0

    def drop(self):
        self.rect.y += self.settings.fleet_drop_speed

    def update(self):
        """Move it"""
        if self.touch_edge():
            self.settings.fleet_direction = self.touch_edge()
        self.rect.x += self.settings.fleet_direction * self.settings.alien_speed_factor
