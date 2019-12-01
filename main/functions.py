"""游戏的各个方法
"""

import pygame
import random
from pygame import *

from moudles.snake import Snake


def show_start_info(settings, screen):
    """游戏开始界面"""
    screen_rect = screen.get_rect()
    font1 = pygame.font.SysFont('微软雅黑', 40)
    font2 = pygame.font.SysFont('微软雅黑', 150)
    tip = font1.render('Press any key to start the game~~~', True, settings.light_green)
    t_rect = tip.get_rect()
    t_rect.centerx = screen_rect.centerx
    t_rect.centery = screen_rect.centery*5//4
    gamestart = font2.render('Snake', True, settings.yellow)
    gamestart = pygame.transform.rotate(gamestart, random.randint(-35, 35))
    g_rect = gamestart.get_rect()
    g_rect.centerx = screen_rect.centerx
    g_rect.centery = screen_rect.centery*2//5
    screen.fill(settings.gray)
    screen.blit(tip, t_rect)
    screen.blit(gamestart, g_rect)
    pygame.display.update()
    while True:  # 键盘监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()     # 终止程序
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()  # 终止程序
                else:
                    return  # 结束此函数, 开始游戏


def save(settings):
    """保存最高分"""
    filename = settings.hightest_score_filename
    try:
        with open(filename, 'r') as h_sco:
            highest_score = h_sco.read()
            if settings.scores > int(highest_score):
                with open(filename, 'w') as h_sco:
                    h_sco.write(str(settings.scores))
                settings.highest_score = settings.scores
            else:
                settings.highest_score = highest_score
    except FileNotFoundError:
        with open(filename, 'w') as h_sco:
            h_sco.write(str(settings.scores))
        settings.hightest_score = settings.scores


def show_gameover_info(settings, screen, s, cause):
    """游戏结束界面"""
    save(settings)
    screen_rect = screen.get_rect()
    font1 = pygame.font.SysFont('', 40)
    font2 = pygame.font.SysFont('', 150)
    tip1 = font1.render('Press "Q" or "Esc" to quit the game.', True, settings.light_green)
    tip2 = font1.render('Press any key to start the game.', True, settings.light_green)
    score = font1.render('Score:%s' % settings.scores, True, settings.light_yellow)
    h_score = font1.render('Highest score:%s' % settings.highest_score, True, settings.light_yellow)
    cause = font1.render(cause, True, settings.red)
    gameover = font2.render('GameOver', True, settings.yellow)
    # 获取rect属性
    t1_rect = tip1.get_rect()
    t2_rect = tip2.get_rect()
    s_rect = score.get_rect()
    hs_rect = h_score.get_rect()
    c_rect = cause.get_rect()
    g_rect = gameover.get_rect()
    # 设置位置
    s_rect.topleft = screen_rect.topleft
    hs_rect.topright = screen_rect.topright
    t1_rect.center = (screen_rect.centerx, screen_rect.centery * 5 // 4)
    t2_rect.midtop = t1_rect.midbottom
    g_rect.centerx = screen_rect.centerx
    g_rect.centery = screen_rect.centery * 2 // 5
    c_rect.midtop = g_rect.midbottom
    # 绘制
    screen.fill(settings.gray)
    screen.blit(cause, c_rect)
    screen.blit(s, (0, 0))
    screen.blit(gameover, g_rect)
    screen.blit(tip1, t1_rect)
    screen.blit(tip2, t2_rect)
    screen.blit(score, s_rect)
    screen.blit(h_score, hs_rect)
    pygame.display.update()
    while True:  # 键盘监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()  # 终止程序
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    exit()  # 终止程序
                else:
                    settings.scores = 0
                    return  # 结束此函数, 开始游戏


def spawn_grid(settings, rects):
    """生成网格"""
    # 生成每一个方格的地址
    box_address_list = [[((x*settings.edge + 2), (y*settings.edge + 2))
                         for x in range(settings.rect_col)] for y in range(settings.rect_row)]
    # 生成每一个网格
    for index in range(len(box_address_list)):
        for address in box_address_list[index]:
            down_rect = pygame.rect.Rect(address[0], address[1], settings.edge, settings.edge)
            up_rect = pygame.rect.Rect(address[0] + settings.grid_line_width/2,
                                       address[1] + settings.grid_line_width/2,
                                       settings.edge - settings.grid_line_width,
                                       settings.edge - settings.grid_line_width)
            rects.append({'up_rect': up_rect, 'down_rect': down_rect})


def spawn_snake(settings, screen):
    """生成蛇对象"""
    # 游戏开始时蛇的坐标
    startx = random.randint(4, settings.rect_col-4)
    starty = random.randint(4, settings.rect_row-4)
    # 选择开始游戏时蛇的朝向
    attitude = random.choice(['vertical_up', 'vertical_down', 'horizontal_right', 'horizontal_left'])
    return Snake(settings, screen, startx, starty, attitude)


def spawn_food(settings):
    """生成初始食物坐标"""
    xID = random.randint(0, settings.rect_col-1)
    yID = random.randint(0, settings.rect_row-1)
    x = xID * settings.edge + settings.grid_line_width
    y = yID * settings.edge + settings.grid_line_width
    return {'x': x, 'y': y, 'xID': xID, 'yID': yID}


def snake_is_alive(settings, snake):
    """判断蛇死了没"""
    tag = True
    cause = None
    snake_coords = snake.snake_coords
    if snake_coords[0]['x'] < 0 or snake_coords[0]['x'] >= settings.rect_col \
        or snake_coords[0]['y'] < 0 or snake_coords[0]['y'] >= settings.rect_row:
        tag = False  # 蛇碰壁啦
        cause = 'You hit yourself to death.'
    for snake_body in snake_coords[1:]:
        if snake_body['x'] == snake_coords[0]['x'] and snake_body['y'] == snake_coords[0]['y']:
            tag = False  # 蛇碰到自己身体啦
            cause = 'You bite yourself to death.'
    return tag, cause


def choose_address(settings, food, snake_coords):
    """选择坐标"""
    food['xID'] = random.randint(0, settings.rect_col - 1)
    food['yID'] = random.randint(0, settings.rect_row - 1)
    for coord in snake_coords:
        if coord['x'] == food['xID'] and coord['y'] == food['yID']:
            choose_address(settings, food, snake_coords)


def snake_is_eat_food(settings, snake, food):
    """判断贪吃蛇是否吃到食物"""
    snake_coords = snake.snake_coords
    if snake_coords[0]['x'] == food['xID'] and snake_coords[0]['y'] == food['yID']:
        # 如果吃到食物, 就保留尾部一格，并重新生成食物
        choose_address(settings, food, snake_coords)
        food['x'] = food['xID'] * settings.edge + settings.grid_line_width
        food['y'] = food['yID'] * settings.edge + settings.grid_line_width
        settings.scores += 1
    else:
        del snake_coords[-1]  # 如果没有吃到食物, 就向前移动, 那么尾部一格删掉


def check_events(settings, snake):
    """监听键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 终止程序
            pygame.quit()
            save(settings)
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # 终止程序
                pygame.quit()
                save(settings)
                exit()
            if event.key in snake.directions.keys():
                change_direction = snake.directions[event.key]
                if direction_check(snake.direction, change_direction):
                    snake.direction = change_direction
                    break


def direction_check(moving_direction, change_direction):
    """判断是否能够改变行进方向"""
    directions = [['up', 'down'], ['left', 'right']]
    if moving_direction in directions[0] and change_direction in directions[1]:
        return True
    elif moving_direction in directions[1] and change_direction in directions[0]:
        return True
    return False


def draw_grid(settings, screen, rects):
    """画出网格"""
    for pair_rect in rects:
        pygame.draw.rect(screen, settings.grid_line_color, pair_rect['down_rect'])
        pygame.draw.rect(screen, settings.grid_bg_color, pair_rect['up_rect'])


def draw_food(settings, screen, food):
    """画出食物"""
    down_rect = pygame.rect.Rect(food['x'], food['y'], settings.edge, settings.edge)
    up_rect = pygame.rect.Rect(food['x'] + settings.edge // 5, food['y'] + settings.edge // 5,
                               settings.edge - settings.edge // 5 * 2,
                               settings.edge - settings.edge // 5 * 2)
    pygame.draw.rect(screen, settings.food_down_color, down_rect)
    pygame.draw.rect(screen, settings.food_up_color, up_rect)


def draw_score(settings, screen):
    """显示分数"""
    font = pygame.font.SysFont('微软雅黑', 50)
    score = font.render('Score: %s' % settings.scores, True, settings.green)
    h_score = font.render('Highest score:%s' % settings.highest_score, True, settings.green)
    # 获取rect属性
    s_rect = score.get_rect()
    hs_rect = h_score.get_rect()
    screen_rect = screen.get_rect()
    # 设置位置
    s_rect.bottomleft = screen_rect.bottomleft
    hs_rect.bottomright = screen_rect.bottomright
    # 绘制
    screen.blit(score, s_rect)
    screen.blit(h_score, hs_rect)