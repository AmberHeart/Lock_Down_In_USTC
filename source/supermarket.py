#导入模块

import sys
import pygame

#pygame初始化

pygame.init()

#设置主窗口

main_screen = pygame.display.set_mode((800,640))
pygame.display.set_caption("这是一个标题")
image_icon = pygame.image.load("../res/icon.png").convert()
pygame.display.set_icon(image_icon)

#设置背景

image_background = pygame.image.load("../res/background.png").convert()
background_x = 0
background_y = 0

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
        
buyer = solid("../res/buyer.png" , (400-64,320-64))
buyer_speed = 8

#设置障碍物

shelf = []
for i in range(1,5):
    shelf.append(solid("../res/shelf1.png" , (200+i*128,128)))
for i in range(3,5):
    shelf.append(solid("../res/shelf1.png" , (200+i*128,350)))

wall = []
for i in range(1,10):
    wall.append(solid("../res/wall1.png" , (i*128-128,0)))
for i in range(1,10):
    wall.append(solid("../res/wall1.png" , (i*128-128,640-128)))
for i in range(1,10):
    wall.append(solid("../res/wall1.png" , (0,i*128-128)))
for i in range(1,10):
    wall.append(solid("../res/wall1.png" , (800-128,i*128-128)))

#创建时钟对象（控制游戏的FPS）

clock = pygame.time.Clock()

#主循环

while True:

#锁60帧

    clock.tick(60)
    
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
        
    
#处理碰撞
    flag = 1
    for i in shelf:
        i.rect.left += movement_x
        i.rect.top += movement_y
        if pygame.sprite.collide_mask(buyer , i):
            i.rect.left -= movement_x
            i.rect.top -= movement_y
            flag = 0
            break
        i.rect.left -= movement_x
        i.rect.top -= movement_y
    for i in wall:
        i.rect.left += movement_x
        i.rect.top += movement_y
        if pygame.sprite.collide_mask(buyer , i):
            i.rect.left -= movement_x
            i.rect.top -= movement_y
            flag = 0
            break
        i.rect.left -= movement_x
        i.rect.top -= movement_y
    if flag == 1:
        background_x += movement_x
        background_y += movement_y
        for i in shelf:
            i.rect.left += movement_x
            i.rect.top += movement_y
        for i in wall:
            i.rect.left += movement_x
            i.rect.top += movement_y
        
    
#打印图像
    
    main_screen.blit( image_background , ( background_x , background_y ))
    for i in wall:
        main_screen.blit( i.image , i.rect )
    for i in shelf:
        main_screen.blit( i.image , i.rect )
    main_screen.blit( buyer.image , buyer.rect )
    
    pygame.display.flip()
