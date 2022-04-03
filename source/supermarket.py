#导入模块

import sys
import pygame
import math

#pygame初始化

pygame.init()

#设置主窗口

main_screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption("这是一个标题")
image_icon = pygame.image.load("../res/image/icon.png").convert()
pygame.display.set_icon(image_icon)

#设置背景

image_background = pygame.image.load("../res/image/map.png").convert()
background_x = 320
background_y = -1280

#初始化移动变量

movement_x = 0
movement_y = 0

#定义实体类

class solid(pygame.sprite.Sprite):
    def __init__(self,filename,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = location

#设置角色
        
buyer = solid("../res/image/player_right.png" , (640-64,480-64))
buyer_speed = 12
max_speed = 12
min_speed = 6
#设置背包

bag_volume = 10
bag_left = 10
bag_item = [0,0,0,0]

#设置战果

result_item = [0,0,0,0]

#设置障碍物和柜子

blocks = []

shelf = []
for i in range(0,6):
    shelf.append([])

for i in range(8,26):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*3-1280)))
for i in range(10,20):
    shelf[0].append(solid("../res/image/wrong.png" , (160*i+320,160*4-1280-80)))
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*7-1280)))
    shelf[1].append(solid("../res/image/wrong.png" , (160*i+320,160*8-1280-80)))
for i in range(8,18):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*11-1280)))
    shelf[3].append(solid("../res/image/wrong.png" , (160*i+320,160*12-1280-80)))
for i in range(22,26):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*5-1280)))
    shelf[2].append(solid("../res/image/wrong.png" , (160*i+320,160*6-1280-80)))
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*9-1280)))
    shelf[2].append(solid("../res/image/wrong.png" , (160*i+320,160*10-1280-80)))
for i in range(4,13):
    blocks.append(solid("../res/image/wrong.png" , (160*26+320,160*i-1280)))
for i in range(8,19):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*15-1280)))
for i in range(4,8):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*6-1280)))
for i in range(7,10):
    blocks.append(solid("../res/image/wrong.png" , (480+320,160*i-1280)))
for i in range(12,13):
    blocks.append(solid("../res/image/wrong.png" , (480+320,160*i-1280)))
for i in range(4,6):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*13-1280)))
for i in range(20,26):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*13-1280)))
for i in range(6,8):
    shelf[4].append(solid("../res/image/wrong.png" , (160*i+320,160*14-1280)))
for i in range(19,20):
    shelf[5].append(solid("../res/image/wrong.png" , (160*i+320,160*14-1280)))
for i in range(4,6):
    blocks.append(solid("../res/image/wrong.png" , (160*7+320,160*i-1280)))
for i in range(1,3):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*9-1280)))
for i in range(1,3):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*12-1280)))
for i in range(10,12):
    blocks.append(solid("../res/image/wrong.png" , (320,160*i-1280)))


#定义碰撞函数

def solid_collide_y(a,m_y,b):
    for i in a:
        i.rect.top += m_y
        if pygame.sprite.collide_rect(b , i):
            i.rect.top -= m_y
            return 0
        i.rect.top -= m_y
    return 1

def solid_collide_x(a,m_x,b):
    for i in a:
        i.rect.left += m_x
        if pygame.sprite.collide_rect(b , i):
            i.rect.left -= m_x
            return 0
        i.rect.left -= m_x
    return 1

def solid_collide_xy(a,m_x,m_y,b):
    for i in a:
        i.rect.left += m_x
        i.rect.top += m_y
        if pygame.sprite.collide_rect(b , i):
            i.rect.left -= m_x
            i.rect.top -= m_y
            return 0
        i.rect.left -= m_x
        i.rect.top -= m_y
    return 1
            
#创建时钟对象（控制游戏的FPS）

clock = pygame.time.Clock()

#主循环

while True:

#锁120帧

    clock.tick(60)

#更新速度

    buyer_speed = (int)(max_speed-(max_speed-min_speed)*(bag_volume-bag_left)/bag_volume)
    
#处理事件
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            movement_x = 0
            movement_y = 0
        if pygame.key.get_pressed()[pygame.K_w]:
            movement_y = buyer_speed
        if pygame.key.get_pressed()[pygame.K_s]:
            movement_y = -buyer_speed
        if pygame.key.get_pressed()[pygame.K_a]:
            movement_x = buyer_speed
        if pygame.key.get_pressed()[pygame.K_d]:
            movement_x = -buyer_speed
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if  96 <= background_x <= 480 and -1376 <= background_y <= -1184:
                for i in range(0,4):
                    result_item[i] += bag_item[i]
                    bag_item[i] = 0
            flag = 1
            
  
#处理上下碰撞

    if (movement_x == 0 and movement_y != 0):
        if (solid_collide_y(blocks,movement_y,buyer) == 1):
            flag = 1
            for i in range(0,6):
                if (solid_collide_y(shelf[i],movement_y,buyer) == 0):
                    flag = 0
                    break
            if flag == 1:
                background_y += movement_y
                for i in blocks:
                    i.rect.top += movement_y
                for j in range(0,6):
                    for i in shelf[j]:
                        i.rect.top += movement_y
                        
#处理左右碰撞
    if (movement_y == 0 and movement_x != 0):
        if (solid_collide_x(blocks,movement_x,buyer) == 1):
            flag = 1
            for i in range(0,6):
                if (solid_collide_x(shelf[i],movement_x,buyer) == 0):
                    flag = 0
                    break
            if flag == 1:
                background_x += movement_x
                for i in blocks:
                    i.rect.left += movement_x
                for j in range(0,6):
                    for i in shelf[j]:
                        i.rect.left += movement_x
    
#处理斜碰
    if (movement_y != 0 and movement_x != 0):
        flag = 1
        flag_ud = 1
        m_x1 = (int)(movement_x / math.sqrt(2))
        m_y1 = (int)(movement_y / math.sqrt(2))
        flag = 1
        if (solid_collide_xy(blocks,m_x1,m_y1,buyer) == 1):
            for i in range(0,6):
                if (solid_collide_xy(shelf[i],m_x1,m_y1,buyer) == 0):
                    flag = 0
                    break
            if flag == 1:
                background_x += m_x1
                background_y += m_y1
                for i in blocks:
                    i.rect.left += m_x1
                    i.rect.top += m_y1
                for j in range(0,6):
                    for i in shelf[j]:
                        i.rect.left += m_x1
                        i.rect.top += m_y1
        else:
            flag = 0
        if flag == 0:
            #处理上下碰撞
            if (solid_collide_y(blocks,movement_y,buyer) == 1):
                flagud = 1
                for i in range(0,6):
                    if (solid_collide_y(shelf[i],movement_y,buyer) == 0):
                        flagud = 0
                        break
                if flagud == 1:
                    background_y += movement_y
                    for i in blocks:
                        i.rect.top += movement_y
                    for j in range(0,6):
                        for i in shelf[j]:
                            i.rect.top += movement_y
            #处理左右碰撞
            if (solid_collide_x(blocks,movement_x,buyer) == 1):
                flaglr = 1
                for i in range(0,6):
                    if (solid_collide_x(shelf[i],movement_x,buyer) == 0):
                        flaglr = 0
                        break
                if flaglr == 1:
                    background_x += movement_x
                    for i in blocks:
                        i.rect.left += movement_x
                    for j in range(0,6):
                        for i in shelf[j]:
                            i.rect.left += movement_x
            
#打印图像

    main_screen.blit( image_background , ( background_x , background_y ))

    '''
    for i in blocks:
        main_screen.blit( i.image , i.rect )
    
        
    for j in range(0,6):
        for i in shelf[j]:
            main_screen.blit( i.image , i.rect )
    '''
    
    main_screen.blit( buyer.image , buyer.rect )
    
    pygame.display.flip()
