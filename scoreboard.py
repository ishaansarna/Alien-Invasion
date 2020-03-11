import pygame.font


# noinspection PyAttributeOutsideInit
class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

    def prep_score(self):
        self.score_img = self.font.render(str(int(self.stats.score)), True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        self.level = self.stats.number_played + 1
        self.level_img = self.font.render(str(' '.join(['Level', str(self.level)])), True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.centerx = self.screen.get_rect().centerx
        self.level_rect.top = 20

    def show_score(self):
        self.prep_score()
        self.screen.blit(self.score_img, self.score_rect)

    def show_level(self):
        self.screen.blit(self.level_img, self.level_rect)
