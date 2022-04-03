# 导入模块

from operator import index
import sys
from turtle import towards
import pygame
import math

# pygame初始化

pygame.init()

# 设置主窗口

main_screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption("这是一个标题")
image_icon = pygame.image.load("../res/image/icon.png").convert()
pygame.display.set_icon(image_icon)

# 设置背景

image_background = pygame.image.load("../res/image/map.png").convert()
background_x = 320
background_y = -1280

# 初始化移动变量

movement_x = 0
movement_y = 0

# 定义实体类


class solid(pygame.sprite.Sprite):
    def __init__(self, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = location

# 定义玩家类


class player(pygame.sprite.Sprite):
    def __init__(self, filename, frames=1):   # 造型frames默认为1
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(filename)
        self.original_width = img.get_width() // 3
        self.original_height = img.get_height() // 4        # 分割图片
        x = 0
        y = 0
        for frame_no in range(frames):
            self.images.append(img.subsurface((x, y, 128, 128)))
            x += self.original_width
            if x == 3 * self.original_width:
                x = 0
                y += self.original_height
        self.index = 7
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = [640-64, 480-64]
        self.last_time = 0
        self.towards = 1
        self.movement = 0
        self.firstframe = {1: 7, 2: 1, 3: 4, 4: 10}
        self.lastframe = {1: 9, 2: 3, 3: 6, 4: 12}

    def update(self, current_time):
        x = self.firstframe[self.towards]
        y = self.lastframe[self.towards]
        if self.index <= x - 1:
            self.index = x - 1
        if current_time - self.last_time > 150:
            self.index += 1
            self.last_time = current_time
        if self.index >= y:
            self.index = x - 1
# 设置角色


buyer = player("../res/image/人物.png", 12)
buyer_speed = 12


# 设置障碍物

blocks = []
for i in range(7, 26):
    blocks.append(solid("../res/image/wrong.png", (160*i+320, 160*3-1280)))
for i in range(7, 22):
    blocks.append(solid("../res/image/wrong.png", (160*i+320, 160*15-1280)))

# 创建时钟对象（控制游戏的FPS）

clock = pygame.time.Clock()

# 主循环

while True:

    # 锁60帧

    clock.tick(60)

# 处理事件

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            movement_x = 0
            movement_y = 0
            buyer.movement = 0
        if pygame.key.get_pressed()[pygame.K_w]:
            movement_y = buyer_speed
            buyer.towards = 4
            buyer.movement = 1
        if pygame.key.get_pressed()[pygame.K_s]:
            movement_y = -buyer_speed
            buyer.towards = 2
            buyer.movement = 1
        if pygame.key.get_pressed()[pygame.K_a]:
            movement_x = buyer_speed
            buyer.towards = 3
            buyer.movement = 1
        if pygame.key.get_pressed()[pygame.K_d]:
            movement_x = -buyer_speed
            buyer.towards = 1
            buyer.movement = 1


# 处理上下碰撞
    if (movement_x == 0 and movement_y != 0):
        flag_ud = 1
        for i in blocks:
            i.rect.top += movement_y
            if pygame.sprite.collide_rect(buyer, i):
                i.rect.top -= movement_y
                flag_ud = 0
                break
            i.rect.top -= movement_y
        if flag_ud == 1:
            background_y += movement_y
            for i in blocks:
                i.rect.top += movement_y

# 处理左右碰撞
    if (movement_y == 0 and movement_x != 0):
        flag_lr = 1
        for i in blocks:
            i.rect.left += movement_x
            if pygame.sprite.collide_rect(buyer, i):
                i.rect.left -= movement_x
                flag_lr = 0
                break
            i.rect.left -= movement_x
        if flag_lr == 1:
            background_x += movement_x
            for i in blocks:
                i.rect.left += movement_x

# 处理斜碰
    if (movement_y != 0 and movement_x != 0):
        flag = 1
        flag_ud = 1
        m_x1 = (int)(movement_x / math.sqrt(2))
        m_y1 = (int)(movement_y / math.sqrt(2))
        for i in blocks:
            i.rect.left += m_x1
            i.rect.top += m_y1
            if pygame.sprite.collide_rect(buyer, i):
                i.rect.left -= m_x1
                i.rect.top -= m_y1
                flag = 0
                break
            i.rect.left -= m_x1
            i.rect.top -= m_y1
        if flag == 1:
            background_x += m_x1
            background_y += m_y1
            for i in blocks:
                i.rect.left += m_x1
                i.rect.top += m_y1
        else:
            # 处理上下碰撞
            flag_ud = 1
            for i in blocks:
                i.rect.top += movement_y
                if pygame.sprite.collide_rect(buyer, i):
                    i.rect.top -= movement_y
                    flag_ud = 0
                    break
                i.rect.top -= movement_y
            if flag_ud == 1:
                background_y += movement_y
                for i in blocks:
                    i.rect.top += movement_y
            # 处理左右碰撞
            flag_lr = 1
            for i in blocks:
                i.rect.left += movement_x
                if pygame.sprite.collide_rect(buyer, i):
                    i.rect.left -= movement_x
                    flag_lr = 0
                    break
                i.rect.left -= movement_x
            if flag_lr == 1:
                background_x += movement_x
                for i in blocks:
                    i.rect.left += movement_x

# 打印图像

    main_screen.blit(image_background, (background_x, background_y))

    for i in blocks:
        main_screen.blit(i.image, i.rect)
    if buyer.movement == 1:
        buyer.update(pygame.time.get_ticks())
    else:
        buyer.index = buyer.firstframe[buyer.towards]
    buyer.image = buyer.images[buyer.index]
    main_screen.blit(buyer.image, buyer.rect)
    pygame.display.flip()
