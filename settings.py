class Settings:
    def __init__(self):
        self.debug = 0
        # Screen settings
        self.screen_res = 1200, 800
        self.bg_color = 230, 230, 230

        # Bullet settings
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        if self.debug:
            self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0

        # Alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_speed_change_factor = 1.04

        # Score settings
        self.score_increase_factor = 1.10
