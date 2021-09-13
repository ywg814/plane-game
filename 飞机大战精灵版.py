import random
from time import sleep

import pygame
from pygame import *


# 玩家飞机
class HeroPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # 创建图像
        self.image = pygame.image.load("./feiji/hero1.png")

        # 图片存为精灵类
        self.rect = self.image.get_rect()
        self.rect.topleft = [480 / 2 - 100 / 2, 600]

        # 飞机速度
        self.speed = 10

        # 记录当前窗口
        self.screen = screen

        # 记录子弹列表
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        # 监听键盘
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.rect.top -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.rect.bottom += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.rect.left -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.rect.right += self.speed
        if key_pressed[K_SPACE]:
            # 按下空格发射子弹
            bullet = Bullet(self.screen, self.rect.left, self.rect.right)
            # 把子弹放到列表里
            self.bullets.add(bullet)

    def display(self):
        # 5 让飞机动起来
        self.screen.blit(self.image, self.rect)
        # 更新子弹坐标
        self.bullets.update()
        # 显示子弹
        self.bullets.draw(self.screen)

    def update(self):
        self.key_control()
        self.display()


# 敌方飞机的类
class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # 飞机图片作为飞机
        self.image = pygame.image.load("./feiji/enemy0.png")
        # 得到图片大小
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

        # 飞机速度
        self.speed = 10

        # 记录当前窗口
        self.screen = screen

        # 记录子弹列表
        self.bullets = pygame.sprite.Group()

        # 敌机移动属性
        self.direction = 'right'

    def display(self):
        # 5 让飞机动起来
        self.screen.blit(self.image, self.rect)
        # 更新子弹
        self.bullets.update()
        self.bullets.draw(self.screen)

    def auto_move(self):
        # 敌机自动移动
        if self.direction == 'right':
            self.rect.left += self.speed
        if self.direction == 'left':
            self.rect.left -= self.speed

        # 修改方向
        if self.rect.left > 480 - 51:
            self.direction = 'left'
        elif self.rect.left < 0:
            self.direction = 'right'

    def auto_fire(self):
        # 自动开火  创建子弹对象
        random_num = random.randint(1, 10)
        if random_num == 8:
            buttet = EnemyBullet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(buttet)



# 子弹类
# 属性
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./feiji/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 100 / 2 - 22 / 2, y - 22]

        # 窗口
        self.screen = screen
        # 速度
        self.speed = 20

    def update(self):
        # 修改子弹y坐标
        self.rect.top -= self.speed
        if self.rect.top < -22:
            self.kill()



# 敌机子弹类
# 属性
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./feiji/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 50 / 2 - 8 / 2, y + 39]

        # 窗口
        self.screen = screen
        # 速度
        self.speed = 20

    def update(self):
        # 修改子弹y坐标
        self.rect.top += self.speed
        if self.rect.top > 852:
            self.kill()


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
        player.update()
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
