import pygame


class Ship:

    def __init__(self, screen):
        """Initialize the ship"""
        self.screen = screen

        self.image = pygame.image.load('resources/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.moving = 0

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)

    def center(self):
        self.rect.centerx = self.screen_rect.centerx

    def update(self):
        """Update position of ship"""

        if self.moving < 0 and self.rect.left >= self.screen_rect.left:
            self.rect.centerx += self.moving
        elif self.moving > 0 and self.rect.right <= self.screen_rect.right:
            self.rect.centerx += self.moving
