class Gamestats:
    """跟踪游戏的统计信息"""
    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        #等按play按钮才是开始游戏
        self.game_active = False

        #最高得分要一直保留的
        self.high_score = 0

        

    def reset_stats(self):
        """初始化在游戏期间变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1