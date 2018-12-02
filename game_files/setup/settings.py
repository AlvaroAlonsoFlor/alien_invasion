class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (46, 55, 71)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 10
        self.fleet_drop_speed = 10
            # from left to right
        self.fleet_direction = 1
