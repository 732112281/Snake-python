import pygame


class Snake():
    """蛇"""
    def __init__(self, settings, screen, startx, starty, attitude):
        '''初始化蛇的各项属性'''
        self.settings = settings
        self.screen = screen
        self.rects = []
        # 移动索引
        self.directions = {pygame.K_w: 'up', pygame.K_s: 'down',
                           pygame.K_a: 'left', pygame.K_d: 'right',
                           pygame.K_UP: 'up', pygame.K_DOWN: 'down',
                           pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right'}
        # 初始方向
        if attitude == 'vertical_up':
            self.snake_coords = [{'x': startx, 'y': starty},
                                 {'x': startx, 'y': starty + 1},
                                 {'x': startx, 'y': starty + 2}]
            self.direction = 'up'
        elif attitude == 'vertical_down':
            self.snake_coords = [{'x': startx, 'y': starty},
                                {'x': startx, 'y': starty - 1},
                                {'x': startx, 'y': starty - 2}]
            self.direction = 'down'
        elif attitude == 'horizontal_right':
            self.snake_coords = [{'x': startx, 'y': starty},
                                 {'x': startx - 1, 'y': starty},
                                 {'x': startx - 2, 'y': starty}]
            self.direction = 'right'
        elif attitude == 'horizontal_left':
            self.snake_coords = [{'x': startx, 'y': starty},
                                 {'x': startx + 1, 'y': starty},
                                 {'x': startx + 2, 'y': starty}]
            self.direction = 'left'


    def move(self):
        '''蛇的移动'''
        if self.direction == 'up':
            newhead = {'x': self.snake_coords[0]['x'], 'y': self.snake_coords[0]['y'] - 1}
        elif self.direction == 'down':
            newhead = {'x': self.snake_coords[0]['x'], 'y': self.snake_coords[0]['y'] + 1}
        elif self.direction == 'left':
            newhead = {'x': self.snake_coords[0]['x'] - 1, 'y': self.snake_coords[0]['y']}
        elif self.direction == 'right':
            newhead = {'x': self.snake_coords[0]['x'] + 1, 'y': self.snake_coords[0]['y']}
        self.snake_coords.insert(0, newhead)


    def draw(self):
        '''画出蛇'''
        for coord in self.snake_coords:
            x = coord['x'] * self.settings.edge + self.settings.grid_line_width
            y = coord['y'] * self.settings.edge + self.settings.grid_line_width
            # 生成rect对象
            rect_down = pygame.rect.Rect(x, y, self.settings.edge, self.settings.edge)
            rect_up = pygame.rect.Rect(x + self.settings.a_rect_line_width,
                                       y + self.settings.a_rect_line_width,
                                    self.settings.edge - self.settings.a_rect_line_width*2,
                                    self.settings.edge - self.settings.a_rect_line_width*2)
            # 绘制rect
            pygame.draw.rect(self.screen, self.settings.a_rect_active_down_color, rect_down)
            pygame.draw.rect(self.screen, self.settings.a_rect_active_up_color, rect_up)
            # 画出蛇的眼睛
            if self.snake_coords.index(coord) == 0:
                self.draw_eye(rect_up)

    def draw_eye(self, rect):
        """绘制蛇的眼睛"""
        if self.direction == 'up':  # 方向向上
            eye_rect1 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect2 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect1.topleft = rect.topleft
            eye_rect2.topright = rect.topright
        elif self.direction == 'down':  # 方向向下
            eye_rect1 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect2 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect1.bottomleft = rect.bottomleft
            eye_rect2.bottomright = rect.bottomright
        elif self.direction == 'left':  # 方向向左
            eye_rect1 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect2 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect1.topleft = rect.topleft
            eye_rect2.bottomleft = rect.bottomleft
        elif self.direction == 'right':  # 方向向右
            eye_rect1 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect2 = pygame.rect.Rect(0, 0, self.settings.edge // 5, self.settings.edge // 5)
            eye_rect1.topright = rect.topright
            eye_rect2.bottomright = rect.bottomright
        # 绘制眼睛
        pygame.draw.rect(self.screen, self.settings.a_rect_eye_color, eye_rect1)
        pygame.draw.rect(self.screen, self.settings.a_rect_eye_color, eye_rect2)
