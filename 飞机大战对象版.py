import random
from time import sleep

import pygame
from pygame import *


# 玩家飞机
class HeroPlane(object):
    def __init__(self, screen):
        # 飞机图片作为飞机
        self.player = pygame.image.load("./feiji/hero1.png")

        # 定义飞机坐标
        self.x = 480 / 2 - 100 / 2
        self.y = 600

        # 飞机速度
        self.speed = 10

        # 记录当前窗口
        self.screen = screen

        # 记录子弹列表
        self.bullets = []

    def key_control(self):
        # 监听键盘
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            # 按下空格发射子弹
            bullet = Bullet(self.screen, self.x, self.y)
            # 把子弹放到列表里
            self.bullets.append(bullet)

    def display(self):
        # 5 让飞机动起来
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞
            bullet.auto_move()
            # 子弹显示
            bullet.display()


# 敌方飞机的类
class EnemyPlane(object):
    def __init__(self, screen):
        # 飞机图片作为飞机
        self.player = pygame.image.load("./feiji/enemy0.png")

        # 定义飞机坐标
        self.x = 0
        self.y = 0

        # 飞机速度
        self.speed = 10

        # 记录当前窗口
        self.screen = screen

        # 记录子弹列表
        self.bullet = []

        # 敌机移动属性
        self.direction = 'right';

    def display(self):
        # 5 让飞机动起来
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullet:
            # 让子弹飞
            bullet.auto_move()
            # 子弹显示
            bullet.display()

    def auto_move(self):
        # 敌机自动移动
        if self.direction == 'right':
            self.x += self.speed
        if self.direction == 'left':
            self.x -= self.speed

        # 修改方向
        if self.x > 480 - 51:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):
        # 自动开火  创建子弹对象
        random_num = random.randint(1, 10)
        if random_num == 8:
            buttet = EnemyBullet(self.screen, self.x, self.y)
            self.bullet.append(buttet)


# 子弹类
# 属性
class Bullet(object):
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 100 / 2 - 22 / 2
        self.y = y - 22
        # 图片
        self.image = pygame.image.load("./feiji/bullet.png")
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 20

    def display(self):
        # 5 让子弹动起来
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        # 修改子弹y坐标
        self.y -= self.speed


# 敌机子弹类
# 属性
class EnemyBullet(object):
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 50 / 2 - 8 / 2
        self.y = y + 39
        # 图片
        self.image = pygame.image.load("./feiji/bullet1.png")
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 20

    def display(self):
        # 5 让子弹动起来
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        # 修改子弹y坐标
        self.y += self.speed


# 添加声音
class GameSound(object):
    def __init__(self):
        pygame.mixer.init()  # 背景音乐初始化
        pygame.mixer.music.load("./feiji/bg2.ogg")
        pygame.mixer.music.set_volume(0.5)  # 声音大小

    def playBackgroundMusic(self):
        pygame.mixer.music.play(-1)  # 开始播放


def main():
    """完成整个程序的控制"""
    sound = GameSound()
    sound.playBackgroundMusic()

    # 1 创建一个窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2 创建一个图片，当做背景
    background = pygame.image.load("./feiji/background.png")
    # 玩家飞机的对象
    player = HeroPlane(screen)
    # 敌方飞机
    enemyplane = EnemyPlane(screen)

    while True:
        # 3 将飞机图片贴到窗口中
        screen.blit(background, (0, 0))

        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                # 执行pygame退出
                pygame.quit()
                # pygame退出
                exit()
        # 执行飞机的按键监听
        player.key_control()
        # 显示飞机
        player.display()
        # 敌方飞机
        enemyplane.display()
        # 敌机自动移动
        enemyplane.auto_move()
        # 敌机产生子弹
        enemyplane.auto_fire()

        # 4 显示窗口中的内容
        pygame.display.update()
        sleep(0.01)


if __name__ == '__main__':
    main()
