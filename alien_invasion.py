import pygame
from pygame.sprite import Group
import functions as fun
from settings import Settings
from ship import Ship
from stats import Stats
from button import Button


def run_game():
    # initialize game and create screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_res)
    pygame.display.set_caption("Alien Invasion")
    stats = Stats()
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    play_button = Button(settings, screen, 'Play')
    fun.create_fleet(settings, screen, aliens, ship.rect.height, stats)

    # start the main loop for the game
    while True:
        fun.check_events(settings, screen, ship, bullets, stats, aliens, play_button)
        if stats.game_active:
            ship.update()
            bullets.update()
            aliens.update()
            fun.drop_aliens(aliens)
            fun.collide(ship, aliens, bullets, settings, stats)
            fun.delete_bullets(bullets)
        fun.update_screen(screen, settings, ship, bullets, aliens, stats, play_button)


if __name__ == '__main__':
    run_game()
