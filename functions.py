import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(settings, screen, ship, bullets, stats, aliens, play_button):
    # watch for kb and m events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
                stats.game_active = 1
                stats.number_played += 1
                reset(settings, screen, aliens, bullets, ship, stats)
                pygame.mouse.set_visible(False)
        elif event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving += 5
            elif event.key == pygame.K_LEFT:
                ship.moving -= 5
            elif event.key == pygame.K_SPACE:
                if len(bullets) <= 2:
                    new_bullet = Bullet(settings, screen, ship)
                    bullets.add(new_bullet)
            elif event.key == pygame.K_q:
                sys.exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving = 0
            elif event.key == pygame.K_LEFT:
                ship.moving = 0


def reset(settings, screen, aliens, bullets, ship, stats):
    aliens.empty()
    bullets.empty()
    ship.center()
    stats.new_game()
    create_fleet(settings, screen, aliens, ship.rect.height, stats)


def draw_bullets(bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def create_fleet(settings, screen, aliens, ship_height, stats):
    alien = Alien(screen, settings)
    number_aliens_x = int(((settings.screen_res[0] - 2 * alien.rect.width) / (2 * alien.rect.width)) - 1)
    available_space_y = settings.screen_res[1] - (3 * alien.rect.height) - ship_height
    number_rows = int(available_space_y / (2 * alien.rect.height))
    stats.number_aliens = number_aliens_x * number_rows

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien = Alien(screen, settings)
            alien.rect.x = 40 + 2 * alien.rect.width * alien_number
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            aliens.add(alien)


def delete_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def drop_aliens(aliens):
    drop = 0
    for alien in aliens:
        if alien.touch_edge() != 0:
            drop = 1
            break
    if drop:
        for alien in aliens:
            alien.drop()


def collide(ship, aliens, bullets, settings, stats):
    collide_dict = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collide_dict:
        settings.alien_speed_factor *= settings.alien_speed_change_factor
        stats.number_aliens -= 1
        stats.score += 10
        if len(aliens) == 0 or stats.number_aliens == 0:
            stats.game_active = 0
    if pygame.sprite.spritecollideany(ship, aliens):
        print('Over')
        stats.game_active = 0
    for alien in aliens.sprites():
        if alien.rect.bottom >= settings.screen_res[1]:
            print('Over')
            stats.game_active = 0


def update_screen(screen, settings, ship, bullets, aliens, stats, play_button):
    screen.fill(settings.bg_color)
    ship.blitme()
    draw_bullets(bullets)
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
