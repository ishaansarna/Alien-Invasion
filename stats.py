class Stats:
    def __init__(self):
        self.game_active = 0
        self.number_aliens = 0
        self.score = 0
        self.number_played = 0
        self.number_aliens_start = 0

    def new_game(self):
        self.number_aliens = 0
        self.score = 0

    def number_killed_aliens(self):
        return self.number_aliens_start - self.number_aliens
