class Settings():
    """储存游戏各项设置信息的类"""
    def __init__(self):
        self.screen_width = 600  # 窗口宽度
        self.screen_height = 600  # 窗口高度
        self.title = "Snake"  # 窗口标题
        self.hightest_score_filename = 'saves/highest_score.sna'
        self.scores = 0  # 初始分数
        try:
            with open(self.hightest_score_filename, 'r') as h_sco:
                self.highest_score = int(h_sco.read())
        except FileNotFoundError:
            self.highest_score = 0  # 初始最高分
        self.map_width = 600  # 蛇活动范围宽度
        self.map_height = 400  # 蛇活动范围高度
        self.edge = 20  # 正方形边长
        self.snake_speed = 10  # 蛇的速度
        self.grid_line_width = 2  # 网格边长
        self.a_rect_line_width = 5
        self.colors()  # 初始化颜色
        self.grid_line_color = self.white  # 网格线颜色
        self.grid_bg_color = self.gray  # 网格背景颜色
        self.food_down_color = self.dark_orange  # 食物边缘颜色
        self.food_up_color = self.orange  # 食物中心颜色
        self.a_rect_active_down_color = self.blue  # 蛇每格边缘颜色
        self.a_rect_active_up_color = self.light_blue  # 蛇每格中心颜色
        self.a_rect_eye_color = self.white
        self.rect_col = self.map_width // self.edge  # 每行方格数
        self.rect_row = self.map_height // self.edge  # 每列方格数

    def colors(self):
        """各个颜色"""
        # 颜色选择(RGB颜色)           R    G    B
        self.red =                  (155,   0,   0)  # 红色
        self.light_red =            (175,  20,  20)  # 亮红色
        self.orange =               (255, 165,   0)  # 橙色
        self.dark_orange =          (255, 140,   0)  # 暗橙色
        self.yellow =               (255, 245,  40)  # 黄色
        self.light_yellow =         (175, 175,  20)  # 亮黄色
        self.green =                (  0, 155,   0)  # 绿色
        self.light_green =          ( 20, 175,  20)  # 亮绿色(草绿色)
        self.blue =                 (  0,   0, 155)  # 蓝色
        self.light_blue =           ( 20,  20, 175)  # 亮蓝色(天蓝色)
        self.white =                (255, 245, 245)  # 白色
        self.gray =                 (185, 185, 185)  # 灰色
        self.black =                (  0,   0,   0)  # 黑色
