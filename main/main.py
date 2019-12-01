"""游戏主代码"""
import pygame
from pygame.locals import *
from time import sleep

from settings.settings import Settings
import main.functions as fc


def main():
    """游戏主方法"""
    pygame.init()  # 初始化pygame
    screen = pygame.display.set_mode((600, 600), pygame.HWSURFACE)  # 创建窗口
    pygame.display.set_caption("Snake")  # 设置窗口标题
    screen_rect = screen.get_rect()  # 获取窗口的rect属性
    s = pygame.Surface((screen_rect.width, screen_rect.width), pygame.SRCALPHA)
    s.fill((255, 255, 255, 128))  # 设置透明度
    rects = []
    settings = Settings()  # 加载设置
    fc.show_start_info(settings, screen)  # 开始界面
    while True:
        fc.spawn_grid(settings, rects)  # 生成网格
        snake = fc.spawn_snake(settings, screen)  # 生成蛇
        food = fc.spawn_food(settings)  # 设置最初始食物位置
        while True:  # 游戏循环
            fc.check_events(settings, snake)  # 监听键盘
            snake.move()  # 蛇的移动
            is_alive = fc.snake_is_alive(settings, snake)  # 判断蛇是否死亡
            if not is_alive[0]:
                break
            fc.snake_is_eat_food(settings, snake, food)  # 判断蛇是否吃到食物
            fc.draw_grid(settings, screen, rects)  # 绘制网格
            fc.draw_food(settings, screen, food)  # 绘制食物
            snake.draw()  # 绘制蛇
            screen.blit(s, (0, 0))  # 透明度
            fc.draw_score(settings, screen)  # 绘制分数
            pygame.display.update()  # 更新屏幕
            pygame.time.Clock().tick(settings.snake_speed)  # 控制fps
        sleep(1)  # 暂停
        fc.show_gameover_info(settings, screen, s, is_alive[1])  # 结束界面


if __name__ == '__main__':
    main()