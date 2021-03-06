class Settings:
    """存储游戏中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #飞船速度
        self.ship_speed = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 6

        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction 为 1 表示向右移， 为-1 表示向左移
        self.fleet_direction = 1

        #加快游戏节奏的速度
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        #外星人分数的提高速度
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """初始化由游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        #记分
        self.alien_points = 50

        #fleet_direction == 1 表示向左，否则向右
        self.fleet_direction = 1
    
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)